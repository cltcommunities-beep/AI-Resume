class ForceDirectedGraph {
  constructor(canvas, onNodeClick, onEdgeClick) {
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.onNodeClick = onNodeClick;
    this.onEdgeClick = onEdgeClick;
    this.nodes = [];
    this.edges = [];
    this.zoom = 1;
    this.panX = 0;
    this.panY = 0;
    this.cssW = 1000;
    this.cssH = 520;
    this.draggedNode = null;
    this.hoveredNode = null;
    this.hoveredEdge = null;
    this.selectedSectorId = null;
    this.ripples = [];
    this.isPaused = false;
    this.time = 0;
    this._initEvents();
    this._startLoop();
  }

  resize() {
    const container = (typeof document !== "undefined" ? document.getElementById("networkContainer") : null) || (this.canvas ? this.canvas.parentElement : null);
    const isFull = (typeof document !== "undefined" && document.fullscreenElement === container) || (container && container.classList && container.classList.contains("fullscreen-active"));
    
    if (isFull) {
      this.cssW = (typeof window !== "undefined") ? window.innerWidth : 1200;
      this.cssH = (typeof window !== "undefined") ? window.innerHeight : 700;
    } else {
      const parentW = container ? container.clientWidth : 0;
      this.cssW = Math.max(320, parentW > 100 ? parentW : 800);
      this.cssH = 520;
    }

    const dpr = (typeof window !== "undefined" && window.devicePixelRatio) || 1;
    this.canvas.width = Math.floor(this.cssW * dpr);
    this.canvas.height = Math.floor(this.cssH * dpr);
    this.canvas.style.width = "100%";
    this.canvas.style.height = this.cssH + "px";
  }

    setData(data) {
    this.resize();
    const cx = this.cssW / 2;
    const cy = this.cssH / 2;

    const sectorClusters = {
      power_nuclear: { x: cx + 210, y: cy + 110 },
      cooling_thermal: { x: cx + 20, y: cy - 140 },
      ai_compute: { x: cx - 210, y: cy - 100 },
      neocloud_dc: { x: cx - 180, y: cy + 120 },
      fintech_banking: { x: cx - 290, y: cy + 30 },
      software_defense: { x: cx + 230, y: cy - 100 }
    };

    const sectorCounts = {};
    this.nodes = data.nodes.map(node => {
      const sId = node.sectorId || "ai_compute";
      sectorCounts[sId] = (sectorCounts[sId] || 0) + 1;
      const idx = sectorCounts[sId] - 1;
      const cluster = sectorClusters[sId] || { x: cx, y: cy };
      const angle = (idx * 1.57);
      const dist = 48 + idx * 26;

      return {
        ...node,
        x: cluster.x + Math.cos(angle) * dist,
        y: cluster.y + Math.sin(angle) * dist,
        vx: 0,
        vy: 0
      };
    });
    this.edges = data.edges;
  }

  zoomIn() {
    this.zoom = Math.min(2.4, this.zoom * 1.2);
  }

  zoomOut() {
    this.zoom = Math.max(0.45, this.zoom * 0.83);
  }

  
  setSectorFilter(sectorId) {
    this.selectedSectorId = (this.selectedSectorId === sectorId) ? null : sectorId;
    if (this.selectedSectorId) {
      this.nodes.forEach(n => {
        if (n.sectorId === this.selectedSectorId) {
          this.triggerRipple(n.id, "#10b981");
        }
      });
    }
  }

  resetView() {
    this.zoom = 1;
    this.panX = 0;
    this.panY = 0;
  }

  focusNode(symbol) {
    const n = this.nodes.find(node => node.id === symbol);
    if (n) {
      this.panX = (this.cssW / 2 - n.x);
      this.panY = (this.cssH / 2 - n.y);
      this.zoom = 1.25;
      this.triggerRipple(symbol, "#38bdf8");
      if (this.onNodeClick) this.onNodeClick(symbol);
    }
  }

  triggerRipple(symbol, color) {
    const node = this.nodes.find(n => n.id === symbol);
    if (node) {
      this.ripples.push({ x: node.x, y: node.y, radius: 10, maxRadius: 110, color, alpha: 1 });
    }
  }

  _startLoop() {
    const step = (timestamp) => {
      this.time = (timestamp || (typeof performance !== "undefined" ? performance.now() : Date.now())) * 0.0018;
      if (!this.isPaused) {
        this._updatePhysics();
      }
      this.render();
      if (typeof requestAnimationFrame !== "undefined") {
        requestAnimationFrame(step);
      }
    };
    if (typeof requestAnimationFrame !== "undefined") {
      requestAnimationFrame(step);
    }
  }

    _updatePhysics() {
    const cx = this.cssW / 2;
    const cy = this.cssH / 2;

    const sectorClusters = {
      power_nuclear: { x: cx + 210, y: cy + 110 },
      cooling_thermal: { x: cx + 20, y: cy - 140 },
      ai_compute: { x: cx - 210, y: cy - 100 },
      neocloud_dc: { x: cx - 180, y: cy + 120 },
      fintech_banking: { x: cx - 290, y: cy + 30 },
      software_defense: { x: cx + 230, y: cy - 100 }
    };

    // 1. Strict Hard Collision Anti-Overlap & Mutual Separation
    for (let i = 0; i < this.nodes.length; i++) {
      for (let j = i + 1; j < this.nodes.length; j++) {
        const a = this.nodes[i];
        const b = this.nodes[j];
        const dx = b.x - a.x;
        const dy = b.y - a.y;
        const dist = Math.hypot(dx, dy) || 1;
        const minDist = a.size + b.size + 56; // Minimum 116px clearance so badges never touch!

        if (dist < minDist) {
          const overlap = minDist - dist;
          const nx = dx / dist;
          const ny = dy / dist;
          // Direct geometric separation (impossible to overlap)
          a.x -= nx * overlap * 0.52;
          a.y -= ny * overlap * 0.52;
          b.x += nx * overlap * 0.52;
          b.y += ny * overlap * 0.52;

          a.vx -= nx * overlap * 0.08;
          a.vy -= ny * overlap * 0.08;
          b.vx += nx * overlap * 0.08;
          b.vy += ny * overlap * 0.08;
        } else if (dist < 190) {
          const repel = (190 - dist) / 190;
          const force = repel * 0.5;
          const fx = (dx / dist) * force;
          const fy = (dy / dist) * force;
          a.vx -= fx;
          a.vy -= fy;
          b.vx += fx;
          b.vy += fy;
        }
      }
    }

    // 2. Gentle Spring Attraction along Connected Edges
    this.edges.forEach(e => {
      const a = this.nodes.find(n => n.id === e.source);
      const b = this.nodes.find(n => n.id === e.target);
      if (a && b) {
        const dx = b.x - a.x;
        const dy = b.y - a.y;
        const dist = Math.hypot(dx, dy) || 1;
        const targetDist = 145;
        if (dist > targetDist) {
          const force = (dist - targetDist) * 0.008;
          const fx = (dx / dist) * force;
          const fy = (dy / dist) * force;
          a.vx += fx;
          a.vy += fy;
          b.vx -= fx;
          b.vy -= fy;
        }
      }
    });

    // 3. Sector Cluster Gravity & Safe Canvas Margin Bounding
    this.nodes.forEach(n => {
      if (n !== this.draggedNode) {
        const cluster = sectorClusters[n.sectorId] || { x: cx, y: cy };
        // Gentle pull towards spacious sector neighborhood
        n.vx += (cluster.x - n.x) * 0.007;
        n.vy += (cluster.y - n.y) * 0.007;

        const speed = Math.hypot(n.vx, n.vy);
        if (speed > 2.8) {
          n.vx = (n.vx / speed) * 2.8;
          n.vy = (n.vy / speed) * 2.8;
        }

        n.vx *= 0.82;
        n.vy *= 0.82;
        n.x += n.vx;
        n.y += n.vy;

        // Strict Margin Bounding
        n.x = Math.max(n.size + 24, Math.min(this.cssW - n.size - 24, n.x));
        n.y = Math.max(n.size + 24, Math.min(this.cssH - n.size - 24, n.y));
      }
    });

    // 4. Ripples
    for (let i = this.ripples.length - 1; i >= 0; i--) {
      const r = this.ripples[i];
      r.radius += 2.5;
      r.alpha = Math.max(0, 1 - (r.radius / r.maxRadius));
      if (r.radius >= r.maxRadius) this.ripples.splice(i, 1);
    }
  }

  render() {
    const ctx = this.ctx;
    const dpr = (typeof window !== "undefined" && window.devicePixelRatio) || 1;
    const w = this.cssW;
    const h = this.cssH;
    const t = this.time;

    ctx.save();
    ctx.scale(dpr, dpr);
    ctx.clearRect(0, 0, w, h);

    ctx.translate(w / 2, h / 2);
    ctx.scale(this.zoom, this.zoom);
    ctx.translate(-w / 2 + this.panX, -h / 2 + this.panY);

    // 1. Ripples
    this.ripples.forEach(r => {
      ctx.beginPath();
      ctx.arc(r.x, r.y, r.radius, 0, Math.PI * 2);
      ctx.strokeStyle = r.color;
      ctx.lineWidth = 2.5;
      ctx.globalAlpha = r.alpha;
      ctx.stroke();
      ctx.globalAlpha = 1.0;
    });

    // 2. Connecting Edges & Animated Star Flow Sparkles
    this.edges.forEach(e => {
      const a = this.nodes.find(n => n.id === e.source);
      const b = this.nodes.find(n => n.id === e.target);
      if (a && b) {

        const isHovered = (e === this.hoveredEdge);
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.strokeStyle = isHovered ? "#ffffff" : e.color;
        ctx.lineWidth = isHovered ? 3.5 : (e.type === "UPSTREAM" ? 2.2 : 1.3);
        if (e.type === "DOWNSTREAM") ctx.setLineDash([4, 4]);
        else if (e.type === "COMPETITOR") ctx.setLineDash([2, 2]);
        else ctx.setLineDash([]);
        ctx.stroke();
        ctx.setLineDash([]);

        // Animated Energy / Supply Flow Sparkles
        const dx = b.x - a.x;
        const dy = b.y - a.y;
        const p1 = (t * 0.45) % 1;
        const p2 = (t * 0.45 + 0.5) % 1;

        [p1, p2].forEach(p => {
          const px = a.x + dx * p;
          const py = a.y + dy * p;
          ctx.beginPath();
          ctx.arc(px, py, 3.2, 0, Math.PI * 2);
          ctx.fillStyle = isHovered ? "#ffffff" : (e.type === "UPSTREAM" ? "#38bdf8" : (e.type === "DOWNSTREAM" ? "#c084fc" : "#fbbf24"));
          ctx.fill();
        });

        if (isHovered) {
          const midX = (a.x + b.x) / 2;
          const midY = (a.y + b.y) / 2;
          ctx.fillStyle = "rgba(2, 6, 23, 0.96)";
          ctx.strokeStyle = "#38bdf8";
          ctx.lineWidth = 1;
          ctx.beginPath();
          if (ctx.roundRect) ctx.roundRect(midX - 90, midY - 14, 180, 28, 6);
          else ctx.rect(midX - 90, midY - 14, 180, 28);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = "#38bdf8";
          ctx.font = "bold 10px sans-serif";
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          ctx.fillText(e.source + " ➔ " + e.target + " (Click Flow)", midX, midY);
        }
      }
    });

    // 3. Stock Nodes - Picture Book Design (Large Friendly Emojis + Bobbing)
    this.nodes.forEach(n => {
      const isHovered = (n === this.hoveredNode);
      const isSectorMatch = !this.selectedSectorId || (n.sectorId === this.selectedSectorId);
      ctx.globalAlpha = isSectorMatch ? 1.0 : 0.22;
      const r = n.size;
      // Gentle playful floating bob
      const bob = Math.sin(t * 2.8 + (n.x * 0.05)) * 2.8;

      // Outer Glow Halo
      ctx.beginPath();
      ctx.arc(n.x, n.y + bob, r + (isHovered ? 8 : 3), 0, Math.PI * 2);
      ctx.fillStyle = isHovered ? "rgba(56, 189, 248, 0.4)" : "rgba(15, 23, 42, 0.55)";
      ctx.fill();

      // Circular Node Base
      ctx.beginPath();
      ctx.arc(n.x, n.y + bob, r, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(15, 23, 42, 0.95)";
      ctx.fill();
      ctx.lineWidth = isHovered ? 3.5 : 2.2;
      ctx.strokeStyle = isHovered ? "#ffffff" : n.color;
      ctx.stroke();

      // Giant Colorful Kid Emoji (Apple/Google/Segoe emoji font)
      const emojiSize = Math.round(r * 0.78);
      ctx.font = emojiSize + "px sans-serif";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(n.kidEmoji || "🏢", n.x, n.y - r * 0.18 + bob);

      // High-Contrast Kid Role Pill inside the circle bottom
      this._drawKidPill(ctx, n.kidTitle || n.label, n.x, n.y + r * 0.52 + bob, r, n.color);

      // Return & Ticker Sub-Badge Underneath Circle
      this._drawUnderNodeBadge(ctx, n.label, n.change1D, n.x, n.y + r + 13 + bob);
      ctx.globalAlpha = 1.0;
    });

    // 4. Detailed Storybook Hover Card
    if (this.hoveredNode) {
      const n = this.hoveredNode;
      const cardW = 290;
      const cardH = 108;
      const cardX = Math.min(w - cardW - 14, Math.max(14, n.x + 18));
      const cardY = Math.min(h - cardH - 14, Math.max(14, n.y - 50));

      ctx.fillStyle = "rgba(2, 6, 23, 0.97)";
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      if (ctx.roundRect) ctx.roundRect(cardX, cardY, cardW, cardH, 10);
      else ctx.rect(cardX, cardY, cardW, cardH);
      ctx.fill();
      ctx.stroke();

      ctx.textAlign = "left";
      ctx.textBaseline = "alphabetic";
      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText((n.kidEmoji || "🏢") + " " + n.label + " — " + (n.kidTitle || n.name), cardX + 12, cardY + 20);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 11px sans-serif";
      ctx.fillText("👶 What it does: " + (n.kidJob || n.whatItDoes).slice(0, 44) + "...", cardX + 12, cardY + 40);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "10px sans-serif";
      ctx.fillText("🤝 Friends: " + (n.kidFriend || n.whoBuys).slice(0, 45) + "...", cardX + 12, cardY + 62);

      ctx.fillStyle = "#fbbf24";
      ctx.font = "bold 10px monospace";
      ctx.fillText("Price: $" + n.price.toFixed(2) + " · YoY Growth: +" + n.growthYoY + "%", cardX + 12, cardY + 82);

      ctx.fillStyle = "#34d399";
      ctx.font = "bold 9.5px sans-serif";
      ctx.fillText("👉 Click to see the fun animated story!", cardX + 12, cardY + 98);
    }

    ctx.restore();
  }

  _drawKidPill(ctx, kidTitle, x, y, r, sectorColor) {
    const pillW = Math.max(42, kidTitle.length * 6.5 + 10);
    const pillH = 13;
    ctx.fillStyle = "rgba(2, 6, 23, 0.95)";
    ctx.strokeStyle = sectorColor;
    ctx.lineWidth = 1;
    ctx.beginPath();
    if (ctx.roundRect) ctx.roundRect(x - pillW / 2, y - pillH / 2, pillW, pillH, 4);
    else ctx.rect(x - pillW / 2, y - pillH / 2, pillW, pillH);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "#ffffff";
    ctx.font = "bold 8.5px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(kidTitle, x, y);
  }

  _drawUnderNodeBadge(ctx, ticker, change1D, x, y) {
    const sign = change1D >= 0 ? "+" : "";
    const txt = ticker + " (" + sign + change1D + "%)";
    const bg = change1D >= 0 ? "rgba(6, 78, 59, 0.95)" : "rgba(127, 29, 29, 0.95)";
    const border = change1D >= 0 ? "#10b981" : "#ef4444";
    const fg = change1D >= 0 ? "#34d399" : "#fca5a5";

    const badgeW = txt.length * 6.5 + 8;
    const badgeH = 13;
    ctx.fillStyle = bg;
    ctx.strokeStyle = border;
    ctx.lineWidth = 0.9;
    ctx.beginPath();
    if (ctx.roundRect) ctx.roundRect(x - badgeW / 2, y - badgeH / 2, badgeW, badgeH, 3);
    else ctx.rect(x - badgeW / 2, y - badgeH / 2, badgeW, badgeH);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = fg;
    ctx.font = "bold 8.5px ui-monospace, SFMono-Regular, monospace";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(txt, x, y);
  }

  _initEvents() {
    this.resize();
    if (typeof window !== "undefined") {
      window.addEventListener("resize", () => {
        this.resize();
      });
    }

    const getPos = (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;
      const x = (mx - this.cssW / 2) / this.zoom + this.cssW / 2 - this.panX;
      const y = (my - this.cssH / 2) / this.zoom + this.cssH / 2 - this.panY;
      return { x, y, mx, my };
    };

    let isPanning = false;
    let startPanX = 0;
    let startPanY = 0;

    this.canvas.addEventListener("mousemove", e => {
      const pos = getPos(e);
      let foundNode = null;
      for (const n of this.nodes) {
        const dx = n.x - pos.x;
        const dy = n.y - pos.y;
        if (Math.sqrt(dx * dx + dy * dy) <= n.size + 6) {
          foundNode = n;
          break;
        }
      }
      this.hoveredNode = foundNode;

      let foundEdge = null;
      if (!foundNode) {
        for (const edge of this.edges) {
          const a = this.nodes.find(n => n.id === edge.source);
          const b = this.nodes.find(n => n.id === edge.target);
          if (a && b) {
            const dist = distToSegment(pos.x, pos.y, a.x, a.y, b.x, b.y);
            if (dist <= 8) {
              foundEdge = edge;
              break;
            }
          }
        }
      }
      this.hoveredEdge = foundEdge;

      this.canvas.style.cursor = (foundNode || foundEdge) ? "pointer" : (isPanning ? "grabbing" : "grab");

      if (this.draggedNode) {
        this.draggedNode.x = pos.x;
        this.draggedNode.y = pos.y;
        this.draggedNode.vx = 0;
        this.draggedNode.vy = 0;
      } else if (isPanning) {
        this.panX += (e.clientX - startPanX) / this.zoom;
        this.panY += (e.clientY - startPanY) / this.zoom;
        startPanX = e.clientX;
        startPanY = e.clientY;
      }
    });

    this.canvas.addEventListener("mousedown", e => {
      const pos = getPos(e);
      if (this.hoveredNode) {
        this.draggedNode = this.hoveredNode;
      } else if (this.hoveredEdge) {
        if (this.onEdgeClick) this.onEdgeClick(this.hoveredEdge.source, this.hoveredEdge.target);
      } else {
        isPanning = true;
        startPanX = e.clientX;
        startPanY = e.clientY;
      }
    });

    if (typeof window !== "undefined") {
      window.addEventListener("mouseup", () => {
        if (this.draggedNode) {
          if (this.onNodeClick) this.onNodeClick(this.draggedNode.id);
          this.draggedNode = null;
        }
        isPanning = false;
      });
    }

    this.canvas.addEventListener("wheel", e => {
      e.preventDefault();
      if (e.deltaY < 0) this.zoomIn();
      else this.zoomOut();
    }, { passive: false });
  }
}

function distToSegment(px, py, x1, y1, x2, y2) {
  const l2 = (x2 - x1) ** 2 + (y2 - y1) ** 2;
  if (l2 === 0) return Math.hypot(px - x1, py - y1);
  let t = ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / l2;
  t = Math.max(0, Math.min(1, t));
  return Math.hypot(px - (x1 + t * (x2 - x1)), py - (y1 + t * (y2 - y1)));
}

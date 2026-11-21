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
      this.cssW = window.innerWidth;
      this.cssH = window.innerHeight;
    } else {
      const parentW = container ? container.clientWidth : 0;
      const rectW = this.canvas ? this.canvas.getBoundingClientRect().width : 0;
      this.cssW = Math.max(900, rectW > 100 ? rectW : (parentW > 100 ? parentW : 1100));
      this.cssH = 520;
    }

    const dpr = (typeof window !== "undefined" && window.devicePixelRatio) || 1;
    this.canvas.width = Math.floor(this.cssW * dpr);
    this.canvas.height = Math.floor(this.cssH * dpr);
    this.canvas.style.width = this.cssW + "px";
    this.canvas.style.height = this.cssH + "px";
  }

  setData(data) {
    this.resize();
    const cx = this.cssW / 2;
    const cy = this.cssH / 2;

    const n = data.nodes.length;
    const innerCount = Math.min(8, n);
    const outerCount = n - innerCount;

    this.nodes = data.nodes.map((node, i) => {
      let angle, radius;
      if (i < innerCount) {
        angle = (i * 2 * Math.PI) / innerCount;
        radius = 135 + (i % 2) * 25;
      } else {
        const outIdx = i - innerCount;
        angle = (outIdx * 2 * Math.PI) / outerCount + (Math.PI / outerCount);
        radius = 230 + (outIdx % 2) * 30;
      }
      return {
        ...node,
        x: cx + Math.cos(angle) * radius,
        y: cy + Math.sin(angle) * radius,
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
      this.zoom = 1.35;
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

    // Node Repulsion (Anti-Clumping)
    for (let i = 0; i < this.nodes.length; i++) {
      for (let j = i + 1; j < this.nodes.length; j++) {
        const a = this.nodes[i];
        const b = this.nodes[j];
        const dx = b.x - a.x;
        const dy = b.y - a.y;
        const dist = Math.hypot(dx, dy) || 1;
        if (dist < 210) {
          const repel = (210 - dist) / 210;
          const force = repel * repel * 1.9;
          const fx = (dx / dist) * force;
          const fy = (dy / dist) * force;
          a.vx -= fx;
          a.vy -= fy;
          b.vx += fx;
          b.vy += fy;
        }
      }
    }

    // Spring Attraction along Connected Edges
    this.edges.forEach(e => {
      const a = this.nodes.find(n => n.id === e.source);
      const b = this.nodes.find(n => n.id === e.target);
      if (a && b) {
        const dx = b.x - a.x;
        const dy = b.y - a.y;
        const dist = Math.hypot(dx, dy) || 1;
        const targetDist = 145;
        const force = (dist - targetDist) * 0.018;
        const fx = (dx / dist) * force;
        const fy = (dy / dist) * force;
        a.vx += fx;
        a.vy += fy;
        b.vx -= fx;
        b.vy -= fy;
      }
    });

    // Centering Gravity, Velocity Clamping, Damping & Safe Bounds
    this.nodes.forEach(n => {
      if (n !== this.draggedNode) {
        n.vx += (cx - n.x) * 0.008;
        n.vy += (cy - n.y) * 0.008;

        const speed = Math.hypot(n.vx, n.vy);
        if (speed > 4.2) {
          n.vx = (n.vx / speed) * 4.2;
          n.vy = (n.vy / speed) * 4.2;
        }

        n.vx *= 0.86;
        n.vy *= 0.86;
        n.x += n.vx;
        n.y += n.vy;

        // Strict Bounding
        n.x = Math.max(n.size + 16, Math.min(this.cssW - n.size - 16, n.x));
        n.y = Math.max(n.size + 16, Math.min(this.cssH - n.size - 16, n.y));
      }
    });

    // Ripples
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

    ctx.translate(w / 2 + this.panX, h / 2 + this.panY);
    ctx.scale(this.zoom, this.zoom);
    ctx.translate(-w / 2, -h / 2);

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

    // 2. Connecting Edges & Animated Flow Particles
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

        // Animated Energy / Product Flow Particles
        const dx = b.x - a.x;
        const dy = b.y - a.y;
        const dist = Math.hypot(dx, dy) || 1;
        const p1 = (t * 0.45) % 1;
        const p2 = (t * 0.45 + 0.5) % 1;

        [p1, p2].forEach(p => {
          const px = a.x + dx * p;
          const py = a.y + dy * p;
          ctx.beginPath();
          ctx.arc(px, py, 2.8, 0, Math.PI * 2);
          ctx.fillStyle = isHovered ? "#ffffff" : (e.type === "UPSTREAM" ? "#38bdf8" : (e.type === "DOWNSTREAM" ? "#c084fc" : "#fb923c"));
          ctx.shadowColor = ctx.fillStyle;
          ctx.shadowBlur = 6;
          ctx.fill();
          ctx.shadowBlur = 0;
        });

        if (isHovered) {
          const midX = (a.x + b.x) / 2;
          const midY = (a.y + b.y) / 2;
          ctx.fillStyle = "rgba(2, 6, 23, 0.96)";
          ctx.strokeStyle = "#38bdf8";
          ctx.lineWidth = 1;
          ctx.beginPath();
          if (ctx.roundRect) ctx.roundRect(midX - 85, midY - 14, 170, 28, 6);
          else ctx.rect(midX - 85, midY - 14, 170, 28);
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

    // 3. Stock Nodes with Looping Animated Business Visuals
    this.nodes.forEach(n => {
      const isHovered = (n === this.hoveredNode);
      const r = n.size;

      // Outer Glow Halo
      ctx.beginPath();
      ctx.arc(n.x, n.y, r + (isHovered ? 8 : 3), 0, Math.PI * 2);
      ctx.fillStyle = isHovered ? "rgba(56, 189, 248, 0.35)" : "rgba(15, 23, 42, 0.55)";
      ctx.fill();

      // Circular Node Base
      ctx.beginPath();
      ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(15, 23, 42, 0.94)";
      ctx.fill();
      ctx.lineWidth = isHovered ? 3.5 : 2;
      ctx.strokeStyle = isHovered ? "#ffffff" : n.color;
      ctx.stroke();

      // Animated Business Visual in Upper 65% of Node
      this._drawProceduralVisual(ctx, n, n.x, n.y - r * 0.15, r * 0.55, t);

      // Ticker Pill at Bottom of Circle
      this._drawTickerPill(ctx, n.label, n.x, n.y + r * 0.52, r, n.color);

      // Return Badge Underneath Circle
      this._drawReturnBadge(ctx, n.change1D, n.x, n.y + r + 11);
    });

    // 4. Detailed Glassmorphic Hover Card
    if (this.hoveredNode) {
      const n = this.hoveredNode;
      const cardW = 270;
      const cardH = 104;
      const cardX = Math.min(w - cardW - 14, Math.max(14, n.x + 18));
      const cardY = Math.min(h - cardH - 14, Math.max(14, n.y - 50));

      ctx.fillStyle = "rgba(2, 6, 23, 0.96)";
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 1.5;
      ctx.shadowColor = "rgba(0, 0, 0, 0.6)";
      ctx.shadowBlur = 12;
      ctx.beginPath();
      if (ctx.roundRect) ctx.roundRect(cardX, cardY, cardW, cardH, 8);
      else ctx.rect(cardX, cardY, cardW, cardH);
      ctx.fill();
      ctx.stroke();
      ctx.shadowBlur = 0;

      ctx.textAlign = "left";
      ctx.textBaseline = "alphabetic";
      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 12px sans-serif";
      ctx.fillText(n.label + " — " + n.name, cardX + 10, cardY + 18);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 10px sans-serif";
      ctx.fillText(n.simpleRole, cardX + 10, cardY + 34);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "10px sans-serif";
      const desc1 = n.whatItDoes ? n.whatItDoes.slice(0, 48) + "..." : n.layer;
      ctx.fillText(desc1, cardX + 10, cardY + 50);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "9px sans-serif";
      ctx.fillText("Customers: " + (n.whoBuys ? n.whoBuys.slice(0, 42) + "..." : "Global AI Giants"), cardX + 10, cardY + 66);

      ctx.fillStyle = "#fbbf24";
      ctx.font = "bold 10px monospace";
      ctx.fillText("Price: $" + n.price.toFixed(2) + " · YoY Rev: +" + n.growthYoY + "%", cardX + 10, cardY + 82);

      ctx.fillStyle = "#34d399";
      ctx.font = "bold 9px sans-serif";
      ctx.fillText("👉 Click node to explore animated story", cardX + 10, cardY + 96);
    }

    ctx.restore();
  }

  _drawTickerPill(ctx, label, x, y, r, sectorColor) {
    const pillW = Math.max(34, label.length * 7.5 + 8);
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
    ctx.font = "bold 9.5px ui-monospace, SFMono-Regular, monospace";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(label, x, y);
  }

  _drawReturnBadge(ctx, change1D, x, y) {
    const sign = change1D >= 0 ? "+" : "";
    const txt = sign + change1D + "%";
    const bg = change1D >= 0 ? "rgba(6, 78, 59, 0.9)" : "rgba(127, 29, 29, 0.9)";
    const border = change1D >= 0 ? "#10b981" : "#ef4444";
    const fg = change1D >= 0 ? "#34d399" : "#fca5a5";

    const badgeW = txt.length * 6 + 10;
    const badgeH = 12;
    ctx.fillStyle = bg;
    ctx.strokeStyle = border;
    ctx.lineWidth = 0.8;
    ctx.beginPath();
    if (ctx.roundRect) ctx.roundRect(x - badgeW / 2, y - badgeH / 2, badgeW, badgeH, 3);
    else ctx.rect(x - badgeW / 2, y - badgeH / 2, badgeW, badgeH);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = fg;
    ctx.font = "bold 8.5px ui-monospace, monospace";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(txt, x, y);
  }

  _drawProceduralVisual(ctx, n, cx, cy, rad, t) {
    const type = n.animType || "brain_gpu";
    ctx.save();
    ctx.translate(cx, cy);

    switch(type) {
      case "brain_gpu": {
        // NVDA: Glowing neural network with central AI chip
        const pulse = 0.55 + 0.45 * Math.sin(t * 3.5);
        ctx.fillStyle = "rgba(30, 58, 138, 0.8)";
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 1.2;
        ctx.strokeRect(-rad * 0.55, -rad * 0.55, rad * 1.1, rad * 1.1);
        ctx.fillRect(-rad * 0.55, -rad * 0.55, rad * 1.1, rad * 1.1);

        // Circuit Pins
        ctx.fillStyle = "#38bdf8";
        for (let i = -2; i <= 2; i++) {
          ctx.fillRect(-rad * 0.7, i * rad * 0.22 - 1, rad * 0.15, 2);
          ctx.fillRect(rad * 0.55, i * rad * 0.22 - 1, rad * 0.15, 2);
        }

        // Neural Core
        ctx.beginPath();
        ctx.arc(0, 0, rad * 0.28, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(56, 189, 248, " + pulse + ")";
        ctx.shadowColor = "#38bdf8";
        ctx.shadowBlur = 8;
        ctx.fill();
        ctx.shadowBlur = 0;

        // Neural Synapses
        for (let a = 0; a < 4; a++) {
          const ang = a * Math.PI / 2 + t * 1.2;
          const sx = Math.cos(ang) * rad * 0.45;
          const sy = Math.sin(ang) * rad * 0.45;
          ctx.beginPath();
          ctx.moveTo(0, 0);
          ctx.lineTo(sx, sy);
          ctx.strokeStyle = "#38bdf8";
          ctx.lineWidth = 0.9;
          ctx.stroke();

          ctx.beginPath();
          ctx.arc(sx, sy, 2, 0, Math.PI * 2);
          ctx.fillStyle = "#ffffff";
          ctx.fill();
        }
        break;
      }

      case "processor": {
        // AMD: Multi-core processor with orbiting bus signal
        ctx.strokeStyle = "#ef4444";
        ctx.lineWidth = 1.2;
        ctx.strokeRect(-rad * 0.6, -rad * 0.6, rad * 1.2, rad * 1.2);

        const dieSize = rad * 0.4;
        const pDie = 0.5 + 0.5 * Math.sin(t * 4);
        ctx.fillStyle = "rgba(239, 68, 68, " + (0.4 + pDie * 0.4) + ")";
        ctx.fillRect(-dieSize / 2, -dieSize / 2, dieSize, dieSize);

        // Orbiting bus clock dot
        const rot = t * 3;
        ctx.beginPath();
        ctx.arc(Math.cos(rot) * rad * 0.65, Math.sin(rot) * rad * 0.65, 2.5, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff";
        ctx.fill();
        break;
      }

      case "networking_switch": {
        // AVGO: Interconnect crossbar switch
        ctx.strokeStyle = "#a855f7";
        ctx.lineWidth = 1;
        ctx.strokeRect(-rad * 0.65, -rad * 0.45, rad * 1.3, rad * 0.9);

        // Data packet beams
        for (let i = 0; i < 3; i++) {
          const px = ((t * 2 + i * 0.33) % 1) * rad * 1.1 - rad * 0.55;
          ctx.beginPath();
          ctx.arc(px, (i - 1) * rad * 0.22, 2, 0, Math.PI * 2);
          ctx.fillStyle = "#c084fc";
          ctx.fill();
        }
        break;
      }

      case "optical_bridge": {
        // MRVL: Fiber optic photon stream
        ctx.beginPath();
        ctx.arc(0, 0, rad * 0.65, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
        ctx.lineWidth = 1.5;
        ctx.stroke();

        for (let i = 0; i < 3; i++) {
          const ang = t * 4 + i * (Math.PI * 2 / 3);
          ctx.beginPath();
          ctx.arc(Math.cos(ang) * rad * 0.65, Math.sin(ang) * rad * 0.65, 2.8, 0, Math.PI * 2);
          ctx.fillStyle = "#38bdf8";
          ctx.shadowColor = "#38bdf8";
          ctx.shadowBlur = 6;
          ctx.fill();
          ctx.shadowBlur = 0;
        }
        break;
      }

      case "chip_fab": {
        // TSM: Silicon wafer with sweeping lithography laser beam
        ctx.beginPath();
        ctx.arc(0, 0, rad * 0.7, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(139, 92, 246, 0.2)";
        ctx.strokeStyle = "#a78bfa";
        ctx.lineWidth = 1.5;
        ctx.fill();
        ctx.stroke();

        // Wafer grid
        ctx.strokeStyle = "rgba(167, 139, 250, 0.3)";
        ctx.lineWidth = 0.7;
        ctx.beginPath();
        ctx.moveTo(-rad * 0.6, 0); ctx.lineTo(rad * 0.6, 0);
        ctx.moveTo(0, -rad * 0.6); ctx.lineTo(0, rad * 0.6);
        ctx.stroke();

        // Sweeping Laser Beam
        const ang = t * 2.8;
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(Math.cos(ang) * rad * 0.7, Math.sin(ang) * rad * 0.7);
        ctx.strokeStyle = "#ec4899";
        ctx.lineWidth = 2;
        ctx.shadowColor = "#ec4899";
        ctx.shadowBlur = 8;
        ctx.stroke();
        ctx.shadowBlur = 0;
        break;
      }

      case "packaging_chip": {
        // AMKR: Microchip packaging with oscillating calipers
        ctx.strokeStyle = "#818cf8";
        ctx.lineWidth = 1;
        ctx.strokeRect(-rad * 0.45, -rad * 0.45, rad * 0.9, rad * 0.9);

        const osc = Math.sin(t * 3) * rad * 0.15;
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 1.5;
        // Left caliper
        ctx.strokeRect(-rad * 0.75 + osc, -rad * 0.35, rad * 0.2, rad * 0.7);
        // Right caliper
        ctx.strokeRect(rad * 0.55 - osc, -rad * 0.35, rad * 0.2, rad * 0.7);
        break;
      }

      case "liquid_cooling": {
        // NVT: Chilled liquid dual vortex rings
        ctx.lineWidth = 1.5;
        for (let i = 0; i < 2; i++) {
          const rRing = rad * (0.35 + i * 0.3);
          const spin = t * (i === 0 ? 3 : -2.5);
          ctx.beginPath();
          ctx.arc(0, 0, rRing, spin, spin + Math.PI * 1.4);
          ctx.strokeStyle = i === 0 ? "#38bdf8" : "#06b6d4";
          ctx.stroke();
        }
        // Center Ice Crystal
        ctx.fillStyle = "#ffffff";
        ctx.beginPath();
        ctx.arc(0, 0, 2.5, 0, Math.PI * 2);
        ctx.fill();
        break;
      }

      case "fan_chiller": {
        // VRT: 3-Blade cooling fan spinning continuously
        ctx.beginPath();
        ctx.arc(0, 0, rad * 0.75, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(6, 182, 212, 0.4)";
        ctx.lineWidth = 1;
        ctx.stroke();

        const fRot = t * 6;
        for (let b = 0; b < 3; b++) {
          const bAng = fRot + b * (Math.PI * 2 / 3);
          ctx.beginPath();
          ctx.moveTo(0, 0);
          ctx.quadraticCurveTo(Math.cos(bAng + 0.4) * rad * 0.5, Math.sin(bAng + 0.4) * rad * 0.5, Math.cos(bAng) * rad * 0.7, Math.sin(bAng) * rad * 0.7);
          ctx.strokeStyle = "#22d3ee";
          ctx.lineWidth = 2.5;
          ctx.stroke();
        }

        // Fan Hub
        ctx.beginPath();
        ctx.arc(0, 0, rad * 0.22, 0, Math.PI * 2);
        ctx.fillStyle = "#0891b2";
        ctx.fill();
        break;
      }

      case "fuel_cell": {
        // BE: Solid oxide fuel cell with high-voltage lightning arc
        ctx.fillStyle = "rgba(16, 185, 129, 0.2)";
        ctx.strokeStyle = "#10b981";
        ctx.lineWidth = 1;
        ctx.strokeRect(-rad * 0.6, -rad * 0.5, rad * 1.2, rad * 1.0);
        ctx.fillRect(-rad * 0.6, -rad * 0.5, rad * 1.2, rad * 1.0);

        // Electric lightning bolt
        ctx.beginPath();
        ctx.moveTo(-rad * 0.1, -rad * 0.4);
        ctx.lineTo(rad * 0.2, -rad * 0.05);
        ctx.lineTo(-rad * 0.05, 0);
        ctx.lineTo(rad * 0.15, rad * 0.4);
        ctx.strokeStyle = "#fbbf24";
        ctx.lineWidth = 2;
        ctx.shadowColor = "#fbbf24";
        ctx.shadowBlur = 8;
        ctx.stroke();
        ctx.shadowBlur = 0;
        break;
      }

      case "nuclear_atom": {
        // CEG: Atom nucleus with 3 orbiting electrons
        ctx.beginPath();
        ctx.arc(0, 0, rad * 0.2, 0, Math.PI * 2);
        ctx.fillStyle = "#ec4899";
        ctx.shadowColor = "#ec4899";
        ctx.shadowBlur = 8;
        ctx.fill();
        ctx.shadowBlur = 0;

        for (let e = 0; e < 3; e++) {
          const orbitTilt = e * (Math.PI / 3);
          ctx.save();
          ctx.rotate(orbitTilt);
          ctx.beginPath();
          ctx.ellipse(0, 0, rad * 0.7, rad * 0.25, 0, 0, Math.PI * 2);
          ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
          ctx.lineWidth = 0.9;
          ctx.stroke();

          // Electron dot
          const eAng = t * 3.5 + e * 2;
          ctx.beginPath();
          ctx.arc(Math.cos(eAng) * rad * 0.7, Math.sin(eAng) * rad * 0.25, 2.5, 0, Math.PI * 2);
          ctx.fillStyle = "#38bdf8";
          ctx.fill();
          ctx.restore();
        }
        break;
      }

      case "power_grid": {
        // VST: High voltage power transmission grid
        ctx.beginPath();
        ctx.moveTo(0, -rad * 0.65);
        ctx.lineTo(-rad * 0.45, rad * 0.5);
        ctx.lineTo(rad * 0.45, rad * 0.5);
        ctx.closePath();
        ctx.strokeStyle = "#eab308";
        ctx.lineWidth = 1.3;
        ctx.stroke();

        // Horizontal crossbars
        ctx.beginPath();
        ctx.moveTo(-rad * 0.55, -rad * 0.2); ctx.lineTo(rad * 0.55, -rad * 0.2);
        ctx.moveTo(-rad * 0.4, rad * 0.15); ctx.lineTo(rad * 0.4, rad * 0.15);
        ctx.stroke();

        // Spark pulse
        if (Math.sin(t * 8) > 0.4) {
          ctx.beginPath();
          ctx.arc(0, -rad * 0.65, 3, 0, Math.PI * 2);
          ctx.fillStyle = "#ffffff";
          ctx.shadowColor = "#eab308";
          ctx.shadowBlur = 8;
          ctx.fill();
          ctx.shadowBlur = 0;
        }
        break;
      }

      case "fast_reactor": {
        // OKLO: Radioactive warning trefoil with glowing emerald core
        const rRad = rad * 0.65;
        ctx.beginPath();
        ctx.arc(0, 0, rad * 0.25, 0, Math.PI * 2);
        ctx.fillStyle = "#10b981";
        ctx.shadowColor = "#10b981";
        ctx.shadowBlur = 8;
        ctx.fill();
        ctx.shadowBlur = 0;

        const pulseS = 0.75 + 0.25 * Math.sin(t * 4);
        for (let i = 0; i < 3; i++) {
          const startA = t * 1.5 + i * (Math.PI * 2 / 3);
          ctx.beginPath();
          ctx.arc(0, 0, rRad * pulseS, startA, startA + Math.PI / 3);
          ctx.strokeStyle = "#34d399";
          ctx.lineWidth = 2.5;
          ctx.stroke();
        }
        break;
      }

      case "cloud_server": {
        // NBIS: Vector cloud with blinking server chassis below
        // Cloud puffs
        ctx.fillStyle = "rgba(56, 189, 248, 0.4)";
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        ctx.arc(-rad * 0.25, -rad * 0.25, rad * 0.25, 0, Math.PI * 2);
        ctx.arc(rad * 0.15, -rad * 0.35, rad * 0.32, 0, Math.PI * 2);
        ctx.arc(rad * 0.38, -rad * 0.2, rad * 0.22, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        // Server rack blade
        ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
        ctx.strokeStyle = "#38bdf8";
        ctx.strokeRect(-rad * 0.45, rad * 0.05, rad * 0.9, rad * 0.32);
        ctx.fillRect(-rad * 0.45, rad * 0.05, rad * 0.9, rad * 0.32);

        // Blinking LEDs
        const led1 = Math.sin(t * 5) > 0;
        const led2 = Math.sin(t * 5 + 1.5) > 0;
        ctx.fillStyle = led1 ? "#10b981" : "#064e3b";
        ctx.fillRect(-rad * 0.3, rad * 0.15, 3, 3);
        ctx.fillStyle = led2 ? "#38bdf8" : "#0c4a6e";
        ctx.fillRect(-rad * 0.1, rad * 0.15, 3, 3);
        break;
      }

      case "gpu_cluster": {
        // CRWV: High density GPU blade stack with compute meters
        ctx.strokeStyle = "#0ea5e9";
        ctx.lineWidth = 1;
        ctx.strokeRect(-rad * 0.5, -rad * 0.55, rad * 1.0, rad * 1.1);

        for (let i = 0; i < 3; i++) {
          const sy = -rad * 0.4 + i * rad * 0.35;
          ctx.fillStyle = "rgba(14, 165, 233, 0.3)";
          ctx.fillRect(-rad * 0.4, sy, rad * 0.8, rad * 0.22);

          const barW = (0.3 + 0.6 * Math.sin(t * 4 + i)) * rad * 0.7;
          ctx.fillStyle = "#38bdf8";
          ctx.fillRect(-rad * 0.35, sy + 2, Math.max(2, barW), rad * 0.12);
        }
        break;
      }

      case "datacenter_campus": {
        // APLD: Data center buildings with rooftop beacon
        ctx.fillStyle = "rgba(100, 116, 139, 0.5)";
        ctx.strokeStyle = "#cbd5e1";
        ctx.lineWidth = 1;
        ctx.strokeRect(-rad * 0.55, -rad * 0.25, rad * 0.5, rad * 0.7);
        ctx.fillRect(-rad * 0.55, -rad * 0.25, rad * 0.5, rad * 0.7);

        ctx.strokeRect(0, -rad * 0.45, rad * 0.55, rad * 0.9);
        ctx.fillRect(0, -rad * 0.45, rad * 0.55, rad * 0.9);

        // Rooftop Beacon
        const beacon = Math.sin(t * 6) > 0.2;
        ctx.fillStyle = beacon ? "#ef4444" : "#450a0a";
        ctx.beginPath();
        ctx.arc(rad * 0.27, -rad * 0.55, 2.5, 0, Math.PI * 2);
        ctx.fill();
        break;
      }

      case "ai_graph": {
        // PLTR: Connected intelligence ontology spiderweb
        const pts = [
          [0, -rad * 0.5],
          [rad * 0.5, -rad * 0.15],
          [rad * 0.3, rad * 0.45],
          [-rad * 0.3, rad * 0.45],
          [-rad * 0.5, -rad * 0.15]
        ];
        ctx.strokeStyle = "rgba(56, 189, 248, 0.5)";
        ctx.lineWidth = 0.8;
        ctx.beginPath();
        pts.forEach((p, idx) => {
          if (idx === 0) ctx.moveTo(p[0], p[1]);
          else ctx.lineTo(p[0], p[1]);
          ctx.lineTo(0, 0);
          ctx.moveTo(p[0], p[1]);
        });
        ctx.closePath();
        ctx.stroke();

        // Pulsing active node
        const actIdx = Math.floor((t * 2) % 5);
        const actPt = pts[actIdx];
        ctx.beginPath();
        ctx.arc(actPt[0], actPt[1], 3, 0, Math.PI * 2);
        ctx.fillStyle = "#38bdf8";
        ctx.shadowColor = "#38bdf8";
        ctx.shadowBlur = 6;
        ctx.fill();
        ctx.shadowBlur = 0;
        break;
      }

      case "fintech_bank": {
        // SOFI: Digital bank coin token with ripple arcs
        ctx.beginPath();
        ctx.arc(0, 0, rad * 0.4, 0, Math.PI * 2);
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = "#38bdf8";
        ctx.font = "bold " + (rad * 0.4) + "px sans-serif";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText("$", 0, 0);

        // Transaction ripples
        const rWave = ((t * 1.5) % 1) * rad * 0.4 + rad * 0.4;
        ctx.beginPath();
        ctx.arc(0, 0, rWave, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(56, 189, 248, " + (1 - rWave / (rad * 0.8)) + ")";
        ctx.lineWidth = 1;
        ctx.stroke();
        break;
      }

      case "pharma_capsule": {
        // LLY: Medicine capsule with DNA spiral
        ctx.save();
        ctx.rotate(Math.PI / 4 + Math.sin(t * 2) * 0.15);
        // Top half
        ctx.fillStyle = "#ef4444";
        ctx.fillRect(-rad * 0.22, -rad * 0.5, rad * 0.44, rad * 0.45);
        // Bottom half
        ctx.fillStyle = "#ffffff";
        ctx.fillRect(-rad * 0.22, -rad * 0.05, rad * 0.44, rad * 0.45);
        ctx.strokeStyle = "#0f172a";
        ctx.strokeRect(-rad * 0.22, -rad * 0.5, rad * 0.44, rad * 0.9);
        ctx.restore();
        break;
      }

      case "enterprise_cloud": {
        // MSFT: 4-square cloud platform with orbit
        const s = rad * 0.32;
        const g = rad * 0.08;
        ctx.fillStyle = "#38bdf8";
        ctx.fillRect(-s - g, -s - g, s, s);
        ctx.fillStyle = "#10b981";
        ctx.fillRect(g, -s - g, s, s);
        ctx.fillStyle = "#f59e0b";
        ctx.fillRect(-s - g, g, s, s);
        ctx.fillStyle = "#ef4444";
        ctx.fillRect(g, g, s, s);
        break;
      }

      case "search_tpu": {
        // GOOGL: Radar search with tensor core
        ctx.beginPath();
        ctx.arc(0, 0, rad * 0.65, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(234, 179, 8, 0.4)";
        ctx.lineWidth = 1;
        ctx.stroke();

        const sAng = t * 3;
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(Math.cos(sAng) * rad * 0.65, Math.sin(sAng) * rad * 0.65);
        ctx.strokeStyle = "#eab308";
        ctx.lineWidth = 1.8;
        ctx.stroke();

        // TPU Core
        ctx.fillStyle = "#3b82f6";
        ctx.fillRect(-rad * 0.2, -rad * 0.2, rad * 0.4, rad * 0.4);
        break;
      }

      default: {
        // Fallback: Sector Icon
        ctx.font = "bold 16px sans-serif";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(n.simpleRole ? n.simpleRole.slice(0, 2) : "🏢", 0, 0);
      }
    }

    ctx.restore();
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
      const w = this.cssW;
      const h = this.cssH;
      const x = (mx - (w / 2 + this.panX)) / this.zoom + w / 2;
      const y = (my - (h / 2 + this.panY)) / this.zoom + h / 2;
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
        this.panX += (e.clientX - startPanX);
        this.panY += (e.clientY - startPanY);
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
#!/usr/bin/env python3
"""
MVVMC Chart Contract & 10/10 Validation Gate (Task 1: stock-chart-builder).
Prevents cross-ticker template leaks (e.g., BE text/prices inside an NBIS chart),
enforces required 9-Layer / 5-Layer structural zones, and runs macOS jsc syntax checks.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from typing import Iterable


JSC_PATH = "/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc"
MIN_TICKER_SHARD_BARS = 5

# Well-known prior template phrases/signatures that must never appear inside an unrelated ticker's chart.
FOREIGN_TICKER_SIGNATURES: dict[str, tuple[str, ...]] = {
    "BE": ("Bloom Energy", "solid oxide fuel cell", "scandium", "California Resources"),
    "NVDA": ("Jensen Huang", "Blackwell B200"),
    "SPCX": ("SpaceX", "Starlink", "Starship"),
    "SOFI": ("SoFi Technologies", "Galileo Technisys"),
    "AMKR": ("Amkor Technology", "CoWoS packaging"),
    "CRWV": ("CoreWeave",),
    "NBIS": ("Nebius", "Arkady Volozh", "neocloud", "GPU cluster"),
    "NVT": ("nVent Electric", "Beth Wozniak", "Maverick Power"),
}

# Unique price fingerprints belonging to specific stocks that must never leak into another ticker's chart
FOREIGN_PRICE_SIGNATURES: dict[str, tuple[str, ...]] = {
    "NBIS": ("80.67", "89.55", "90.40", "94.04", "73.52", "299.86", "85.15"),
    "BE": ("14.85", "18.30", "22.40"),
}


@dataclass(frozen=True)
class ChartDataContract:
    """Protocol-style data contract binding a generated HTML chart to one verified ticker."""

    symbol: str
    company_name: str
    is_broad_market: bool = False
    peer_symbols: tuple[str, ...] = ()
    banned_legacy_terms: tuple[str, ...] = ()
    banned_legacy_prices: tuple[str, ...] = ()


@dataclass
class ValidationResult:
    """Structured result emitted by ChartContractValidator."""

    passed: bool
    checks: list[tuple[str, bool, str]] = field(default_factory=list)
    jsc_passed: bool = False
    jsc_error: str = ""
    leaks_found: list[str] = field(default_factory=list)


class ChartContractValidator:
    """Validates chart HTML against Rule 2 & Task 1 Chart Builder contracts."""

    def __init__(self, contract: ChartDataContract) -> None:
        self.contract = contract

    def find_foreign_leaks(self, html: str) -> list[str]:
        """Detect residual foreign ticker names, industry strings, or banned prices."""
        leaks: list[str] = []
        allowed = {self.contract.symbol.upper(), *(p.upper() for p in self.contract.peer_symbols)}

        for other_sym, signatures in FOREIGN_TICKER_SIGNATURES.items():
            if other_sym.upper() in allowed:
                continue
            for phrase in signatures:
                if re.search(rf"\b{re.escape(phrase)}\b", html, flags=re.IGNORECASE):
                    leaks.append(f"Foreign signature for {other_sym}: '{phrase}'")

        # Automatically check for foreign price fingerprints belonging to other stocks
        for other_sym, prices in FOREIGN_PRICE_SIGNATURES.items():
            if other_sym.upper() in allowed:
                continue
            for price in prices:
                if re.search(rf"(?<![\d.]){re.escape(price)}(?![\d.])", html):
                    leaks.append(f"Foreign price fingerprint for {other_sym}: '${price}'")

        for term in self.contract.banned_legacy_terms:
            if re.search(rf"\b{re.escape(term)}\b", html):
                leaks.append(f"Banned legacy term: '{term}'")

        for price in self.contract.banned_legacy_prices:
            if re.search(rf"(?<![\d.]){re.escape(price)}(?![\d.])", html):
                leaks.append(f"Banned legacy price: '{price}'")

        # Range Anomaly Gate: verify right-axis pills do not contain wildly out-of-range prices
        spot_match = re.search(r"var\s+SPOT\s*=\s*([0-9.]+);", html)
        if spot_match:
            spot = float(spot_match.group(1))
            # Scan pills text pattern: text:\s*"(\$?[0-9.]+)
            pill_prices = re.findall(r'text:\s*"\$?([0-9.]+)', html)
            for p_str in pill_prices:
                p_val = float(p_str)
                if p_val < 0.40 * spot or p_val > 2.80 * spot:
                    leaks.append(f"Price anomaly in pill: '${p_str}' deviates dangerously from SPOT ${spot}")

        return leaks

    def run_jsc_syntax_check(self, html: str) -> tuple[bool, str]:
        """Extract inline <script> blocks and validate JS syntax with macOS JavaScriptCore."""
        if not os.path.exists(JSC_PATH):
            return False, f"jsc binary not found at {JSC_PATH}"

        scripts = [
            s for s in re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, flags=re.DOTALL)
            if s.strip()
        ]
        if not scripts:
            return False, "No inline <script> block found to validate"

        mock_dom = (
            "var window={devicePixelRatio:1,addEventListener:function(){}};"
            "var document={body:{classList:{toggle:function(){},contains:function(){return true;}}},"
            "getElementById:function(){return{getContext:function(){return{scale:function(){},fillRect:function(){},"
            "strokeRect:function(){},beginPath:function(){},moveTo:function(){},lineTo:function(){},stroke:function(){},"
            "fill:function(){},closePath:function(){},arc:function(){},setLineDash:function(){},fillText:function(){},"
            "measureText:function(){return{width:50};}};},getBoundingClientRect:function(){return{width:800,height:400};},"
            "addEventListener:function(){},classList:{add:function(){},remove:function(){},toggle:function(){}},style:{},textContent:'',value:'0'};},"
            "querySelectorAll:function(){return[];}};"
        )

        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as tmp:
            tmp.write(mock_dom + "\n" + "\n".join(scripts))
            tmp_path = tmp.name

        try:
            proc = subprocess.run([JSC_PATH, tmp_path], capture_output=True, text=True, timeout=10)
            if proc.returncode != 0:
                return False, (proc.stderr or proc.stdout).strip()
            return True, ""
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def validate_html(self, html: str) -> ValidationResult:
        """Execute streamlined automated structural checks + leak scan + jsc syntax test."""
        sym = self.contract.symbol
        leaks = self.find_foreign_leaks(html)
        jsc_ok, jsc_err = self.run_jsc_syntax_check(html)

        checks: list[tuple[str, bool, str]] = [
            (
                "0. Zero foreign ticker leaks & static hygiene (no :root override, allowlisted Tailwind)",
                len(leaks) == 0
                and ":root" not in html
                and "tailwindcss.min.js" in html,
                "; ".join(leaks) if leaks else "Clean isolation",
            ),
            (
                "1. Header Bar: 4-Timeframe Switcher + Target Ticker Symbol",
                sym in html and all(x in html for x in ('data-tf="TODAY"', 'data-tf="2D"', 'data-tf="1D"', 'data-tf="1W"')),
                f"Ticker {sym} & 4 TF buttons present",
            ),
            (
                "2. Contextual Controls & Synchronized Coach Strip",
                all(x in html for x in ('id="ctrlStrip"', 'id="coachStrip"')),
                "#ctrlStrip & #coachStrip wired",
            ),
            (
                "3. 3 Interactive Views (Canvas + 4-Step Graph + 4-Step Explanation)",
                all(x in html for x in ('id="viewA"', 'id="viewB"', 'id="viewC"', 'id="mainCanvas"', 'id="storyCanvas"')),
                "All 3 interactive views wired (#viewA, #viewB, #viewC)",
            ),
            (
                "4. Direct Pill-Hover Guidance Engine & S1/S2/S3 / L2 Bid Floors",
                all(x in html for x in ("actionHeader", "actionTake", "lastRenderedPills", "hoveredPillIdx"))
                and (
                    self.contract.is_broad_market
                    or (all(x in html for x in ("S1", "S2", "S3")) and any(b in html for b in ("BID FLOOR", "L2 BID", "Bid Floor")))
                ),
                "Pill-hover callouts + dynamic action bindings + S1/S2/S3 & L2 Bid Floors wired",
            ),
            (
                "5. Corporate Events, Risk Ticket, Competitor Matrix / Broad Market Overlays",
                (
                    all(x in html for x in ("Breadth", "Credit", "VIX", "Rotation"))
                    if self.contract.is_broad_market
                    else all(x in html for x in ("Corporate Events", "Layer 9"))
                ),
                "Layer 7-9 / Broad Market macro overlays present",
            ),
            (
                "6. Kid-Level 30-Second Summary & Masked Account ••••3782 Footer",
                "••••3782" in html and "Simple Kid-Level Summary" in html,
                "Privacy mask ••••3782 + Kid summary present",
            ),
            (
                "7. Live Array Parity (TODAY_BARS / TWO_DAY_BARS / DAILY_BARS / WEEKLY_BARS) & jsc Check",
                jsc_ok
                and all(x in html for x in ("TODAY_BARS", "TWO_DAY_BARS", "DAILY_BARS", "WEEKLY_BARS", "HORIZONS")),
                jsc_err if not jsc_ok else "jsc exit 0 & all bar arrays defined",
            ),
        ]

        all_ok = all(ok for _, ok, _ in checks)
        return ValidationResult(passed=all_ok, checks=checks, jsc_passed=jsc_ok, jsc_error=jsc_err, leaks_found=leaks)


def main(argv: Iterable[str]) -> int:
    """CLI entry point: python3 validate_chart_contract.py <chart.html> <SYMBOL> [--market] [--peers P1,P2]"""
    args = list(argv)
    if len(args) < 3:
        print("Usage: validate_chart_contract.py <chart.html> <SYMBOL> [--market] [--peers A,B] [--banned-terms X,Y] [--banned-prices P1,P2]")
        return 2

    html_path, symbol = args[1], args[2].upper()
    is_market = "--market" in args
    peers: tuple[str, ...] = ()
    banned_terms: tuple[str, ...] = ()
    banned_prices: tuple[str, ...] = ()

    for i, tok in enumerate(args[3:], start=3):
        if tok == "--peers" and i + 1 < len(args):
            peers = tuple(p.strip().upper() for p in args[i + 1].split(",") if p.strip())
        elif tok == "--banned-terms" and i + 1 < len(args):
            banned_terms = tuple(t.strip() for t in args[i + 1].split(",") if t.strip())
        elif tok == "--banned-prices" and i + 1 < len(args):
            banned_prices = tuple(p.strip() for p in args[i + 1].split(",") if p.strip())

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    contract = ChartDataContract(
        symbol=symbol,
        company_name=symbol,
        is_broad_market=is_market,
        peer_symbols=peers,
        banned_legacy_terms=banned_terms,
        banned_legacy_prices=banned_prices,
    )
    res = ChartContractValidator(contract).validate_html(html)

    print(f"=== TASK 1 CHART CONTRACT VALIDATION: {symbol} ({os.path.basename(html_path)}) ===")
    for name, ok, detail in res.checks:
        print(f"  {'✅ PASS' if ok else '❌ FAIL'} - {name} [{detail}]")
    print(f"  {'✅ PASS' if res.jsc_passed else '❌ FAIL'} - macOS jsc syntax check")
    return 0 if res.passed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

/**
 * GrowthScannerViewModel
 * Implements GrowthScannerViewModelProtocol
 * Calculates momentum scores, growth filtering, and leaderboard rankings.
 */
class GrowthScannerViewModel {
  constructor(stockRepository, eventBus) {
    this.repo = stockRepository;
    this.eventBus = eventBus;
    this.stocks = [];
    this.activeFilter = 'ALL'; // 'ALL', 'AI_INFRA', 'POWER', 'COOLING', 'DEFENSE', 'BIOTECH'
    this.searchQuery = '';
    this.sortField = 'growthYoY';
    this.sortAsc = false;
  }

  async loadData() {
    this.stocks = await this.repo.getAllStocks();
    this._computeMomentumScores();
    return this.getFilteredStocks();
  }

  _computeMomentumScores() {
    this.stocks.forEach(s => {
      // Composite momentum score (0-100)
      // RVOL weight (30%), 1M return (25%), 1Y growth (25%), 1D return (20%)
      const rvolScore = Math.min(30, (s.rvol / 2.5) * 30);
      const m1Score = Math.max(0, Math.min(25, ((s.change1M + 20) / 60) * 25));
      const gScore = Math.min(25, (s.growthYoY / 80) * 25);
      const d1Score = Math.max(0, Math.min(20, ((s.change1D + 5) / 15) * 20));
      s.momentumScore = Math.round(rvolScore + m1Score + gScore + d1Score);
    });
  }

  setFilter(filter) {
    this.activeFilter = filter;
    this.eventBus.publish('scanner:filterChanged', this.getFilteredStocks());
  }

  setSearch(query) {
    this.searchQuery = (query || '').trim().toLowerCase();
    this.eventBus.publish('scanner:searchChanged', this.getFilteredStocks());
  }

  setSort(field) {
    if (this.sortField === field) {
      this.sortAsc = !this.sortAsc;
    } else {
      this.sortField = field;
      this.sortAsc = false;
    }
    this.eventBus.publish('scanner:sortChanged', this.getFilteredStocks());
  }

  getFilteredStocks() {
    let result = [...this.stocks];

    if (this.activeFilter !== 'ALL') {
      result = result.filter(s => {
        if (this.activeFilter === 'AI_INFRA') return s.layer.includes('AI') || s.sector === 'Semiconductors';
        if (this.activeFilter === 'POWER') return s.sector.includes('Energy');
        if (this.activeFilter === 'COOLING') return s.sector.includes('Thermal');
        if (this.activeFilter === 'DEFENSE') return s.sector.includes('Defense');
        if (this.activeFilter === 'BIOTECH') return s.sector.includes('Healthcare');
        if (this.activeFilter === 'FINTECH') return s.sector.includes('Fintech');
        return true;
      });
    }

    if (this.searchQuery) {
      result = result.filter(s =>
        s.symbol.toLowerCase().includes(this.searchQuery) ||
        s.name.toLowerCase().includes(this.searchQuery) ||
        s.layer.toLowerCase().includes(this.searchQuery) ||
        s.growthDriver.toLowerCase().includes(this.searchQuery)
      );
    }

    result.sort((a, b) => {
      let va = a[this.sortField];
      let vb = b[this.sortField];
      if (va < vb) return this.sortAsc ? -1 : 1;
      if (va > vb) return this.sortAsc ? 1 : -1;
      return 0;
    });

    return result;
  }
}

if (typeof module !== 'undefined') {
  module.exports = { GrowthScannerViewModel };
}

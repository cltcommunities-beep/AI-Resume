/**
 * StockDetailViewModel
 * Implements StockDetailViewModelProtocol
 * Provides deep forensic due diligence: 3-link dependencies, why growing, and who benefits next.
 */
class StockDetailViewModel {
  constructor(stockRepository, eventBus) {
    this.repo = stockRepository;
    this.eventBus = eventBus;
    this.activeStock = null;
  }

  async selectStock(symbol) {
    try {
      this.activeStock = await this.repo.getStock(symbol);
      this.eventBus.publish('detail:stockLoaded', this.activeStock);
      return this.activeStock;
    } catch (err) {
      console.error('[StockDetailViewModel] Error loading stock:', err);
      return null;
    }
  }

  closeDetail() {
    this.activeStock = null;
    this.eventBus.publish('detail:closed', null);
  }
}

if (typeof module !== 'undefined') {
  module.exports = { StockDetailViewModel };
}

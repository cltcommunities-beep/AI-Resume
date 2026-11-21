/**
 * StockNetworkViewModel
 * Implements StockNetworkViewModelProtocol
 * Manages graph topology, cluster filtering, and ripple shock simulation.
 */
class StockNetworkViewModel {
  constructor(stockRepository, eventBus) {
    this.repo = stockRepository;
    this.eventBus = eventBus;
    this.graphData = { nodes: [], links: [] };
    this.selectedNode = null;
    this.activeShock = null;
  }

  async loadGraph() {
    this.graphData = await this.repo.getEcosystemGraph();
    return this.graphData;
  }

  selectNode(symbol) {
    this.selectedNode = symbol;
    this.eventBus.publish('network:nodeSelected', symbol);
  }

  async triggerShock(symbol, percent) {
    this.activeShock = await this.repo.simulateShock(symbol, percent);
    this.eventBus.publish('network:shockSimulated', this.activeShock);
    return this.activeShock;
  }

  clearShock() {
    this.activeShock = null;
    this.eventBus.publish('network:shockCleared', null);
  }
}

if (typeof module !== 'undefined') {
  module.exports = { StockNetworkViewModel };
}

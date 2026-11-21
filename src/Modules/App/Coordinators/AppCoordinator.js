/**
 * AppCoordinator (MVVM-C Master Router)
 * Orchestrates navigation, state synchronization, and inter-module event routing.
 */
class AppCoordinator {
  constructor(container) {
    this.container = container;
    this.eventBus = container.resolve(Symbol.for('EventBusProtocol') || ServiceTokens.EventBus);
    this.scannerVM = null;
    this.networkVM = null;
    this.detailVM = null;
    this.activeTab = 'NETWORK'; // 'NETWORK' or 'SCANNER' or 'SIMULATOR'
  }

  start(scannerVM, networkVM, detailVM) {
    this.scannerVM = scannerVM;
    this.networkVM = networkVM;
    this.detailVM = detailVM;

    // Cross-module subscriptions
    this.eventBus.subscribe('network:nodeSelected', (symbol) => {
      this.detailVM.selectStock(symbol);
    });

    this.eventBus.subscribe('scanner:stockSelected', (symbol) => {
      this.detailVM.selectStock(symbol);
      this.networkVM.selectNode(symbol);
    });
  }

  switchTab(tab) {
    this.activeTab = tab;
    this.eventBus.publish('app:tabSwitched', tab);
  }

  inspectStock(symbol) {
    this.detailVM.selectStock(symbol);
  }

  simulateRipple(symbol, percent) {
    this.networkVM.triggerShock(symbol, percent);
  }
}

if (typeof module !== 'undefined') {
  module.exports = { AppCoordinator };
}

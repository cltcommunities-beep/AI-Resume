/**
 * ServiceContainer (Dependency Injection Container)
 * Implements ServiceContainerProtocol
 * In accordance with Rule 4: Protocol-based contracts & Dependency Injection.
 */
class ServiceContainer {
  constructor() {
    this._factories = new Map();
    this._instances = new Map();
  }

  register(token, factory, isSingleton = true) {
    this._factories.set(token, { factory, isSingleton });
  }

  resolve(token) {
    if (this._instances.has(token)) {
      return this._instances.get(token);
    }
    const registration = this._factories.get(token);
    if (!registration) {
      throw new Error(`[ServiceContainer] No registration found for token: ${String(token)}`);
    }
    const instance = registration.factory(this);
    if (registration.isSingleton) {
      this._instances.set(token, instance);
    }
    return instance;
  }
}

// Global Symbols / Protocol Tokens
const ServiceTokens = {
  NetworkService: Symbol('NetworkServiceProtocol'),
  StockRepository: Symbol('StockRepositoryProtocol'),
  EventBus: Symbol('EventBusProtocol'),
  AppCoordinator: Symbol('AppCoordinatorProtocol')
};

if (typeof module !== 'undefined') {
  module.exports = { ServiceContainer, ServiceTokens };
}

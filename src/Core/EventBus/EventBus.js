/**
 * EventBus (Decoupled Messaging Engine)
 * Implements EventBusProtocol
 */
class EventBus {
  constructor() {
    this._listeners = new Map();
  }

  subscribe(event, callback) {
    if (!this._listeners.has(event)) {
      this._listeners.set(event, new Set());
    }
    this._listeners.get(event).add(callback);
    return () => this.unsubscribe(event, callback);
  }

  unsubscribe(event, callback) {
    if (this._listeners.has(event)) {
      this._listeners.get(event).delete(callback);
    }
  }

  publish(event, payload) {
    if (this._listeners.has(event)) {
      this._listeners.get(event).forEach(cb => {
        try { cb(payload); } catch (e) { console.error(`[EventBus] Error in handler for ${event}:`, e); }
      });
    }
  }
}

if (typeof module !== 'undefined') {
  module.exports = { EventBus };
}

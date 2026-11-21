/**
 * NetworkService (Async/Await Network Layer with Memory Caching)
 * Implements NetworkServiceProtocol per Rule 6
 */
class NetworkService {
  constructor(cacheTTLMs = 60000) {
    this._cache = new Map();
    this._cacheTTL = cacheTTLMs;
  }

  async fetch(request) {
    const key = `${request.method || 'GET'}:${request.endpoint}:${JSON.stringify(request.params || {})}`;
    const now = Date.now();

    if (request.cachePolicy !== 'networkOnly' && this._cache.has(key)) {
      const entry = this._cache.get(key);
      if (now - entry.timestamp < this._cacheTTL) {
        return entry.data;
      }
    }

    try {
      // Standardized async/await mock/fetch pipeline
      let data;
      if (request.mockHandler) {
        data = await request.mockHandler(request.params);
      } else {
        const url = new URL(request.endpoint, window.location ? window.location.origin : 'http://localhost');
        if (request.params) {
          Object.entries(request.params).forEach(([k, v]) => url.searchParams.append(k, v));
        }
        const resp = await fetch(url.toString(), {
          method: request.method || 'GET',
          headers: request.headers || { 'Content-Type': 'application/json' }
        });
        if (!resp.ok) throw new Error(`HTTP Error ${resp.status}: ${resp.statusText}`);
        data = await resp.json();
      }

      this._cache.set(key, { data, timestamp: now });
      return data;
    } catch (err) {
      console.error(`[NetworkService] Fetch error on ${request.endpoint}:`, err);
      throw err;
    }
  }

  clearCache() {
    this._cache.clear();
  }
}

if (typeof module !== 'undefined') {
  module.exports = { NetworkService };
}

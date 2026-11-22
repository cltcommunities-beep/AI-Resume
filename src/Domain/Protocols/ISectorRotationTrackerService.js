/**
 * @protocol ISectorRotationTrackerService
 * Protocol contract defining sector rotation capital flow tracking.
 */
class ISectorRotationTrackerService {
  /**
   * @param {'1D' | '1W' | '1M'} timeframe
   * @returns {Promise<Array<SectorMomentumMetric>>}
   */
  async getSectorMetrics(timeframe) {
    throw new Error('ISectorRotationTrackerService.getSectorMetrics must be implemented');
  }

  /**
   * @returns {Promise<RotationCycleState>}
   */
  async getRotationCycleState() {
    throw new Error('ISectorRotationTrackerService.getRotationCycleState must be implemented');
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { ISectorRotationTrackerService };
}

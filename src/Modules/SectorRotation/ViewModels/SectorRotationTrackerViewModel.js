/**
 * @class SectorRotationTrackerViewModel
 * ViewModel orchestrating sector rotation tracking, timeframe switching, and event bus broadcasts.
 */
class SectorRotationTrackerViewModel {
  constructor(trackerService, eventBus) {
    this.trackerService = trackerService;
    this.eventBus = eventBus;
    this.timeframe = '1D'; // '1D' | '1W' | '1M'
    this.metrics = [];
    this.cycleState = null;
    this.selectedSectorId = null;
  }

  async loadTracker() {
    this.metrics = await this.trackerService.getSectorMetrics(this.timeframe);
    this.cycleState = await this.trackerService.getRotationCycleState();
    
    this.eventBus.publish('tracker:dataLoaded', {
      timeframe: this.timeframe,
      metrics: this.metrics,
      cycleState: this.cycleState,
      selectedSectorId: this.selectedSectorId
    });

    return { metrics: this.metrics, cycleState: this.cycleState };
  }

  async setTimeframe(tf) {
    if (this.timeframe === tf) return;
    this.timeframe = tf;
    this.metrics = await this.trackerService.getSectorMetrics(this.timeframe);

    this.eventBus.publish('tracker:timeframeChanged', {
      timeframe: this.timeframe,
      metrics: this.metrics
    });

    return this.metrics;
  }

  selectSector(sectorId) {
    this.selectedSectorId = (this.selectedSectorId === sectorId) ? null : sectorId;
    this.eventBus.publish('tracker:sectorSelected', this.selectedSectorId);
    return this.selectedSectorId;
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { SectorRotationTrackerViewModel };
}

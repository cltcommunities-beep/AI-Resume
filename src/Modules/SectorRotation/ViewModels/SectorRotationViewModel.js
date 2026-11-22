/**
 * SectorRotationViewModel
 * Implements ISectorRotationViewModel
 * Manages institutional sector rotation data, capital flow state, and sector filter highlighting.
 */
class SectorRotationViewModel {
  constructor(stockRepository, eventBus) {
    this.repo = stockRepository;
    this.eventBus = eventBus;
    this.rotations = [];
    this.selectedSector = null;
  }

  async loadRotations() {
    this.rotations = await this.repo.getSectorRotations();
    this.eventBus.publish("rotation:dataLoaded", this.rotations);
    return this.rotations;
  }

  selectSector(sectorId) {
    this.selectedSector = (this.selectedSector === sectorId) ? null : sectorId;
    this.eventBus.publish("rotation:sectorSelected", this.selectedSector);
  }

  selectStock(symbol) {
    this.eventBus.publish("rotation:stockSelected", symbol);
  }
}

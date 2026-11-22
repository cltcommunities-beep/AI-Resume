/**
 * @class SectorRotationTrackerService
 * Implements ISectorRotationTrackerService to calculate live sector capital velocity,
 * momentum leadership states (Leading, Weakening, Lagging, Improving), and macro cycle stages.
 */
class SectorRotationTrackerService {
  constructor(stockRepository) {
    this.repo = stockRepository;
  }

  async getSectorMetrics(timeframe = '1D') {
    const sectors = await this.repo.getSectorRotations();
    
    return sectors.map(sec => {
      // Calculate weighted averages based on component stocks
      const count = sec.stocks.length || 1;
      const sum1D = sec.stocks.reduce((acc, s) => acc + (s.change1D || 0), 0);
      const avg1D = Number((sum1D / count).toFixed(1));
      
      const sum1M = sec.stocks.reduce((acc, s) => acc + (s.change1M || 0), 0);
      const avg1M = Number((sum1M / count).toFixed(1));

      // Approximated 1W momentum based on 1M/1D trajectory
      const avg1W = Number((avg1D * 2.2 + avg1M * 0.25).toFixed(1));

      // Determine active metric based on selected timeframe
      let activeMomentum = avg1D;
      if (timeframe === '1W') activeMomentum = avg1W;
      if (timeframe === '1M') activeMomentum = avg1M;

      // Classify 4-Quadrant Leadership State
      let flowState = 'IMPROVING';
      let stateBadge = '🔄 Improving';
      let stateColor = '#38bdf8';
      let stateBg = 'rgba(14, 165, 233, 0.15)';

      if (avg1M >= 15 && avg1D >= 3) {
        flowState = 'LEADING';
        stateBadge = '🚀 Leading Inflow';
        stateColor = '#34d399';
        stateBg = 'rgba(16, 185, 129, 0.15)';
      } else if (avg1M >= 10 && avg1D < 0) {
        flowState = 'WEAKENING';
        stateBadge = '⚠️ Weakening / Peak';
        stateColor = '#fbbf24';
        stateBg = 'rgba(245, 158, 11, 0.15)';
      } else if (avg1M < 5 && avg1D < 0) {
        flowState = 'LAGGING';
        stateBadge = '🛑 Lagging / Outflow';
        stateColor = '#f87171';
        stateBg = 'rgba(239, 68, 68, 0.15)';
      } else {
        flowState = 'IMPROVING';
        stateBadge = '🔄 Early Inflection';
        stateColor = '#60a5fa';
        stateBg = 'rgba(59, 130, 246, 0.15)';
      }

      // Best performing stock in this sector
      const sortedStocks = [...sec.stocks].sort((a, b) => b.change1D - a.change1D);
      const leadStock = sortedStocks[0] || { symbol: 'N/A', change1D: 0 };

      // Normalised Momentum Score (0 to 100 for visual bar)
      const clampedScore = Math.max(5, Math.min(100, Math.round(50 + activeMomentum * 2.5)));

      return {
        id: sec.id,
        name: sec.name,
        emoji: sec.emoji,
        flowState,
        stateBadge,
        stateColor,
        stateBg,
        flowTag: sec.flowTag,
        kidReason: sec.kidReason,
        macroDriver: sec.macroDriver,
        momentum1D: avg1D,
        momentum1W: avg1W,
        momentum1M: avg1M,
        activeMomentum,
        inflowScore: clampedScore,
        leadStock: leadStock.symbol,
        leadStockChange: leadStock.change1D,
        stocks: sec.stocks
      };
    }).sort((a, b) => b.activeMomentum - a.activeMomentum);
  }

  async getRotationCycleState() {
    return {
      activeStage: 3,
      totalStages: 4,
      stageTitle: '⚡ Energy & Baseload Power Bottleneck',
      stageSubtitle: 'Wall Street capital rotating into power infrastructure & cooling',
      priorStage: '🧠 Stage 2: Hardware Compute & Chip Buildout (Consolidating)',
      currentFocus: '⚡ Stage 3: Instant Power & Cooling Deployment (Active Surge)',
      nextProjectedStage: '☁️ Stage 4: Enterprise Cloud & Mobile Cash Fortresses (Preparing)',
      stages: [
        { num: 1, name: 'Silicon Chips', status: 'Completed', color: '#64748b' },
        { num: 2, name: 'Cooling Racks', status: 'Peaking', color: '#38bdf8' },
        { num: 3, name: 'Power & Grid', status: 'CURRENT LEADER', color: '#fbbf24' },
        { num: 4, name: 'Cloud & Cash', status: 'Next In Line', color: '#34d399' }
      ]
    };
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { SectorRotationTrackerService };
}

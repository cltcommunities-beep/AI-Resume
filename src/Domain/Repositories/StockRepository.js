/**
 * StockRepository
 * Authoritative Domain Data Engine & Ecosystem Knowledge Graph
 * Covers 20 complete stocks with Plain-English Business Stories, 2-Way Relationships, and Domino Scenarios.
 */
class StockRepository {
  constructor(networkService, eventBus) {
    this.network = networkService;
    this.eventBus = eventBus;
    this._stocks = [
  {
    "symbol": "NVDA",
    "name": "NVIDIA Corporation",
    "simpleRole": "\ud83e\udde0 The AI Brain Designer",
    "sector": "Semiconductors",
    "layer": "AI Compute Silicon",
    "price": 125.79,
    "change1D": -13.8,
    "change1M": -21.4,
    "growthYoY": 103.0,
    "rvol": 2.15,
    "marketCapB": 3094.0,
    "peRatio": 38.5,
    "whatItDoes": "NVIDIA designs the world's most powerful specialized computer chips (GPUs) that act as the 'super-brains' behind modern artificial intelligence like ChatGPT, self-driving cars, and robotics.",
    "whyNeeded": "Standard computer processors (CPUs) can only do one calculation at a time. NVIDIA chips can perform millions of complex mathematical calculations at the exact same fraction of a second, which is the only way AI models can learn and generate answers.",
    "whatItSells": "Blackwell & Hopper AI microchips, HGX server motherboards, high-speed networking cables (Quantum InfiniBand), and CUDA AI software that developers code on.",
    "whoBuys": "Giant cloud companies (Microsoft, Amazon, Google, Meta), AI startups (OpenAI, Anthropic), and specialized cloud hosts (CoreWeave, Nebius).",
    "growthDrivers": "Every company in the world wants AI; tech giants are spending hundreds of billions of dollars constructing giant data center supercomputers.",
    "businessRisks": "Export restrictions on selling to China, potential customer chip spending slowdowns, or customers building their own internal chips.",
    "storySteps": [
      {
        "icon": "\ud83e\uddd1\u200d\ud83d\udcbb",
        "title": "AI Engineers Need Compute",
        "desc": "Developers write complex AI models that require billions of simultaneous calculations."
      },
      {
        "icon": "\ud83d\udfe2",
        "title": "NVIDIA Designs the Super-Chips",
        "desc": "NVIDIA architects the Blackwell architecture and CUDA software library."
      },
      {
        "icon": "\ud83c\udfed",
        "title": "TSMC Manufactures the Silicon",
        "desc": "TSMC prints the microscopic 3-nanometer circuits on silicon wafers in Taiwan."
      },
      {
        "icon": "\ud83d\udcbe",
        "title": "Memory Companies Add HBM",
        "desc": "Micron & SK Hynix attach ultra-fast memory stacks to feed data into the chip."
      },
      {
        "icon": "\u2744\ufe0f",
        "title": "Liquid Cooling Keeps It From Melting",
        "desc": "Vertiv & nVent pump chilled liquid directly onto the chip to remove 120kW of heat."
      },
      {
        "icon": "\u26a1",
        "title": "Energy Plants Supply 24/7 Power",
        "desc": "Bloom Energy & Constellation supply continuous, uninterrupted electricity."
      },
      {
        "icon": "\u2601\ufe0f",
        "title": "Cloud Providers Rent It to Users",
        "desc": "Microsoft Azure & Nebius host the servers so you can use AI apps on your phone."
      }
    ],
    "upstream": [
      "TSM",
      "AMKR"
    ],
    "downstream": [
      "MSFT",
      "META",
      "GOOGL",
      "AMZN",
      "NBIS",
      "CRWV"
    ],
    "competitors": [
      "AMD",
      "AVGO"
    ]
  },
  {
    "symbol": "AMD",
    "name": "Advanced Micro Devices",
    "simpleRole": "\u26a1 The High-Speed Challenger",
    "sector": "Semiconductors",
    "layer": "AI Compute Silicon",
    "price": 138.25,
    "change1D": -3.2,
    "change1M": -8.5,
    "growthYoY": 18.0,
    "rvol": 1.35,
    "marketCapB": 223.5,
    "peRatio": 45.2,
    "whatItDoes": "AMD creates high-performance computer processors and AI accelerator chips (MI300 series) that directly compete with Intel in PCs/servers and NVIDIA in AI computing.",
    "whyNeeded": "Tech giants do not want to be trapped buying exclusively from NVIDIA at premium prices. AMD gives hyperscalers a reliable, high-speed alternative.",
    "whatItSells": "Instinct MI300X/MI325X AI graphics chips, EPYC server CPUs, and Ryzen personal computer processors.",
    "whoBuys": "Microsoft Azure, Oracle Cloud, Meta, and major server builders like Dell and HPE.",
    "growthDrivers": "Cloud providers diversifying away from NVIDIA to save money and secure compute supply.",
    "businessRisks": "NVIDIA's massive software moat (CUDA) makes it difficult for programmers to switch their code to AMD's ROCm software.",
    "storySteps": [
      {
        "icon": "\ud83c\udfe2",
        "title": "Hyperscalers Want Cost Relief",
        "desc": "Cloud giants need a second supplier to avoid paying monopoly prices for GPUs."
      },
      {
        "icon": "\ud83d\udd34",
        "title": "AMD Engineers MI300X",
        "desc": "AMD designs an AI chip with massive memory capacity to handle large AI models."
      },
      {
        "icon": "\ud83c\udfed",
        "title": "TSMC Prints the Circuits",
        "desc": "Uses TSMC's advanced 5nm & 6nm nodes with 3D chiplet stacking."
      },
      {
        "icon": "\ud83d\udda5\ufe0f",
        "title": "Deployed in Oracle & Azure",
        "desc": "Cloud providers deploy AMD clusters for customers running inference AI workloads."
      }
    ],
    "upstream": [
      "TSM",
      "AMKR"
    ],
    "downstream": [
      "MSFT",
      "GOOGL",
      "META"
    ],
    "competitors": [
      "NVDA"
    ]
  },
  {
    "symbol": "AVGO",
    "name": "Broadcom Inc.",
    "simpleRole": "\ud83d\udd0c The Custom Chip & Highway Builder",
    "sector": "Semiconductors",
    "layer": "Custom AI ASICs & Networking",
    "price": 164.8,
    "change1D": -2.1,
    "change1M": 12.4,
    "growthYoY": 47.0,
    "rvol": 1.42,
    "marketCapB": 768.4,
    "peRatio": 34.2,
    "whatItDoes": "Broadcom co-designs custom microchips for tech giants (like Google's TPU) and manufactures high-speed networking switches that connect tens of thousands of AI chips together.",
    "whyNeeded": "When 100,000 AI chips work on one big problem, the bottleneck is transferring data between them without traffic jams. Broadcom builds the 'superhighways'.",
    "whatItSells": "Tomahawk & Jericho high-speed Ethernet switch chips, optical components, and custom AI ASIC processor designs.",
    "whoBuys": "Google (for all its TPU AI chips), Meta (for MTIA chips), Apple, and enterprise cloud data centers.",
    "growthDrivers": "Hyperscalers building their own custom silicon to replace expensive commercial GPUs, and networking speeds doubling from 400G to 800G and 1.6T.",
    "businessRisks": "Heavy revenue concentration in a handful of giant customers (Google, Apple, Meta).",
    "storySteps": [
      {
        "icon": "\ud83c\udf10",
        "title": "Google Wants Custom Chips",
        "desc": "Google decides to build its own AI processor (TPU) instead of buying only from outside vendors."
      },
      {
        "icon": "\ud83e\udd1d",
        "title": "Broadcom Co-Designs the Silicon",
        "desc": "Broadcom provides proprietary chip design blocks and high-speed data pathways."
      },
      {
        "icon": "\ud83d\udea6",
        "title": "Switching Data Traffic",
        "desc": "Broadcom's Tomahawk switches direct multi-terabit data packets between servers."
      },
      {
        "icon": "\ud83d\udcf1",
        "title": "Powers Google Gemini",
        "desc": "Google trains and serves Gemini AI models using the Broadcom-designed TPU network."
      }
    ],
    "upstream": [
      "TSM",
      "AMKR"
    ],
    "downstream": [
      "GOOGL",
      "META",
      "MSFT",
      "AAPL"
    ],
    "competitors": [
      "MRVL",
      "NVDA"
    ]
  },
  {
    "symbol": "MRVL",
    "name": "Marvell Technology",
    "simpleRole": "\ud83d\udca1 The Light-Speed Data Transporter",
    "sector": "Semiconductors",
    "layer": "Custom AI ASICs & Optics",
    "price": 88.5,
    "change1D": 1.8,
    "change1M": 21.0,
    "growthYoY": 34.0,
    "rvol": 1.55,
    "marketCapB": 76.5,
    "peRatio": 48.0,
    "whatItDoes": "Marvell creates optical chips (electro-optics) that turn electrical signals into light pulses, transmitting data through fiber-optic cables inside data centers at nearly the speed of light.",
    "whyNeeded": "Traditional copper wires get too hot and lose signal quality over distances longer than a few meters. Marvell's optical chips allow millions of servers to communicate instantly.",
    "whatItSells": "PAM4 Optical DSPs (Digital Signal Processors), custom cloud AI processors, and storage controllers.",
    "whoBuys": "Amazon Web Services (AWS), Microsoft, Google, and networking equipment makers.",
    "growthDrivers": "Every new AI data center requires millions of optical transceivers to connect server racks together.",
    "businessRisks": "Customer design cycles take 2-3 years; losing a single cloud ASIC generation can hurt growth.",
    "storySteps": [
      {
        "icon": "\u26a1",
        "title": "Copper Reaches Physics Limits",
        "desc": "Copper cables cannot transmit 800 Gigabits without overheating."
      },
      {
        "icon": "\ud83d\udca1",
        "title": "Marvell Converts Signals to Light",
        "desc": "Marvell's DSP converts electrons into laser light pulses over thin glass fibers."
      },
      {
        "icon": "\u2601\ufe0f",
        "title": "AWS Links Its AI Clusters",
        "desc": "Amazon links thousands of AI server racks across sprawling data center halls."
      }
    ],
    "upstream": [
      "TSM"
    ],
    "downstream": [
      "AMZN",
      "MSFT",
      "GOOGL"
    ],
    "competitors": [
      "AVGO"
    ]
  },
  {
    "symbol": "TSM",
    "name": "Taiwan Semiconductor (TSMC)",
    "simpleRole": "\ud83c\udfed The World's Microchip Factory",
    "sector": "Foundry & Fabrication",
    "layer": "Advanced Semiconductor Foundry",
    "price": 184.2,
    "change1D": -1.8,
    "change1M": 6.8,
    "growthYoY": 39.0,
    "rvol": 1.68,
    "marketCapB": 955.0,
    "peRatio": 26.5,
    "whatItDoes": "TSMC is the world's largest and most advanced semiconductor foundry. They physically manufacture the microscopic chips designed by Apple, NVIDIA, AMD, Qualcomm, and Broadcom.",
    "whyNeeded": "Designing a chip takes smart engineers; building a chip requires a $20 billion cleanroom factory with ultraviolet laser machines. No chip company can afford their own factory, so they all hire TSMC.",
    "whatItSells": "Finished silicon wafers printed with 3-nanometer and 2-nanometer microscopic circuitry, and CoWoS advanced 3D packaging.",
    "whoBuys": "NVIDIA, Apple (for every iPhone & Mac chip), AMD, Broadcom, Qualcomm, and Amazon.",
    "growthDrivers": "Every leading-edge AI chip in existence is manufactured exclusively at TSMC.",
    "businessRisks": "Geopolitical tensions in the Taiwan Strait and heavy dependency on equipment from ASML.",
    "storySteps": [
      {
        "icon": "\ud83d\udcd0",
        "title": "Nvidia/Apple Sends Blueprint",
        "desc": "Fabless designers send TSMC digital blueprints of billions of microscopic transistors."
      },
      {
        "icon": "\ud83d\udd2c",
        "title": "Printed with Extreme UV Light",
        "desc": "ASML lithography machines etch circuits only a few atoms wide onto pure silicon disks."
      },
      {
        "icon": "\ud83d\udce6",
        "title": "CoWoS 3D Stacking",
        "desc": "TSMC stacks the chip and high-bandwidth memory side-by-side on a micro-silicon base."
      },
      {
        "icon": "\ud83d\udea2",
        "title": "Shipped to Assembly Plants",
        "desc": "Finished processor modules are sent to Foxconn & Quanta to be built into servers."
      }
    ],
    "upstream": [
      "ASML",
      "AMKR"
    ],
    "downstream": [
      "NVDA",
      "AAPL",
      "AMD",
      "AVGO",
      "QCOM"
    ],
    "competitors": [
      "INTC"
    ]
  },
  {
    "symbol": "AMKR",
    "name": "Amkor Technology",
    "simpleRole": "\ud83d\udce6 The Chip Packaging Specialist",
    "sector": "Foundry & Fabrication",
    "layer": "Advanced Packaging (OSAT)",
    "price": 28.4,
    "change1D": 0.8,
    "change1M": 4.5,
    "growthYoY": 12.0,
    "rvol": 1.25,
    "marketCapB": 7.0,
    "peRatio": 16.8,
    "whatItDoes": "Amkor takes delicate raw silicon wafers cut from factories, encases them in protective housings, and solders the microscopic electrical pins so they can plug into motherboards.",
    "whyNeeded": "Modern AI chips are actually multiple small chips ('chiplets') stitched together in one package. Advanced packaging is the main bottleneck holding back AI supply.",
    "whatItSells": "2.5D and 3D semiconductor packaging, wafer testing, and protective encapsulation.",
    "whoBuys": "TSMC (partner), Apple, Qualcomm, NVIDIA, and automotive electronics makers.",
    "growthDrivers": "TSMC's internal packaging lines are 100% full, forcing chip companies to outsource packaging to Amkor.",
    "businessRisks": "Cyclical demand in automotive and smartphone markets.",
    "storySteps": [
      {
        "icon": "\ud83d\udd2a",
        "title": "Raw Wafers Diced",
        "desc": "Silicon wafers are sliced into individual microchip dies."
      },
      {
        "icon": "\ud83d\udce6",
        "title": "Assembled with Substrates",
        "desc": "Amkor bonds multiple dies together and solders thousands of microscopic pins."
      },
      {
        "icon": "\ud83d\udee1\ufe0f",
        "title": "Encapsulated & Tested",
        "desc": "Protective resin protects the chip against thermal expansion and physical damage."
      }
    ],
    "upstream": [
      "Substrates"
    ],
    "downstream": [
      "TSM",
      "AAPL",
      "QCOM",
      "NVDA"
    ],
    "competitors": [
      "ASX"
    ]
  },
  {
    "symbol": "NVT",
    "name": "nVent Electric",
    "simpleRole": "\u2744\ufe0f The Liquid Cooling & Enclosure Shield",
    "sector": "Thermal & Electrical",
    "layer": "AI Liquid Cooling & Protection",
    "price": 101.86,
    "change1D": -5.77,
    "change1M": -18.2,
    "growthYoY": 44.0,
    "rvol": 1.45,
    "marketCapB": 16.46,
    "peRatio": 24.8,
    "whatItDoes": "nVent manufactures the precision plumbing, pumps, manifolds, and cooling distribution units (CDUs) that pump chilled liquid directly across sizzling-hot AI microchips inside server racks.",
    "whyNeeded": "NVIDIA's latest Blackwell servers produce over 120,000 watts of heat per rack\u2014enough to heat 10 homes. Blowing cold air over them no longer works; without liquid cooling, the chips would melt in seconds.",
    "whatItSells": "Direct-to-chip liquid cooling manifolds, quick-disconnect hoses, cooling distribution units (CDUs), and modular server cabinets.",
    "whoBuys": "NVIDIA, Microsoft, Amazon Web Services, CoreWeave, and hyperscale data center builders.",
    "growthDrivers": "The industry-wide transition from traditional air-conditioned data centers to 100% direct-to-chip liquid cooling.",
    "businessRisks": "Supply chain bottlenecks for specialized pumps or delays in hyperscale data center construction.",
    "storySteps": [
      {
        "icon": "\ud83d\udd25",
        "title": "120kW Heat Generated",
        "desc": "Dozens of NVIDIA GPUs running in one rack create extreme concentrated heat."
      },
      {
        "icon": "\u2744\ufe0f",
        "title": "nVent CDUs Pump Chilled Fluid",
        "desc": "nVent's precision pumps send cold dielectric liquid through stainless manifolds."
      },
      {
        "icon": "\ud83d\udca7",
        "title": "Direct Contact Cold Plates",
        "desc": "Heat transfers into the liquid with zero risk of leaks onto electrical circuits."
      },
      {
        "icon": "\ud83d\udee1\ufe0f",
        "title": "Continuous Operation",
        "desc": "Servers run at peak speed 24/7 without thermal throttling or hardware shutdowns."
      }
    ],
    "upstream": [
      "Copper",
      "Precision Pumps"
    ],
    "downstream": [
      "NVDA",
      "MSFT",
      "AMZN",
      "CRWV"
    ],
    "competitors": [
      "VRT",
      "ETN"
    ]
  },
  {
    "symbol": "VRT",
    "name": "Vertiv Holdings",
    "simpleRole": "\ud83c\udfe2 The Data Center Thermal Master",
    "sector": "Thermal & Electrical",
    "layer": "AI Liquid Cooling & Protection",
    "price": 128.4,
    "change1D": -4.2,
    "change1M": 14.5,
    "growthYoY": 38.0,
    "rvol": 1.62,
    "marketCapB": 48.2,
    "peRatio": 42.1,
    "whatItDoes": "Vertiv is the world's leading provider of complete critical digital infrastructure\u2014industrial cooling chillers, uninterruptible power systems (UPS), and power distribution units for data centers.",
    "whyNeeded": "If an AI data center loses power for even one second, months of model training can be permanently corrupted. Vertiv keeps the electricity clean and the temperature stable.",
    "whatItSells": "Industrial hybrid chillers, high-density cooling distribution units, battery backup systems, and intelligent power racks.",
    "whoBuys": "Microsoft, Google, NVIDIA, Oracle, Meta, and major colocation providers like Equinix and Digital Realty.",
    "growthDrivers": "Every new gigawatt-scale AI campus requires hundreds of millions of dollars of Vertiv power and cooling equipment.",
    "businessRisks": "Higher interest rates could slow down speculative real-estate data center construction.",
    "storySteps": [
      {
        "icon": "\ud83c\udfd7\ufe0f",
        "title": "New 500MW AI Campus Built",
        "desc": "A cloud provider breaks ground on a massive computer center."
      },
      {
        "icon": "\u2744\ufe0f",
        "title": "Vertiv Installs Chiller Systems",
        "desc": "Vertiv equips the building with rooftop chillers, indoor CDUs, and pipework."
      },
      {
        "icon": "\ud83d\udd0b",
        "title": "Battery Backup Protected",
        "desc": "Industrial UPS batteries ensure power never blinks during utility grid spikes."
      },
      {
        "icon": "\ud83d\udcbb",
        "title": "Houses Tens of Thousands of GPUs",
        "desc": "Servers operate in climate-controlled, uninterrupted harmony."
      }
    ],
    "upstream": [
      "Industrial Compressors"
    ],
    "downstream": [
      "MSFT",
      "GOOGL",
      "NVDA",
      "ORCL"
    ],
    "competitors": [
      "NVT",
      "ETN"
    ]
  },
  {
    "symbol": "BE",
    "name": "Bloom Energy",
    "simpleRole": "\u26a1 The Instant On-Site Power Plant",
    "sector": "Energy & Power",
    "layer": "AI Baseload & Fuel Cells",
    "price": 178.13,
    "change1D": 8.4,
    "change1M": 82.0,
    "growthYoY": 28.0,
    "rvol": 2.85,
    "marketCapB": 4.12,
    "peRatio": 38.5,
    "whatItDoes": "Bloom Energy builds solid-oxide fuel cell 'Energy Servers' that convert natural gas or hydrogen into clean, reliable baseload electricity on-site with zero combustion.",
    "whyNeeded": "Connecting a new AI data center to the traditional electric utility grid takes 5 to 7 years in the US. Bloom Energy can install and turn on a 50-megawatt power system in just 50 days right next to the building.",
    "whatItSells": "Bloom Energy Solid-Oxide Fuel Cell Servers and microgrid electrical management software.",
    "whoBuys": "American Electric Power (AEP), CoreWeave, Microsoft, Amazon, and hospital campuses.",
    "growthDrivers": "Data centers cannot wait 5 years for power lines; Bloom signed a landmark 1-Gigawatt contract with utility giant AEP to power AI sites immediately.",
    "businessRisks": "Requires access to natural gas pipelines and faces competition from utility grid upgrades.",
    "storySteps": [
      {
        "icon": "\ud83d\uded1",
        "title": "Grid Queue is 5 Years Long",
        "desc": "A data center has 50,000 AI chips ready but the electric company has no power available."
      },
      {
        "icon": "\ud83d\ude9a",
        "title": "Bloom Trucks in Fuel Cells",
        "desc": "Modular energy server cabinets are delivered and connected in weeks."
      },
      {
        "icon": "\u26a1",
        "title": "Chemical Energy Conversion",
        "desc": "Solid oxide cells produce continuous electricity without burning fuel or smoking."
      },
      {
        "icon": "\ud83d\udfe2",
        "title": "AI Servers Turn On Immediately",
        "desc": "The data center starts generating cloud revenue years ahead of competitors."
      }
    ],
    "upstream": [
      "Natural Gas",
      "Ceramics"
    ],
    "downstream": [
      "CRWV",
      "MSFT",
      "AMZN"
    ],
    "competitors": [
      "PLUG",
      "GEV"
    ]
  },
  {
    "symbol": "CEG",
    "name": "Constellation Energy",
    "simpleRole": "\u269b\ufe0f The Clean Nuclear Giant",
    "sector": "Energy & Power",
    "layer": "Nuclear Baseload Power",
    "price": 242.5,
    "change1D": 1.2,
    "change1M": 16.4,
    "growthYoY": 24.0,
    "rvol": 1.38,
    "marketCapB": 76.2,
    "peRatio": 32.4,
    "whatItDoes": "Constellation Energy is the largest producer of carbon-free energy in the United States, operating the nation's biggest fleet of commercial nuclear power reactors.",
    "whyNeeded": "Solar only works when the sun shines and wind only blows occasionally. Nuclear is the only zero-carbon energy source on Earth that runs 24 hours a day, 7 days a week, 365 days a year at 95%+ capacity.",
    "whatItSells": "Carbon-free baseload wholesale electricity and multi-decade direct Power Purchase Agreements (PPAs).",
    "whoBuys": "Microsoft (signed 20-year contract), tech hyperscalers, and regional power grids across the Midwest and East Coast.",
    "growthDrivers": "Tech companies have strict 100% net-zero carbon pledges; restarting decommissioned reactors like Three Mile Island (Crane Clean Energy Center) exclusively for Microsoft.",
    "businessRisks": "Complex regulatory approvals from the Nuclear Regulatory Commission (NRC) and grid operator challenges.",
    "storySteps": [
      {
        "icon": "\ud83c\udf3f",
        "title": "Microsoft Pledges Zero Carbon",
        "desc": "Microsoft needs gigawatts of electricity but refuses to burn coal or polluting gas."
      },
      {
        "icon": "\u269b\ufe0f",
        "title": "Constellation Restarts Nuclear Plant",
        "desc": "Invests $1.6B to restore Unit 1 at Three Mile Island under a 20-year contract."
      },
      {
        "icon": "\ud83d\udd0c",
        "title": "835 Megawatts Direct to Cloud",
        "desc": "Generates 24/7 clean power dedicated entirely to Azure AI data centers."
      },
      {
        "icon": "\ud83c\udf10",
        "title": "Guaranteed Continuous Operation",
        "desc": "Keeps servers humming rain or shine with zero atmospheric carbon emissions."
      }
    ],
    "upstream": [
      "Uranium",
      "NRC"
    ],
    "downstream": [
      "MSFT"
    ],
    "competitors": [
      "VST"
    ]
  },
  {
    "symbol": "VST",
    "name": "Vistra Corp",
    "simpleRole": "\u26a1 The Power House Producer",
    "sector": "Energy & Power",
    "layer": "Nuclear & Gas Baseload Power",
    "price": 142.1,
    "change1D": 2.4,
    "change1M": 28.5,
    "growthYoY": 42.0,
    "rvol": 1.75,
    "marketCapB": 49.5,
    "peRatio": 22.0,
    "whatItDoes": "Vistra is one of the largest competitive electricity generators in America, operating 41 gigawatts of nuclear, natural gas, solar, and massive battery storage facilities in Texas, Ohio, and Pennsylvania.",
    "whyNeeded": "As electricity demand skyrockets due to data centers, electric vehicles, and factories, power shortages cause wholesale electricity prices to surge.",
    "whatItSells": "Wholesale megawatt-hours of electricity, capacity reserves, and direct corporate energy contracts.",
    "whoBuys": "Regional electric grids (ERCOT Texas, PJM Northeast), commercial utilities, and hyperscale data center operators.",
    "growthDrivers": "Skyrocketing wholesale electricity prices in power-constrained regions and long-term contracts with data center tenants.",
    "businessRisks": "Extreme weather events (like Texas freezes) or government regulations on energy wholesale pricing.",
    "storySteps": [
      {
        "icon": "\ud83d\udcc8",
        "title": "Texas & Virginia Power Shortages",
        "desc": "Electricity demand outpaces supply as hundreds of data centers plug into the grid."
      },
      {
        "icon": "\u26a1",
        "title": "Vistra Dispatches Energy",
        "desc": "Runs nuclear and gas turbines at full capacity to meet peak power spikes."
      },
      {
        "icon": "\ud83d\udcb0",
        "title": "Soaring Wholesale Prices",
        "desc": "Higher power rates generate massive cash flow for electricity producers."
      }
    ],
    "upstream": [
      "Natural Gas",
      "Uranium"
    ],
    "downstream": [
      "ERCOT Grid",
      "PJM Grid"
    ],
    "competitors": [
      "CEG"
    ]
  },
  {
    "symbol": "OKLO",
    "name": "Oklo Inc.",
    "simpleRole": "\ud83d\udd2c The Compact Nuclear Pioneer",
    "sector": "Energy & Power",
    "layer": "Small Modular Reactors (SMRs)",
    "price": 24.8,
    "change1D": 4.5,
    "change1M": 48.0,
    "growthYoY": 0.0,
    "rvol": 2.1,
    "marketCapB": 3.1,
    "peRatio": -1.0,
    "whatItDoes": "Oklo designs fast-fission 'Small Modular nuclear Reactors' (SMRs) called the Aurora powerhouse that can produce 15 to 50 megawatts of clean energy in a footprint no larger than a school gymnasium.",
    "whyNeeded": "Traditional nuclear plants take 15 years and $15 billion to build. Oklo's micro-reactors can be manufactured in a factory, trucked to an AI site, and buried safely right beside the data center.",
    "whatItSells": "Direct electricity and high-temperature heat from on-site small modular nuclear powerhouses.",
    "whoBuys": "Data center operators, AI labs, industrial manufacturing plants, and military bases.",
    "growthDrivers": "Backed by Sam Altman (CEO of OpenAI); tech companies wanting dedicated nuclear power plants on their own property.",
    "businessRisks": "Pre-revenue company; still waiting for final design licenses from the Nuclear Regulatory Commission (NRC).",
    "storySteps": [
      {
        "icon": "\ud83e\udde0",
        "title": "OpenAI Needs Dedicated Energy",
        "desc": "Future AI models will require gigawatts of dedicated power."
      },
      {
        "icon": "\ud83d\udd2c",
        "title": "Oklo Engineers Micro-Reactors",
        "desc": "Designs compact, self-cooling nuclear reactors that run on recycled nuclear fuel."
      },
      {
        "icon": "\ud83c\udfd7\ufe0f",
        "title": "Co-Located at Data Centers",
        "desc": "Planted right next to computer centers, eliminating hundreds of miles of transmission wires."
      }
    ],
    "upstream": [
      "LEU",
      "NRC"
    ],
    "downstream": [
      "Frontier AI Labs"
    ],
    "competitors": [
      "SMR"
    ]
  },
  {
    "symbol": "NBIS",
    "name": "Nebius Group",
    "simpleRole": "\u2601\ufe0f The Clean-Slate AI Neocloud",
    "sector": "Cloud Infrastructure",
    "layer": "AI Neocloud & GPU Clusters",
    "price": 29.8,
    "change1D": 1.4,
    "change1M": 32.5,
    "growthYoY": 210.0,
    "rvol": 2.4,
    "marketCapB": 5.8,
    "peRatio": -1.0,
    "whatItDoes": "Nebius is a purpose-built European & Western AI cloud company. Unlike old cloud providers bogged down by 20-year-old software, Nebius built its data centers exclusively for NVIDIA GPU clusters from day one.",
    "whyNeeded": "Developers waiting months for GPU allocations at Amazon or Google can spin up thousands of synchronized H100 and Blackwell chips on Nebius within minutes.",
    "whatItSells": "High-performance GPU cluster compute by the hour, bare-metal AI infrastructure, and managed AI platform tools.",
    "whoBuys": "AI research labs, frontier startups (like Mistral AI), European enterprises, and autonomous driving teams.",
    "growthDrivers": "Over $2 billion in unencumbered cash with zero net debt, preferred NVIDIA tier-1 cloud partner allocation, and surging European AI sovereignty demand.",
    "businessRisks": "Intense competition from hyperscalers (Azure, AWS) and peer neoclouds (CoreWeave).",
    "storySteps": [
      {
        "icon": "\ud83d\ude80",
        "title": "AI Startups Need Fast GPUs",
        "desc": "Engineers need 4,000 GPUs linked together without waiting in 9-month cloud queues."
      },
      {
        "icon": "\u2601\ufe0f",
        "title": "Nebius Provides Instant Clusters",
        "desc": "Delivers purpose-built high-bandwidth InfiniBand clusters ready for training."
      },
      {
        "icon": "\ud83d\udcb6",
        "title": "European Sovereign Data Centers",
        "desc": "Complies 100% with European data privacy and AI regulations."
      }
    ],
    "upstream": [
      "NVDA",
      "TSM"
    ],
    "downstream": [
      "Enterprise AI Labs"
    ],
    "competitors": [
      "CRWV",
      "MSFT"
    ]
  },
  {
    "symbol": "CRWV",
    "name": "CoreWeave",
    "simpleRole": "\u26a1 The Specialized GPU Cloud Pioneer",
    "sector": "Cloud Infrastructure",
    "layer": "AI Neocloud & GPU Clusters",
    "price": 54.0,
    "change1D": 3.2,
    "change1M": 28.0,
    "growthYoY": 340.0,
    "rvol": 1.95,
    "marketCapB": 19.5,
    "peRatio": -1.0,
    "whatItDoes": "CoreWeave started as an Ethereum mining firm and pivoted early into the world's most aggressive buyer of NVIDIA AI supercomputers, renting them to companies training large language models.",
    "whyNeeded": "When Microsoft ran out of AI computing power for OpenAI in 2023, it signed a multi-billion-dollar deal to rent CoreWeave's GPU clusters to fill the gap.",
    "whatItSells": "Dedicated NVIDIA GPU clusters, Kubernetes AI management, and ultra-low-latency cloud networking.",
    "whoBuys": "Microsoft, Inflection AI, Cohere, Mistral, and leading enterprise AI developers.",
    "growthDrivers": "Strategic backing and guaranteed GPU allocations directly from NVIDIA.",
    "businessRisks": "Heavy debt taken on to purchase tens of thousands of GPUs and potential contract renegotiation by hyperscale customers.",
    "storySteps": [
      {
        "icon": "\ud83d\uded1",
        "title": "Microsoft Azure Runs Out of GPUs",
        "desc": "Azure demand for OpenAI explodes beyond its internal data center capacity."
      },
      {
        "icon": "\ud83e\udd1d",
        "title": "Contracts CoreWeave's Fleet",
        "desc": "Signs multi-billion-dollar leases for tens of thousands of CoreWeave GPUs."
      },
      {
        "icon": "\u26a1",
        "title": "Expands with Bloom Energy",
        "desc": "Partners with Bloom Energy to power new data center sites in record time."
      }
    ],
    "upstream": [
      "NVDA",
      "BE"
    ],
    "downstream": [
      "MSFT"
    ],
    "competitors": [
      "NBIS",
      "APLD"
    ]
  },
  {
    "symbol": "APLD",
    "name": "Applied Digital",
    "simpleRole": "\ud83c\udfd7\ufe0f The High-Power Campus Landlord",
    "sector": "Cloud Infrastructure",
    "layer": "AI Data Center Campuses",
    "price": 8.4,
    "change1D": 1.1,
    "change1M": 14.0,
    "growthYoY": 85.0,
    "rvol": 1.8,
    "marketCapB": 1.45,
    "peRatio": -1.0,
    "whatItDoes": "Applied Digital finds land near cheap power sources in North Dakota and Texas, secures massive electrical permits (100MW to 400MW), and builds custom data center buildings for cloud tenants.",
    "whyNeeded": "AI data centers require 5 times more electricity per square foot than standard server warehouses. Applied Digital specializes in high-power engineering.",
    "whatItSells": "High-density data center lease space, power interconnects, and cooling management.",
    "whoBuys": "NVIDIA (investor), CoreWeave, and hyperscale tech companies.",
    "growthDrivers": "Secured major institutional investments and multi-year leases for hundreds of megawatts of compute space.",
    "businessRisks": "High capital costs to construct buildings and dependence on debt financing.",
    "storySteps": [
      {
        "icon": "\ud83d\udccd",
        "title": "Secures Power in North Dakota",
        "desc": "Secures hundreds of megawatts of stranded electrical capacity."
      },
      {
        "icon": "\ud83c\udfd7\ufe0f",
        "title": "Constructs 100MW Buildings",
        "desc": "Builds high-density shell buildings with heavy liquid cooling infrastructure."
      },
      {
        "icon": "\ud83d\udcbb",
        "title": "Leases to AI Clouds",
        "desc": "Tenants fill the building with thousands of AI servers."
      }
    ],
    "upstream": [
      "NVT",
      "VRT"
    ],
    "downstream": [
      "CRWV"
    ],
    "competitors": [
      "APLD"
    ]
  },
  {
    "symbol": "PLTR",
    "name": "Palantir Technologies",
    "simpleRole": "\ud83d\udee1\ufe0f The Enterprise & Defense AI Operating System",
    "sector": "Software & AI Defense",
    "layer": "Enterprise AI & Defense Software",
    "price": 64.2,
    "change1D": 2.8,
    "change1M": 44.0,
    "growthYoY": 30.0,
    "rvol": 2.2,
    "marketCapB": 145.0,
    "peRatio": 115.0,
    "whatItDoes": "Palantir makes the software that connects messy, fragmented company or military data into a live digital map (an 'ontology') and lets generative AI safely take real-world actions.",
    "whyNeeded": "Companies can chat with ChatGPT, but ChatGPT doesn't know their factory inventory or supply chain rules. Palantir gives AI the verified data and safety guardrails needed to run actual businesses and military operations.",
    "whatItSells": "AIP (Artificial Intelligence Platform), Gotham (defense & intelligence), and Foundry (commercial enterprise software).",
    "whoBuys": "U.S. Department of Defense (Army, Navy, Space Force), BP, Airbus, Cleveland Clinic, Tyson Foods, and hundreds of commercial corporations.",
    "growthDrivers": "AIP is being adopted at record speed by U.S. companies looking to turn AI into measurable profits; lucrative multi-hundred-million-dollar defense contracts.",
    "businessRisks": "Very high valuation multiple (P/E > 100x) leaves little room for revenue slowdowns.",
    "storySteps": [
      {
        "icon": "\ud83d\udcc2",
        "title": "Company Has 50 Different Databases",
        "desc": "Hospitals or airlines have fragmented data scattered across legacy software."
      },
      {
        "icon": "\ud83d\uddfa\ufe0f",
        "title": "Palantir Builds the Digital Twin",
        "desc": "Foundry maps real-world airplanes, patients, parts, and schedules into one live screen."
      },
      {
        "icon": "\ud83e\udd16",
        "title": "AIP Automates Decisions",
        "desc": "AI agents re-route flights around storms or reorder hospital supplies automatically."
      },
      {
        "icon": "\ud83d\udee1\ufe0f",
        "title": "Deploys on Battlefield",
        "desc": "U.S. Army uses Project Maven and TITAN to identify threats and coordinate sensors in real time."
      }
    ],
    "upstream": [
      "MSFT"
    ],
    "downstream": [
      "U.S. DoD"
    ],
    "competitors": [
      "SNOW"
    ]
  },
  {
    "symbol": "SOFI",
    "name": "SoFi Technologies",
    "simpleRole": "\ud83c\udfe6 The Mobile-First Digital Bank",
    "sector": "Fintech & Banking",
    "layer": "Digital Banking & Tech Platform",
    "price": 15.42,
    "change1D": 1.4,
    "change1M": 38.0,
    "growthYoY": 30.0,
    "rvol": 1.65,
    "marketCapB": 16.2,
    "peRatio": 32.0,
    "whatItDoes": "SoFi is a fully chartered digital bank with no brick-and-mortar branches. It provides high-yield checking, student and personal loans, automated investing, credit cards, and backend payment infrastructure.",
    "whyNeeded": "Young people despise traditional bank fees and paperwork. SoFi combines all personal financial needs into one seamless mobile app with high deposit interest rates.",
    "whatItSells": "High-yield bank deposits, personal & student loans, home mortgages, SoFi Invest, and Galileo payment-processing software for other fintechs.",
    "whoBuys": "Over 9.4 million everyday consumer members, plus other fintech companies (like Robinhood) that use Galileo to power their debit cards.",
    "growthDrivers": "Four straight quarters of GAAP profitability, deposit inflows compounding over $24B, and high-margin software fee revenue from Galileo.",
    "businessRisks": "Rapid interest rate changes affecting borrower loan repayment or student loan regulatory policy changes.",
    "storySteps": [
      {
        "icon": "\ud83d\udcf1",
        "title": "User Downloads Mobile App",
        "desc": "A college graduate signs up to refinance student debt and earn high interest on savings."
      },
      {
        "icon": "\ud83d\udcb3",
        "title": "Direct Deposit Inflow",
        "desc": "User sets up paycheck direct deposit, giving SoFi low-cost loan funding."
      },
      {
        "icon": "\u2699\ufe0f",
        "title": "Galileo Powers Other Fintechs",
        "desc": "SoFi's software core processes debit transactions for millions of non-SoFi users."
      },
      {
        "icon": "\ud83d\udcc8",
        "title": "Compounds Into Financial Super-App",
        "desc": "User takes out a mortgage and buys stocks inside the same account."
      }
    ],
    "upstream": [
      "AWS"
    ],
    "downstream": [
      "9.4M+ Members"
    ],
    "competitors": [
      "HOOD"
    ]
  },
  {
    "symbol": "LLY",
    "name": "Eli Lilly and Company",
    "simpleRole": "\ud83d\udc8a The Weight-Loss Medicine Monopoly",
    "sector": "Healthcare & Biotech",
    "layer": "GLP-1 Metabolic Health Monopoly",
    "price": 782.5,
    "change1D": 0.6,
    "change1M": -6.5,
    "growthYoY": 42.0,
    "rvol": 1.15,
    "marketCapB": 742.0,
    "peRatio": 54.0,
    "whatItDoes": "Eli Lilly discovers and produces life-saving pharmaceutical drugs, most famously Mounjaro and Zepbound (tirzepatide)\u2014groundbreaking injectable medicines that treat diabetes and cause massive, safe weight loss.",
    "whyNeeded": "Obesity and diabetes affect over 1 billion people worldwide, driving heart attacks, strokes, and healthcare bankruptcies. Lilly's medicines mimic natural gut hormones to turn off appetite and restore insulin balance.",
    "whatItSells": "Zepbound (weight loss), Mounjaro (type 2 diabetes), Verzenio (breast cancer), and Kisunla (Alzheimer's disease).",
    "whoBuys": "Patients, retail pharmacies (CVS, Walgreens), hospital health systems, and health insurance providers.",
    "growthDrivers": "Demand for Zepbound is virtually limitless; Lilly is investing $9 billion in new manufacturing plants to produce tens of millions of pens per year.",
    "businessRisks": "Compounding pharmacies making copycat drugs during shortages, patent expirations down the road, and insurance coverage battles.",
    "storySteps": [
      {
        "icon": "\ud83e\uddec",
        "title": "Scientists Discover GIP/GLP-1",
        "desc": "Discovers how dual hormone receptors signal fullness to the human brain."
      },
      {
        "icon": "\ud83d\udc89",
        "title": "Formulates Tirzepatide",
        "desc": "Clinical trials show patients lose up to 22.5% of total body weight safely."
      },
      {
        "icon": "\ud83c\udfed",
        "title": "Automated Injector Pen Production",
        "desc": "Massive sterile manufacturing lines fill and assemble millions of weekly pens."
      },
      {
        "icon": "\ud83c\udfe5",
        "title": "Prescribed Globally",
        "desc": "Patients reverse metabolic disease and lower risks of cardiovascular events."
      }
    ],
    "upstream": [
      "API Precursors"
    ],
    "downstream": [
      "Pharmacies"
    ],
    "competitors": [
      "NVO"
    ]
  },
  {
    "symbol": "MSFT",
    "name": "Microsoft Corporation",
    "simpleRole": "\ud83d\udcbb The AI Enterprise Powerhouse",
    "sector": "Hyperscale Cloud",
    "layer": "Hyperscale Cloud & Frontier AI",
    "price": 428.0,
    "change1D": -0.8,
    "change1M": 3.4,
    "growthYoY": 16.0,
    "rvol": 1.1,
    "marketCapB": 3180.0,
    "peRatio": 34.0,
    "whatItDoes": "Microsoft is the world's enterprise software giant (Windows, Office 365) and the #2 cloud provider (Azure). It partnered with and invested $13B+ in OpenAI, integrating ChatGPT into all its products.",
    "whyNeeded": "Nearly every business on Earth runs on Windows, Excel, and Teams. By adding AI Copilots to tools employees already use, Microsoft makes enterprise AI instantly accessible.",
    "whatItSells": "Azure AI Cloud Services, Microsoft 365 Copilot subscriptions, Windows OS, and GitHub Copilot for programmers.",
    "whoBuys": "Over 85% of Fortune 500 corporations, government agencies, schools, and developers.",
    "growthDrivers": "Millions of corporate employees upgrading to $30/month Copilot seats, and Azure cloud revenue surging from AI model hosting.",
    "businessRisks": "Huge data center CapEx spending ($80B+ a year) pressuring operating margins if enterprise AI monetization takes time.",
    "storySteps": [
      {
        "icon": "\ud83e\udd1d",
        "title": "Partners with OpenAI",
        "desc": "Invests billions in exchange for exclusive commercial rights to GPT-4 models."
      },
      {
        "icon": "\u2601\ufe0f",
        "title": "Builds Azure Supercomputers",
        "desc": "Buys tens of thousands of Nvidia GPUs and contracts nuclear power to run them."
      },
      {
        "icon": "\ud83d\udcca",
        "title": "Embeds AI in Word & Excel",
        "desc": "Office Copilot writes emails, analyzes spreadsheets, and generates slides in seconds."
      }
    ],
    "upstream": [
      "NVDA",
      "CEG"
    ],
    "downstream": [
      "Global Enterprises"
    ],
    "competitors": [
      "GOOGL"
    ]
  },
  {
    "symbol": "GOOGL",
    "name": "Alphabet Inc.",
    "simpleRole": "\ud83d\udd0d The Vertically-Integrated AI Titan",
    "sector": "Hyperscale Cloud",
    "layer": "Search, TPU Silicon & Cloud",
    "price": 176.4,
    "change1D": 1.1,
    "change1M": 5.8,
    "growthYoY": 15.0,
    "rvol": 1.2,
    "marketCapB": 2180.0,
    "peRatio": 22.5,
    "whatItDoes": "Alphabet operates the world's #1 search engine (Google), video platform (YouTube), smartphone OS (Android), and Google Cloud. It develops frontier Gemini AI models and designs its own custom TPU chips.",
    "whyNeeded": "Google is the only tech titan that owns every single layer of the AI stack: its own custom silicon (TPUs), its own deep research lab (Google DeepMind), its own global fiber network, and billions of daily users.",
    "whatItSells": "Digital advertising on Search & YouTube, Google Cloud Platform (GCP) compute, and Gemini Advanced subscriptions.",
    "whoBuys": "Billions of global internet users, millions of advertisers, and enterprise cloud customers.",
    "growthDrivers": "AI overviews increasing search user engagement, YouTube ad revenue resilience, and Google Cloud margin expansion.",
    "businessRisks": "Antitrust legal challenges from the U.S. Department of Justice regarding search distribution and browser defaults.",
    "storySteps": [
      {
        "icon": "\ud83e\uddea",
        "title": "DeepMind Invents Transformer",
        "desc": "Google researchers publish the landmark paper that created modern generative AI."
      },
      {
        "icon": "\ud83d\udd0c",
        "title": "Builds Custom TPU Chips",
        "desc": "Designs 6 generations of custom Tensor Processing Units with Broadcom."
      },
      {
        "icon": "\ud83c\udf10",
        "title": "Serves 3 Billion People Daily",
        "desc": "Deploys Gemini into Search, Android, Gmail, and YouTube at global scale."
      }
    ],
    "upstream": [
      "AVGO",
      "TSM"
    ],
    "downstream": [
      "Global Consumers"
    ],
    "competitors": [
      "MSFT"
    ]
  }
];
    this._relationships = {
  "TSM-NVDA": {
    "source": "TSM",
    "target": "NVDA",
    "sourceRole": "The Microchip Factory (TSMC)",
    "targetRole": "The AI Chip Designer (NVIDIA)",
    "type": "Confirmed Multi-Billion-Dollar Manufacturing Contract",
    "badge": "\ud83c\udfed Foundry Supplier \u2794 Designer",
    "direction": "TSM (Manufactures Chips) \u2794 NVDA (Receives Finished Silicon)",
    "goodsFlow": "3nm & 4nm microchip wafers with CoWoS 3D packaging",
    "cashFlow": "NVIDIA pays TSMC tens of billions of dollars annually",
    "whyMatters": "NVIDIA has zero semiconductor factories of its own. It is completely physically dependent on TSMC to build its Blackwell and Hopper chips. Without TSMC, NVIDIA cannot sell a single GPU. Meanwhile, NVIDIA represents over 11% of TSMC's total global revenue.",
    "ifDemandRises": "TSMC cleanroom factories run at 100% capacity, expanding high-margin CoWoS packaging lines. TSMC raises wafer prices, boosting operating margins.",
    "ifDemandDrops": "NVIDIA wafer orders slow down, but TSMC's massive customer base (Apple, AMD, Qualcomm, Broadcom) cushions the blow.",
    "dependenceLevel": "Critical (10/10) \u2014 100% of NVIDIA's leading-edge chips come from TSMC."
  },
  "NVDA-NVT": {
    "source": "NVDA",
    "target": "NVT",
    "sourceRole": "The AI Chip Designer (NVIDIA)",
    "targetRole": "The Liquid Cooling Provider (nVent)",
    "type": "Certified Co-Design Thermal & Plumbing Partnership",
    "badge": "\u2744\ufe0f Thermal Co-Design Partner",
    "direction": "NVT (Pumps & Manifolds) \u2794 NVDA (Directly Inside Blackwell Racks)",
    "goodsFlow": "Liquid cooling distribution units (CDUs), manifolds, and quick-disconnect hoses",
    "cashFlow": "Data center operators and server builders buy nVent plumbing specified by NVIDIA",
    "whyMatters": "NVIDIA's latest Blackwell GB200 racks produce over 120,000 watts of heat\u2014enough to melt standard servers. Traditional air cooling cannot remove this heat. nVent co-designed the internal fluid manifolds directly with NVIDIA so liquid touches the chip plates safely.",
    "ifDemandRises": "Every new NVIDIA Blackwell rack deployed forces data centers to install nVent cooling manifolds, resulting in explosive +40% to +60% backlog growth for nVent.",
    "ifDemandDrops": "If data centers delay Blackwell buildouts, nVent's liquid cooling shipments slow, but its legacy industrial electrical enclosures provide downside support.",
    "dependenceLevel": "High (9/10) \u2014 Liquid cooling is a physical requirement for next-generation AI."
  },
  "NVDA-VRT": {
    "source": "NVDA",
    "target": "VRT",
    "sourceRole": "The AI Chip Designer (NVIDIA)",
    "targetRole": "The Data Center Thermal Master (Vertiv)",
    "type": "Strategic Digital Infrastructure & Power Partnership",
    "badge": "\ud83c\udfe2 Facility Cooling & Power Infrastructure",
    "direction": "VRT (Mega-Chillers & UPS) \u2794 NVDA (Cooling & Protecting Clusters)",
    "goodsFlow": "Industrial cooling chillers, cooling distribution units (CDUs), and uninterruptible power systems (UPS)",
    "cashFlow": "Cloud providers (Microsoft, Oracle, Google) pay Vertiv to equip data centers for NVIDIA chips",
    "whyMatters": "While nVent cools inside the server rack, Vertiv cools and powers the entire building. Vertiv takes the boiling liquid from the server racks and chills it using rooftop industrial heat exchangers.",
    "ifDemandRises": "Hyperscalers order gigawatts of Vertiv power and cooling infrastructure, creating multi-year backlogs and pricing power.",
    "ifDemandDrops": "Data center construction delays could push Vertiv equipment delivery dates into later quarters.",
    "dependenceLevel": "High (9/10) \u2014 Massive AI clusters cannot run without industrial heat dissipation."
  },
  "NVDA-BE": {
    "source": "NVDA",
    "target": "BE",
    "sourceRole": "The AI Chip Designer (NVIDIA)",
    "targetRole": "The Instant On-Site Power Plant (Bloom Energy)",
    "type": "Commercial AI Baseload Power Agreement",
    "badge": "\u26a1 Instant On-Site Power Supply",
    "direction": "BE (Solid-Oxide Electricity) \u2794 NVDA (Powers GPU Clusters)",
    "goodsFlow": "Continuous 24/7 on-site baseload electricity generated from natural gas/hydrogen fuel cells",
    "cashFlow": "Cloud hosts (CoreWeave, AEP) pay Bloom Energy for dedicated power servers",
    "whyMatters": "Connecting a data center to the traditional electric grid takes 5 to 7 years in Virginia and Texas. Bloom Energy installs fuel cells in just 50 days, allowing NVIDIA clusters to turn on and make money years ahead of the utility grid.",
    "ifDemandRises": "Bloom Energy secures multi-gigawatt deals (like its landmark 1GW agreement with AEP) as cloud hosts scramble for fast electricity.",
    "ifDemandDrops": "If traditional power grids rapidly add capacity, demand for temporary on-site fuel cells could moderate.",
    "dependenceLevel": "High (8/10) \u2014 Electric grid delays are the #1 bottleneck holding back AI compute."
  },
  "NVDA-MSFT": {
    "source": "NVDA",
    "target": "MSFT",
    "sourceRole": "The AI Chip Designer (NVIDIA)",
    "targetRole": "The Enterprise AI Cloud Giant (Microsoft)",
    "type": "Anchor Hyperscale Commercial Customer Agreement",
    "badge": "\ud83d\uded2 #1 Largest Customer Agreement",
    "direction": "NVDA (Supplies GPUs) \u2794 MSFT (Deploys in Azure Cloud)",
    "goodsFlow": "Tens of thousands of Blackwell & Hopper AI supercomputer nodes",
    "cashFlow": "Microsoft pays NVIDIA tens of billions of dollars annually (15-19% of NVIDIA's revenue)",
    "whyMatters": "Microsoft is NVIDIA's single largest customer in the world. Microsoft uses these chips to run OpenAI's ChatGPT models and power Microsoft 365 Copilot for hundreds of millions of corporate employees.",
    "ifDemandRises": "Microsoft expands data center CapEx beyond $80B annually, ensuring NVIDIA posts record quarterly revenue beats.",
    "ifDemandDrops": "Any pause by Microsoft in data center spending creates instant volatility for NVIDIA's stock.",
    "dependenceLevel": "Critical (10/10) \u2014 Microsoft is the anchor buyer funding the entire AI infrastructure wave."
  },
  "NVDA-AMD": {
    "source": "NVDA",
    "target": "AMD",
    "sourceRole": "The AI Market Leader (NVIDIA)",
    "targetRole": "The High-Speed Challenger (AMD)",
    "type": "Direct Market Competition (AI Accelerator GPUs)",
    "badge": "\u2694\ufe0f Direct Commercial Competitors",
    "direction": "NVDA (Defends ~80% Market Share) \u2694\ufe0f AMD (Captures ~10-15% Share)",
    "goodsFlow": "Competing for the exact same hyperscaler cloud accelerator budgets",
    "cashFlow": "Cloud buyers split budgets between NVIDIA Blackwell and AMD MI300X/MI325X",
    "whyMatters": "NVIDIA enjoys massive 75%+ gross margins. Cloud providers hate monopoly pricing and actively fund AMD as a viable second source to force price competition.",
    "ifDemandRises": "Both companies grow because the total AI market is expanding, but AMD can gain market share in 'inference' (running AI models) where software lock-in is weaker.",
    "ifDemandDrops": "NVIDIA's superior CUDA software ecosystem gives it stronger customer retention during downturns.",
    "dependenceLevel": "Competitive (8/10) \u2014 AMD acts as the primary price check against NVIDIA's monopoly."
  },
  "NVDA-NBIS": {
    "source": "NVDA",
    "target": "NBIS",
    "sourceRole": "The AI Chip Designer (NVIDIA)",
    "targetRole": "The Clean-Slate Neocloud (Nebius)",
    "type": "Certified Tier-1 NVIDIA Cloud Partner Agreement",
    "badge": "\u2601\ufe0f Preferred AI Cloud Partner",
    "direction": "NVDA (Priority GPU Allocations) \u2794 NBIS (Rents Clusters to Startups)",
    "goodsFlow": "High-priority delivery of H100, H200, and Blackwell GPU clusters",
    "cashFlow": "Nebius spends its $2B+ cash vault purchasing NVIDIA hardware",
    "whyMatters": "NVIDIA deliberately nurtures independent 'neoclouds' like Nebius to prevent Amazon, Microsoft, and Google from controlling 100% of the world's AI cloud hosting.",
    "ifDemandRises": "Nebius fills all available cluster capacity, driving revenue growth above +200% YoY.",
    "ifDemandDrops": "Nebius has zero net debt and over $2B cash, making it capable of surviving temporary pricing wars.",
    "dependenceLevel": "Strong (8/10) \u2014 Nebius's entire business model is built on NVIDIA accelerated computing."
  },
  "NVDA-CRWV": {
    "source": "NVDA",
    "target": "CRWV",
    "sourceRole": "The AI Chip Designer (NVIDIA)",
    "targetRole": "The Specialized GPU Cloud (CoreWeave)",
    "type": "Strategic Equity Investment & Priority Supply Contract",
    "badge": "\ud83e\udd1d Strategic Investment & Preferred Host",
    "direction": "NVDA (Equity Backer & Supplier) \u2794 CRWV (Pure-Play AI GPU Cloud)",
    "goodsFlow": "Tens of thousands of synchronized GPU clusters delivered ahead of competitors",
    "cashFlow": "CoreWeave borrows billions against GPUs to buy more NVIDIA hardware",
    "whyMatters": "NVIDIA owns an equity stake in CoreWeave and gives it priority access to new chips. CoreWeave was Microsoft's savior when Azure ran out of capacity for OpenAI.",
    "ifDemandRises": "CoreWeave signs multi-billion-dollar leases with AI developers, expanding its footprint across the US.",
    "ifDemandDrops": "CoreWeave carries substantial debt used to purchase GPUs, making high interest rates a key sensitivity.",
    "dependenceLevel": "Critical (9/10) \u2014 CoreWeave exists almost entirely as a scaled deployment engine for NVIDIA."
  },
  "AVGO-GOOGL": {
    "source": "AVGO",
    "target": "GOOGL",
    "sourceRole": "The Custom Chip Co-Designer (Broadcom)",
    "targetRole": "The Vertically-Integrated Titan (Google)",
    "type": "Exclusive Long-Term Custom ASIC Co-Design Contract",
    "badge": "\ud83d\udd0c Google TPU Co-Design Partner",
    "direction": "AVGO (Custom Design & Networking) \u2794 GOOGL (Powers Gemini & Search)",
    "goodsFlow": "Google Tensor Processing Unit (TPU v5/v6) custom silicon and optical switching",
    "cashFlow": "Google pays Broadcom billions for co-design IP and silicon royalties",
    "whyMatters": "Google does not rely solely on NVIDIA; it trains its flagship Gemini models on its own proprietary TPU chips. Broadcom is Google's exclusive co-design partner, making this one of the most profitable tech alliances in the world.",
    "ifDemandRises": "Google expands internal TPU deployment to cut costs, driving Broadcom's AI revenue to new all-time highs.",
    "ifDemandDrops": "Google represents a massive percentage of Broadcom's custom silicon revenue; any cancellation would be material.",
    "dependenceLevel": "Critical (10/10) \u2014 Power alliance behind Google's custom AI infrastructure."
  },
  "MSFT-CEG": {
    "source": "CEG",
    "target": "MSFT",
    "sourceRole": "The Clean Nuclear Giant (Constellation)",
    "targetRole": "The Enterprise AI Cloud Giant (Microsoft)",
    "type": "Historic 20-Year Binding Nuclear Power Purchase Agreement (PPA)",
    "badge": "\u269b\ufe0f 20-Year Nuclear Power Agreement",
    "direction": "CEG (835MW Clean Nuclear Electricity) \u2794 MSFT (Powers Azure AI Data Centers)",
    "goodsFlow": "100% of the continuous carbon-free electricity from Three Mile Island Unit 1",
    "cashFlow": "Microsoft pays premium, fixed long-term power rates for 20 continuous years",
    "whyMatters": "Microsoft pledged to be carbon-negative by 2030, but AI servers demand gigawatts of electricity. Constellation is spending $1.6 billion to bring a shut-down nuclear reactor back to life exclusively for Microsoft.",
    "ifDemandRises": "Sets the blueprint for the entire tech sector: tech giants will contract entire nuclear plants directly.",
    "ifDemandDrops": "Contract is legally binding for 20 years; Constellation's revenue is 100% guaranteed.",
    "dependenceLevel": "Permanent (10/10) \u2014 A 20-year multi-billion-dollar landmark clean energy pact."
  },
  "CRWV-BE": {
    "source": "BE",
    "target": "CRWV",
    "sourceRole": "The Instant On-Site Power Plant (Bloom Energy)",
    "targetRole": "The Specialized GPU Cloud (CoreWeave)",
    "type": "Commercial AI Baseload Power Agreement",
    "badge": "\u26a1 On-Site Fuel Cell Deployment",
    "direction": "BE (Solid-Oxide Fuel Cells) \u2794 CRWV (Powers Thousands of GPUs)",
    "goodsFlow": "Continuous on-site baseload power servers installed directly outside data centers",
    "cashFlow": "CoreWeave pays Bloom Energy for rapid power availability",
    "whyMatters": "CoreWeave has billions of dollars of NVIDIA GPUs waiting in warehouses. Every month without power costs millions in lost cloud lease revenue. Bloom installs power in 50 days, rescuing CoreWeave from utility grid delays.",
    "ifDemandRises": "CoreWeave expands Bloom fuel cells across all its North American data centers.",
    "ifDemandDrops": "If local utility grids catch up, reliance on on-site fuel cells could moderate.",
    "dependenceLevel": "Strong (8/10) \u2014 Eliminates the #1 bottleneck to turning on GPU clusters."
  }
};
    this._scenarios = [
  {
    "id": "nvda_boom",
    "title": "\ud83d\ude80 What happens if NVIDIA's AI chip demand doubles?",
    "trigger": "Generative AI models require 4x larger GPU clusters for reasoning (Blackwell Ultra Supercycle).",
    "dominoes": [
      {
        "step": 1,
        "ticker": "TSM",
        "name": "Taiwan Semiconductor",
        "role": "Foundry",
        "icon": "\ud83c\udfed",
        "businessImpact": "Cleanroom factories run at 100% capacity; raises 3nm wafer prices by 5-10%; aggressively expands CoWoS advanced 3D packaging lines.",
        "stockDistinction": "\ud83d\udfe2 Highly Positive: Direct expansion in high-margin advanced packaging revenue."
      },
      {
        "step": 2,
        "ticker": "AMKR",
        "name": "Amkor Technology",
        "role": "Packaging Partner",
        "icon": "\ud83d\udce6",
        "businessImpact": "TSMC's internal packaging lines overflow, forcing TSMC and NVIDIA to outsource secondary 2.5D packaging to Amkor.",
        "stockDistinction": "\ud83d\udfe2 Positive: High factory utilization, though lower profit margins than TSMC."
      },
      {
        "step": 3,
        "ticker": "NVT",
        "name": "nVent Electric",
        "role": "Liquid Cooling",
        "icon": "\u2744\ufe0f",
        "businessImpact": "Every Blackwell rack emits 120kW of heat and cannot use air. Data center builders must buy nVent fluid manifolds, CDUs, and hoses.",
        "stockDistinction": "\ud83d\udfe2 Massive Winner: High operating leverage; liquid cooling transforms from niche product into mandatory standard."
      },
      {
        "step": 4,
        "ticker": "VRT",
        "name": "Vertiv Holdings",
        "role": "Thermal Infrastructure",
        "icon": "\ud83c\udfe2",
        "businessImpact": "Data centers must install Vertiv mega-chillers on rooftops and heavy-duty uninterruptible power units inside the building.",
        "stockDistinction": "\ud83d\udfe2 Strong Winner: Order backlog reaches record multi-billion-dollar highs."
      },
      {
        "step": 5,
        "ticker": "BE",
        "name": "Bloom Energy",
        "role": "Baseload Power",
        "icon": "\u26a1",
        "businessImpact": "Utility power grids cannot connect new sites for 5 years. Cloud hosts buy Bloom fuel cells to get power in 50 days.",
        "stockDistinction": "\ud83d\udfe2 Explosive Surge: Transitions Bloom from clean-energy play to critical AI power savior."
      },
      {
        "step": 6,
        "ticker": "NBIS",
        "name": "Nebius Group",
        "role": "AI Neocloud",
        "icon": "\u2601\ufe0f",
        "businessImpact": "Receives priority Blackwell allocations from NVIDIA and leases clusters to AI startups at premium hourly rates.",
        "stockDistinction": "\ud83d\udfe2 High Growth: Revenue compounds >200% YoY as AI researchers scramble for compute."
      }
    ]
  },
  {
    "id": "power_grid_crunch",
    "title": "\u26a1 What happens if the power grid runs out of electricity?",
    "trigger": "Electric utilities in Virginia, Texas, and Georgia freeze new data center grid connections due to transformer shortages.",
    "dominoes": [
      {
        "step": 1,
        "ticker": "BE",
        "name": "Bloom Energy",
        "role": "Instant Power",
        "icon": "\u26a1",
        "businessImpact": "Becomes the #1 fastest solution on Earth to get power on-site in 50 days using natural gas fuel cells.",
        "stockDistinction": "\ud83d\udfe2 Huge Beneficiary: Data centers with stranded GPUs pay premium rates for immediate power."
      },
      {
        "step": 2,
        "ticker": "CEG",
        "name": "Constellation Energy",
        "role": "Nuclear Baseload",
        "icon": "\u269b\ufe0f",
        "businessImpact": "Hyperscalers compete to sign direct multi-decade power contracts with Constellation's nuclear fleet.",
        "stockDistinction": "\ud83d\udfe2 Long-Term Winner: Locks in high electricity prices for 20 years with zero fuel volatility."
      },
      {
        "step": 3,
        "ticker": "VST",
        "name": "Vistra Corp",
        "role": "Merchant Power",
        "icon": "\ud83d\udcc8",
        "businessImpact": "Wholesale electricity prices on regional grids spike by 30-50%, generating record free cash flow.",
        "stockDistinction": "\ud83d\udfe2 Immediate Winner: Direct merchant cash flow expansion."
      },
      {
        "step": 4,
        "ticker": "OKLO",
        "name": "Oklo Inc.",
        "role": "Micro-Reactors",
        "icon": "\ud83d\udd2c",
        "businessImpact": "Urgency for small modular reactors surges; tech giants fund SMR pilot sites directly.",
        "stockDistinction": "\ud83d\udfe1 Sentiment Winner: Accelerates regulatory approvals, though revenue remains years away."
      },
      {
        "step": 5,
        "ticker": "APLD",
        "name": "Applied Digital",
        "role": "Campus Landlord",
        "icon": "\ud83c\udfd7\ufe0f",
        "businessImpact": "Campuses that already possess pre-approved power permits become worth 3x to 5x more.",
        "stockDistinction": "\ud83d\udfe2 Asset Value Winner: Pre-permitted power capacity trades at huge premiums."
      }
    ]
  },
  {
    "id": "liquid_cooling_mandate",
    "title": "\u2744\ufe0f What happens if all AI data centers must switch to liquid cooling?",
    "trigger": "Next-gen AI chips reach 1,000+ watts each, making air conditioning obsolete across all major data centers.",
    "dominoes": [
      {
        "step": 1,
        "ticker": "NVT",
        "name": "nVent Electric",
        "role": "Rack Plumbing",
        "icon": "\u2744\ufe0f",
        "businessImpact": "Replaces traditional air cabinets with custom stainless manifolds and leak-detection sensors.",
        "stockDistinction": "\ud83d\udfe2 Transformative Winner: High recurring revenue from custom fluid plumbing."
      },
      {
        "step": 2,
        "ticker": "VRT",
        "name": "Vertiv Holdings",
        "role": "Facility Chillers",
        "icon": "\ud83c\udfe2",
        "businessImpact": "Captures the multi-million-dollar facility retrofit market, replacing old AC with liquid heat exchangers.",
        "stockDistinction": "\ud83d\udfe2 High Margin Expansion: Premium pricing on complex thermal engineering."
      },
      {
        "step": 3,
        "ticker": "NVDA",
        "name": "NVIDIA",
        "role": "Chip Architecture",
        "icon": "\ud83e\udde0",
        "businessImpact": "Can push chip clock speeds 25% higher without thermal throttling, delivering faster AI models.",
        "stockDistinction": "\ud83d\udfe2 Performance Win: Greater compute density per square foot."
      }
    ]
  }
];
  }

  async getAllStocks() { return this._stocks; }
  async getStockBySymbol(symbol) {
    return this._stocks.find(s => s.symbol.toUpperCase() === symbol.toUpperCase()) || null;
  }
  async getGraphTopology() {
    const KID_PROFILES = {
      NVDA: { emoji: "🧠", title: "AI BRAIN", job: "Designs super-smart brains for robots & ChatGPT", friend: "TSMC bakes the chips; Vertiv blows cold air" },
      TSM: { emoji: "🏭", title: "CHIP FACTORY", job: "The giant kitchen that bakes computer chips for everyone", friend: "Builds chips for Nvidia & Apple" },
      VRT: { emoji: "❄️", title: "BIG FAN", job: "Blows icy cold air so hot computer brains don’t melt", friend: "Keeps Nvidia and data centers ice cold" },
      NVT: { emoji: "🧊", title: "ICE LIQUID", job: "Runs chilled water tubes around computers to freeze them", friend: "Cooling partner for AI servers" },
      BE: { emoji: "⚡", title: "POWER BOX", job: "Magic battery box that makes clean electricity on the spot", friend: "Gives power to AI data center buildings" },
      CEG: { emoji: "⚛️", title: "ATOM POWER", job: "Splits tiny atoms to power whole cities with clean nuclear energy", friend: "Sends huge electricity to Microsoft" },
      VST: { emoji: "🔌", title: "POWER GRID", job: "Pumps electricity through giant wires into buildings", friend: "Powers big AI tech campuses" },
      OKLO: { emoji: "☢️", title: "MINI ATOM", job: "Builds small nuclear batteries that fit inside a room", friend: "Future clean energy for AI" },
      NBIS: { emoji: "☁️", title: "AI CLOUD", job: "A playground in the sky where you rent fast computers", friend: "Rents thousands of Nvidia chips" },
      CRWV: { emoji: "🖥️", title: "COMPUTER RENT", job: "Has rooms full of thousands of screens and chips to borrow", friend: "Buys chips from Nvidia" },
      APLD: { emoji: "🏢", title: "DATA HOUSE", job: "Builds giant football-field houses with power plugs for computers", friend: "Hosts computers for cloud companies" },
      AMD: { emoji: "💻", title: "SPEED CHIP", job: "Makes speedy gaming and computer processors", friend: "Competes with Nvidia & Intel" },
      AVGO: { emoji: "🔌", title: "MAGIC CABLES", job: "Makes super-fast cables that let computers talk together", friend: "Connects all data center chips" },
      MRVL: { emoji: "🌐", title: "LIGHT SPEED", job: "Sends computer messages through beams of light", friend: "Helps data centers move data fast" },
      AMKR: { emoji: "📦", title: "CHIP PACKER", job: "Puts tiny microchips safely into protective plastic packages", friend: "Packs chips for TSMC & Nvidia" },
      PLTR: { emoji: "🕵️", title: "SPY AI", job: "Connects the dots like a smart detective to catch bad guys", friend: "Helps governments & hospitals" },
      SOFI: { emoji: "🏦", title: "PHONE BANK", job: "A friendly bank inside your phone with zero paper or lines", friend: "Digital banking for young people" },
      LLY: { emoji: "💊", title: "HEALTH PILL", job: "Makes medicine pills that help sick people get strong and healthy", friend: "World leader in weight-loss medicine" },
      MSFT: { emoji: "🪟", title: "OFFICE TOOLS", job: "Makes Windows, Minecraft, and tools everybody uses for work", friend: "Biggest partner of OpenAI" },
      GOOGL: { emoji: "🔍", title: "MAGIC SEARCH", job: "Answers every question in the universe in less than 1 second", friend: "Builds Gemini and Android" }
    };

    const nodes = this._stocks.map(s => {
      const kid = KID_PROFILES[s.symbol] || { emoji: "🏢", title: s.symbol, job: s.whatItDoes, friend: s.whoBuys };
      return {
        id: s.symbol,
        label: s.symbol,
        name: s.name,
        simpleRole: s.simpleRole,
        layer: s.layer,
        kidEmoji: kid.emoji,
        kidTitle: kid.title,
        kidJob: kid.job,
        kidFriend: kid.friend,
        price: s.price,
        change1D: s.change1D,
        change1M: s.change1M,
        growthYoY: s.growthYoY,
        whatItDoes: s.whatItDoes,
        whoBuys: s.whoBuys,
        size: Math.max(30, Math.min(44, 26 + Math.sqrt(s.marketCapB) * 0.35)),
        color: this._getLayerColor(s.layer)
      };
    });

    const edges = [];
    this._stocks.forEach(s => {
      s.upstream.forEach(up => {
        const target = this._stocks.find(x => x.symbol === up);
        if (target) {
          edges.push({ source: target.symbol, target: s.symbol, type: 'UPSTREAM', color: '#38bdf8' });
        }
      });
      s.downstream.forEach(down => {
        const target = this._stocks.find(x => x.symbol === down);
        if (target) {
          edges.push({ source: s.symbol, target: target.symbol, type: 'DOWNSTREAM', color: '#c084fc' });
        }
      });
      s.competitors.forEach(comp => {
        const target = this._stocks.find(x => x.symbol === comp);
        if (target && s.symbol < target.symbol) {
          edges.push({ source: s.symbol, target: target.symbol, type: 'COMPETITOR', color: '#fb923c' });
        }
      });
    });
    return { nodes, edges };
  }

  getRelationship(source, target) {
    const key1 = `${source}-${target}`;
    const key2 = `${target}-${source}`;
    if (this._relationships[key1]) return this._relationships[key1];
    if (this._relationships[key2]) return this._relationships[key2];

    const sStock = this._stocks.find(s => s.symbol === source);
    const tStock = this._stocks.find(s => s.symbol === target);
    if (!sStock || !tStock) return null;

    let type = 'Supply Chain Relationship';
    let badge = '🔗 Supply Chain';
    if (sStock.competitors.includes(target) || tStock.competitors.includes(source)) {
      type = 'Direct Industry Competition';
      badge = '⚔️ Competitors';
    } else if (sStock.upstream.includes(target) || tStock.downstream.includes(source)) {
      type = 'Commercial Supply Partnership';
      badge = '⬆️ Direct Supplier';
    }

    return {
      source, target,
      sourceRole: sStock.simpleRole,
      targetRole: tStock.simpleRole,
      type, badge,
      direction: `${source} ➔ ${target}`,
      goodsFlow: `Hardware, software, or commercial infrastructure services`,
      cashFlow: `Commercial revenue contracts`,
      whyMatters: `${source} (${sStock.name}) and ${target} (${tStock.name}) operate in tightly synchronized layers of the technology ecosystem. Changes in customer demand at one company directly impact orders at the other.`,
      ifDemandRises: `Increased industry demand accelerates deployment orders between both companies.`,
      ifDemandDrops: `Slowdowns could lead to temporary inventory adjustments.`,
      dependenceLevel: 'Moderate (7/10)'
    };
  }

  _getLayerColor(layer) {
    if (layer.includes('Silicon')) return '#3b82f6';
    if (layer.includes('Cooling')) return '#06b6d4';
    if (layer.includes('Power') || layer.includes('Baseload') || layer.includes('SMR')) return '#10b981';
    if (layer.includes('Foundry') || layer.includes('Packaging')) return '#8b5cf6';
    if (layer.includes('Neocloud') || layer.includes('Campus')) return '#a855f7';
    if (layer.includes('Software') || layer.includes('Defense')) return '#f59e0b';
    if (layer.includes('Fintech')) return '#6366f1';
    if (layer.includes('Health') || layer.includes('Biotech')) return '#ec4899';
    return '#64748b';
  }

  async simulateShock(symbol, shockDelta) {
    const anchor = await this.getStockBySymbol(symbol);
    if (!anchor) return null;
    const affected = [];

    anchor.upstream.forEach(upSym => {
      const up = this._stocks.find(s => s.symbol === upSym);
      if (up) {
        const move = shockDelta * 0.65;
        affected.push({
          symbol: up.symbol,
          role: 'Upstream Supplier',
          relationship: `Supplies critical hardware/power to ${symbol}`,
          projectedMove: Number(move.toFixed(1)),
          reason: shockDelta > 0 ? `Higher ${symbol} demand orders directly expand ${up.symbol} backlog.` : `Demand slowdown at ${symbol} creates inventory build at ${up.symbol}.`
        });
      }
    });

    anchor.downstream.forEach(downSym => {
      const down = this._stocks.find(s => s.symbol === downSym);
      if (down) {
        const move = shockDelta * 0.45;
        affected.push({
          symbol: down.symbol,
          role: 'Downstream Customer',
          relationship: `Purchases compute / systems from ${symbol}`,
          projectedMove: Number(move.toFixed(1)),
          reason: shockDelta > 0 ? `Accelerated deployment schedules for ${down.symbol} applications.` : `Component shortages or delays from ${symbol} drag ${down.symbol} deployment.`
        });
      }
    });

    anchor.competitors.forEach(compSym => {
      const comp = this._stocks.find(s => s.symbol === compSym);
      if (comp) {
        const move = -shockDelta * 0.35;
        affected.push({
          symbol: comp.symbol,
          role: 'Direct Competitor',
          relationship: `Competes in ${anchor.layer}`,
          projectedMove: Number(move.toFixed(1)),
          reason: shockDelta > 0 ? `Market share capture by ${symbol} puts pricing pressure on ${comp.symbol}.` : `Customers seek alternative second-source allocation from ${comp.symbol}.`
        });
      }
    });

    return { shockSymbol: symbol, shockDelta, affected };
  }
}

if (typeof module !== 'undefined') {
  module.exports = { StockRepository };
}

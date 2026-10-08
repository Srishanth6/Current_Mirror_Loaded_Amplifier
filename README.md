# Current-Mirror Loaded Single-Stage CMOS Amplifier

## 📌 Project Overview

Design and performance analysis of a **current-mirror loaded single-stage CMOS amplifier** using a generic **180 nm Level-1 SPICE model**.

The design targets:

- Voltage gain > **25 dB**
- Current-mirror mismatch < **5%**
- Supply voltage: **1.8 V**
- Reference current: **20 µA**
- Mid-rail output bias

This project was completed as part of my **Winter Upskilling Project**, with emphasis on CMOS analog design, MOSFET biasing, small-signal analysis, SPICE simulation, and current-mirror mismatch analysis.

## 🧩 Circuit Topology

The amplifier consists of:

- **M1:** NMOS common-source input transistor
- **M2:** Diode-connected PMOS reference transistor
- **M3:** PMOS current-mirror load
- **IREF:** 20 µA reference current source
- **VDD:** 1.8 V

The low-frequency voltage gain is approximately:

\[
A_v \approx -g_{m1}(r_{o1} \parallel r_{o3})
\]

## ⚙️ Design Parameters

| Device | Role | W/L |
|---|---|---|
| M1 | NMOS common-source | 6 µm / 1.0 µm |
| M2 | PMOS diode reference | 24 µm / 1.5 µm |
| M3 | PMOS active load | 24 µm / 1.5 µm |

### SPICE Model

**NMOS**
- VTO = 0.45 V
- KP = 270 µA/V²
- λ = 0.08 V⁻¹

**PMOS**
- VTO = −0.45 V
- KP = 70 µA/V²
- λ = 0.04 V⁻¹

## 📊 Key Results

| Parameter | Result |
|---|---:|
| Supply | 1.8 V |
| Reference current | 20 µA |
| Input bias | 0.602 V |
| Output bias | ≈ 0.963 V |
| Midband gain | **41.3 dB** |
| Voltage gain | **116.5 V/V** |
| Output resistance | ≈ 439 kΩ |
| Power | ≈ 72 µW |
| Systematic mirror error at 0.9 V | **1.0%** |
| Random mismatch, 3σ | **2.6%** |
| Combined mismatch budget | **4.0%** |
| Specification | **PASS** ✅ |

## 🔬 Current-Mirror Mismatch

The project evaluates both:

1. **Systematic mismatch** caused by unequal drain-source voltages and channel-length modulation.
2. **Random mismatch** caused by threshold-voltage and current-factor variations.

A 500-sample mismatch analysis gives:

- Matched VSD: mean error ≈ 0.12%, σ ≈ 0.95%
- At VOUT = 0.9 V: mean error ≈ 1.15%, σ ≈ 0.96%
- Combined |mean| + 3σ ≈ **4.0%**
- Maximum observed error ≈ **4.3%**

Therefore the design remains within the **5% mismatch requirement**.

## 🧪 Simulation

The project includes an LTspice-compatible SPICE netlist containing:

- DC operating-point analysis
- DC input sweep
- AC frequency response
- Gain measurement

The netlist uses a generic Level-1 MOS model and is intended for educational/design-analysis purposes rather than foundry sign-off.

## 📁 Repository Structure

```
Current_Mirror_Loaded_Amplifier/
├── README.md
├── calculations/
│   └── theoretical_analysis.md
├── results/
│   └── theoretical_vs_simulation.md
├── simulation/
│   └── LTspice/
│       └── cm_cs_amp.net
└── docs/
    └── amplifier_report.pdf
```

## 🚀 Future Work

- Re-run the design using LTspice with the final netlist.
- Replace the Level-1 model with a foundry BSIM model.
- Perform Cadence Virtuoso schematic and layout implementation.
- Implement common-centroid layout for the current mirror.
- Perform post-layout parasitic extraction and re-simulation.
- Compare pre-layout and post-layout gain/mismatch.

## 👨‍💻 Author

**Srishanth Reddy**  
B.Tech Electronics & Communication Engineering  
Chaitanya Bharathi Institute of Technology (CBIT), Hyderabad

---

**Focus areas:** Analog IC Design • CMOS • Current Mirrors • SPICE • LTspice • VLSI • MOSFET Small-Signal Analysis

# Theoretical vs Practical / Simulation Analysis

## Important note

This repository contains two related analyses from the academic work:

1. The dedicated current-mirror-loaded amplifier design uses a generic 180 nm Level-1 SPICE deck and reports a nominal gain of 41.3 dB in ngspice-44.2 (see `results/ngspice/`). Random mismatch has not been simulated yet.
2. Earlier CMOS case-study calculations compared simplified theoretical equations against an LTspice practical result.

## Current results: ngspice-44.2 (reproducible)

Source: `results/ngspice/ngspice_run.log`, generic Level-1 models, simulated 21 Oct 2026.

| Parameter | Simulated |
|---|---:|
| Output bias V(vout) | 0.963 V |
| Gain at 10 Hz | 41.3 dB (116.5 V/V) |
| Output resistance 1/(g_ds1 + g_ds3) | ≈ 439 kΩ |
| Supply power | ≈ 72.3 µW |
| Systematic mirror error at V_OUT = 0.9 V | +1.03 % |

No hand-calculated (theoretical) comparison for this amplifier is included yet.

---

## Interpretation

For the historical case study above (unverified): the DC current agrees closely between theory and simulation, while voltage gain shows a much larger difference because simplified hand calculations do not fully capture the small-signal behaviour and device/model effects represented in SPICE.

For the dedicated current-mirror amplifier in this repository, ngspice-44.2 with the Level-1 models gives 41.3 dB gain at the nominal bias point and a +1.03 % systematic mirror error where V_OUT = 0.9 V. That meets the > 25 dB gain target. The < 5 % mismatch target needs Monte Carlo results that the repository does not yet contain.

## Next validation step

Replace the educational Level-1 models with a foundry BSIM model and repeat:

- DC operating-point analysis
- AC gain
- frequency response
- Monte Carlo mismatch
- post-layout extraction

---

## Historical / unverified (source files unavailable)

> **Not reproduced.** This table comes from an earlier, separate CMOS case study. Its LTspice schematic, netlist and logs are not in this repository, so the values below could not be checked or re-run. They are kept verbatim for reference only and are **not** results for the current amplifier.

### Earlier LTspice Case-Study Comparison

| Parameter | Theoretical | LTspice | Difference / Error |
|---|---:|---:|---:|
| Drain current | 103.48 µA | 103.649 µA | 0.16% |
| Drain voltage | 1.27051 V | 1.35209 V | 6.42% |
| Voltage gain | -170.26 V/V | -42.32 V/V | 75.15% |
| Midband gain | 44.62 dB | 32.53 dB | 12.09 dB |
| Upper cutoff | — | 266.955 kHz | Simulation result |

Percentage error:

Error = |Theoretical - Simulation| / |Theoretical| × 100

For logarithmic gain values, comparing the dB difference is more meaningful than applying percentage error directly to dB.

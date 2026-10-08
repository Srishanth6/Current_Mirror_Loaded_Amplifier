# Theoretical vs Practical / Simulation Analysis

## Important note

This repository contains two related analyses from the academic work:

1. The dedicated current-mirror-loaded amplifier design uses a generic 180 nm Level-1 SPICE deck and reports a nominal gain of 41.3 dB with a mismatch budget below 5%.
2. Earlier CMOS case-study calculations compared simplified theoretical equations against an LTspice practical result.

## Earlier LTspice Case-Study Comparison

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

## Interpretation

The DC current agrees closely between theory and simulation, while voltage gain shows a much larger difference because simplified hand calculations do not fully capture the small-signal behaviour and device/model effects represented in SPICE.

For the dedicated current-mirror amplifier in this repository, the Level-1 design reports 41.3 dB gain at the nominal bias point and a maximum observed mirror error of approximately 4.3%, satisfying the design targets.

## Next validation step

Replace the educational Level-1 models with a foundry BSIM model and repeat:

- DC operating-point analysis
- AC gain
- frequency response
- Monte Carlo mismatch
- post-layout extraction

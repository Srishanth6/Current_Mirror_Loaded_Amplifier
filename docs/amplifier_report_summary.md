# Amplifier Design & Simulation Report

**Project:** Current-Mirror Loaded Single-Stage CMOS Amplifier  
**Process assumption:** Generic 180 nm CMOS, Level-1 SPICE model  
**Supply:** 1.8 V  
**Reference current:** 20 µA

## Specification

| Requirement | Result |
|---|---:|
| Voltage gain > 25 dB | **41.3 dB — PASS** |
| Mirror mismatch < 5% | **4.0% combined |mean| + 3σ — PASS** |
| Output bias near mid-rail | **≈ 0.96 V — PASS** |
| Power | **≈ 72 µW** |

## Topology

The amplifier uses an NMOS common-source input transistor (M1) and a PMOS current-mirror load (M2/M3). The low-frequency gain is approximated by:

Av = −gm1(ro1 || ro3)

The 25 dB target corresponds to approximately 17.8 V/V.

## Device sizing

- M1: NMOS, W/L = 6 µm / 1.0 µm
- M2: PMOS diode reference, W/L = 24 µm / 1.5 µm
- M3: PMOS active load, W/L = 24 µm / 1.5 µm

## Current-mirror mismatch

The analysis separates systematic mismatch from random mismatch.

A 500-sample analysis reports:

- Matched VSD: mean error ≈ 0.12%, σ ≈ 0.95%
- VOUT = 0.9 V: mean error ≈ 1.15%, σ ≈ 0.96%
- Combined |mean| + 3σ ≈ 4.0%
- Maximum observed error ≈ 4.3%

Thus the design remains below the 5% mismatch requirement.

## Conclusion

The Level-1 design satisfies the requested gain and current-mirror mismatch targets. The next engineering step is verification with a foundry BSIM model, followed by Cadence Virtuoso layout, common-centroid matching, parasitic extraction, and post-layout simulation.

> The numerical results are based on the educational Level-1 model and should not be interpreted as fabrication/sign-off results.

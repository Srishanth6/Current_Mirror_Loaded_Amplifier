# Theoretical Analysis

These calculations use the generic 180 nm Level-1 models and device sizes in `simulation/LTspice/cm_cs_amp.net`. The bias point (VIN = 0.602 V, VOUT = 0.963 V, ID = 20.16 µA) is taken from the ngspice operating-point result in `results/ngspice/`. The small-signal numbers below are then written from the Level-1 equations, not from a separate Monte Carlo run.

## 1. Gain

The minimum required gain is:

25 dB = 17.8 V/V

For the current-mirror loaded common-source stage:

Av ≈ -gm1(ro1 || ro3)

Level-1, with channel-length modulation included at the simulated VDS:

- VOV1 = VIN - VTO = 0.602 - 0.45 = 0.152 V
- gm1 = 2·ID / VOV1 ≈ 265.3 µS
- ro1 = (1 + LAMBDA1·VDS1) / (LAMBDA1·ID) ≈ 668 kΩ
- ro3 = (1 + LAMBDA3·|VSD3|) / (LAMBDA3·ID) ≈ 1.282 MΩ
- Rout = ro1 || ro3 ≈ 439 kΩ

Therefore:

|Av| ≈ gm1 · Rout ≈ 116.5 V/V

Av(dB) = 20 log10(116.5) ≈ 41.3 dB

This matches the ngspice AC gain at 10 Hz in `results/ngspice/` and is about 16 dB above the 25 dB specification. It is not an independent hand estimate of ID or VOUT; those came from the simulator.

## 2. Bias point

At VIN = 0.602 V (from `results/ngspice/`):

- VOUT ≈ 0.963 V
- I(M1) ≈ 20.16 µA
- I(M3) ≈ 20.16 µA
- IREF = 20 µA
- Power ≈ 72 µW

The output is close to mid-rail, which leaves headroom for M1 and M3 to stay in saturation.

## 3. Current-mirror mismatch

The intended mirror ratio is I3 / IREF. With matched devices and equal VSD, that ratio is 1.

At VOUT = 0.9 V, channel-length modulation gives a systematic error of about 1.0% in the ngspice DC sweep (the README reports +1.03%).

Random mismatch (VT and β variation) has not been simulated in this repository. There is no Monte Carlo deck and no 500-sample result. The < 5% mismatch requirement cannot be signed off from the files that are here.

## 4. Design conclusion

With the educational Level-1 models, the simulated midband gain is 41.3 dB, which meets the > 25 dB gain target. The systematic mirror error at VOUT = 0.9 V is about 1%. The random-mismatch part of the 5% budget has not been checked.

The design should be re-run with a foundry BSIM model, and with a documented Monte Carlo mismatch test, before any claim of fabrication readiness.

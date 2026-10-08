# Theoretical Analysis

## 1. Gain requirement

The minimum required gain is:

25 dB = 17.8 V/V

For the current-mirror loaded common-source stage:

Av ≈ -gm1(ro1 || ro3)

The Level-1 operating-point solution gives approximately:

- gm1 = 265.2 µS
- ro1 = 668 kΩ
- ro3 = 1.282 MΩ
- Rout ≈ 439 kΩ

Therefore:

|Av| ≈ 116.5 V/V

Av(dB) = 20 log10(116.5) ≈ 41.3 dB

This exceeds the 25 dB specification by approximately 16 dB.

## 2. Bias point

At VIN = 0.602 V:

- VOUT ≈ 0.963 V
- I(M1) ≈ 20.16 µA
- I(M3) ≈ 20.16 µA
- IREF = 20 µA
- Power ≈ 72 µW

The output is close to mid-rail, providing useful output swing while keeping M1 and M3 in saturation.

## 3. Current-mirror mismatch

The mirror ratio is evaluated as:

I3 / IREF

With matched devices and equal VSD, the ratio is approximately 1.000.

At VOUT = 0.9 V, channel-length modulation introduces approximately:

1.0% systematic error.

A 500-sample random mismatch analysis gives approximately:

- Mean error: 0.12% at matched VSD
- Standard deviation: 0.95%
- 3σ random contribution: ≈ 2.6%
- Maximum observed error: 3.2% at matched VSD
- Combined |mean| + 3σ at VOUT = 0.9 V: ≈ 4.0%

Thus the design remains below the 5% mismatch requirement.

## 4. Design conclusion

The Level-1 design satisfies both principal requirements:

- Gain > 25 dB ✅
- Current mismatch < 5% ✅

The design should be re-verified using a foundry BSIM model before any claim of fabrication readiness.

"""Regenerate ngspice_results.png from ac.txt and dc.txt (ngspice wrdata output).
Run from results/ngspice:  python3 plot_results.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ac = [list(map(float, l.split())) for l in open("ac.txt") if l.strip()]
dc = [list(map(float, l.split())) for l in open("dc.txt") if l.strip()]

fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
ax[0].semilogx([r[0] for r in ac], [r[1] for r in ac])
ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("|Av| (dB)")
ax[0].set_title("AC gain (no device caps in Level-1 model → flat)")
ax[0].grid(True, which="both", alpha=.3)
ax[1].plot([r[0] for r in dc], [r[1] for r in dc])
ax[1].axvline(0.602, ls="--", c="gray")
ax[1].set_xlabel("VIN (V)")
ax[1].set_ylabel("VOUT (V)")
ax[1].set_title("DC transfer, VIN 0.4–0.9 V")
ax[1].grid(alpha=.3)
fig.suptitle("cm_cs_amp.net, ngspice-44.2, generic Level-1 models")
plt.tight_layout()
plt.savefig("ngspice_results.png", dpi=110)

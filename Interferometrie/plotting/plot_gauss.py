import numpy as np
import matplotlib.pyplot as plt

dl = np.array([40, 30, 10, 50, 40])
m = np.array([127, 87, 31, 162, 133])
lam = 2 * dl / m * 1000

mean = lam.mean()
s = lam.std(ddof=1)
sem = s / np.sqrt(len(lam))
lam_lit = 632.8

x = np.linspace(mean - 4 * s, mean + 4 * s, 500)
pdf = np.exp(-(x - mean) ** 2 / (2 * s ** 2)) / (s * np.sqrt(2 * np.pi))

fig, ax = plt.subplots(figsize=(6, 4.6))
ax.plot(x, pdf, color="C0", label=rf"Normalverteilung ($\bar\lambda$ = {mean:.1f} nm, $\sigma$ = {s:.1f} nm)")
ax.fill_between(x, pdf, where=(x >= mean - s) & (x <= mean + s), color="C0", alpha=0.2, label=r"$\pm 1\,\sigma$")
ax.axvline(mean, color="C0", ls="--", lw=1)
ax.axvline(lam_lit, color="C3", lw=1.5, label="Literaturwert 632,8 nm")
ax.vlines(lam, 0, 0.08 * pdf.max(), color="k", lw=1.5, label="Einzelmessungen")
ax.set_xlabel(r"Wellenlänge $\lambda$ [nm]")
ax.set_ylabel("Wahrscheinlichkeitsdichte")
ax.set_ylim(bottom=0)
ax.legend(fontsize=8, loc='upper center', bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=False)
fig.tight_layout()
fig.savefig("gauss_laser_plot.png", dpi=300)
print(lam.round(2), round(mean, 2), round(s, 2), round(sem, 2))

import numpy as np
import matplotlib.pyplot as plt

n = np.array([4/5, 3/5, 1/5, 1, 4/5])
m = np.array([127, 87, 31, 162, 133])
lam = 632.8
d = m * lam / (2 * n) / 1000

mean = d.mean()
s = d.std(ddof=1) 
sem = s / np.sqrt(len(d))
d_ref = 50.0

x = np.linspace(mean - 4 * s, mean + 4 * s, 500)
pdf = np.exp(-(x - mean) ** 2 / (2 * s ** 2)) / (s * np.sqrt(2 * np.pi))

fig, ax = plt.subplots(figsize=(6, 4.6))
ax.plot(x, pdf, color="C0", label=rf"Normalverteilung ($\bar d$ = {mean:.1f} µm, $\sigma$ = {s:.1f} µm)")
ax.fill_between(x, pdf, where=(x >= mean - s) & (x <= mean + s), color="C0", alpha=0.2, label=r"$\pm 1\,\sigma$")
ax.axvline(mean, color="C0", ls="--", lw=1)
ax.axvline(d_ref, color="C3", lw=1.5, label="Skalenwert 50 µm")
ax.vlines(d, 0, 0.08 * pdf.max(), color="k", lw=1.5, label="Einzelmessungen")
ax.set_xlabel(r"Verschiebung pro Umdrehung $d$ [µm]")
ax.set_ylabel("Wahrscheinlichkeitsdichte")
ax.set_ylim(bottom=0)
ax.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=False)
fig.tight_layout()
fig.savefig("gauss_laser_plot_2.png", dpi=300)
print(d.round(2), round(mean, 2), round(s, 2), round(sem, 2))
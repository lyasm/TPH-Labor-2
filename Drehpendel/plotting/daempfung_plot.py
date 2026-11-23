import matplotlib.pyplot as plt

I = [0, 0.1016, 0.2052, 0.614, 0.85]
delta = [0.025, 0.0406, 0.1234, 0.370, 0.625]

plt.figure(figsize=(6, 4))
plt.plot(I, delta, "o-")
plt.xlabel(r"Spulenstrom $I$ [A]")
plt.ylabel(r"Abklingkonstante $\delta$ [s$^{-1}$]")
plt.grid(True)
plt.tight_layout()
plt.savefig("daempfung_plot.pdf")
plt.savefig("daempfung_plot.png", dpi=200)

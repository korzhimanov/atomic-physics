"""Глава о водородоподобных атомах: радиальные плотности вероятности."""
import numpy as np

import common as cm

r = np.linspace(0, 30, 3000)   # в единицах боровского радиуса r_B

# нормированные радиальные плотности rho(r) = r^2 R_nl^2 (Z = 1)
RHO = {
    "1s": 4 * r**2 * np.exp(-2 * r),
    "2s": 0.5 * r**2 * (1 - r / 2)**2 * np.exp(-r),
    "3s": 4 / 27 * r**2 * (1 - 2 * r / 3 + 2 * r**2 / 27)**2 * np.exp(-2 * r / 3),
    "2p": 1 / 24 * r**4 * np.exp(-r),
}
STYLE = {
    "1s": dict(color=cm.BLUE),
    "2s": dict(color=cm.ORANGE),
    "3s": dict(color=cm.AQUA),
    "2p": dict(color=cm.VIOLET, ls=(0, (5, 2))),
}
# положения подписей (r, rho)
LABEL = {"1s": (1.35, 0.53), "2s": (6.6, 0.19), "3s": (15.5, 0.105), "2p": (4.6, 0.205)}


def radial():
    fig, ax = cm.subplots(height=2.6)
    for key, rho in RHO.items():
        ax.plot(r, rho, **STYLE[key])
        ax.text(*LABEL[key], key, color=cm.INK, fontsize=9)
    # отметки, о которых идёт речь в тексте
    for x0 in (1, 2, 4):
        ax.axvline(x0, color=cm.MUTED, lw=0.5, ls=":", zorder=0)
    ax.set_xticks([0, 1, 2, 4, 5, 10, 15, 20, 25, 30])
    ax.set_xticklabels(["0", "1", "2", "4", "", "10", "15", "20", "25", "30"])
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 0.57)
    ax.set_xlabel(r"$r/r_B$")
    ax.set_ylabel(r"$\rho(r)$, $1/r_B$")
    cm.save(fig, "hydrogen-radial-functions")


if __name__ == "__main__":
    radial()

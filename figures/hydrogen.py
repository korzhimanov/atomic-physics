"""Глава о водородоподобных атомах: радиальные плотности вероятности."""
import numpy as np
from matplotlib.patches import Rectangle

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


def angular():
    """Сечения угловых распределений |Y_lm(θ)|² плоскостью, проходящей через ось z."""
    fig, axes = cm.subplots(3, 3, width=3.3, height=3.2,
                            gridspec_kw=dict(hspace=0.05, wspace=0.05))
    th = np.linspace(0, 2 * np.pi, 721)
    c, s_ = np.cos(th), np.sin(th)
    Y2 = {(0, 0): np.ones_like(th),
          (1, 0): c**2, (1, 1): s_**2,
          (2, 0): (3 * c**2 - 1) ** 2, (2, 1): s_**2 * c**2, (2, 2): s_**4}
    for l in range(3):
        for m in range(3):
            ax = axes[l, m]
            cm.scheme_axes(ax, (-1.25, 1.25), (-1.25, 1.25))
            if m > l:
                continue
            rho = Y2[(l, m)] / Y2[(l, m)].max()
            ax.plot([0, 0], [-1.2, 1.2], color=cm.MUTED, lw=0.5, ls=(0, (3, 2)))
            ax.fill(rho * s_, rho * c, color=cm.BLUE_LIGHT, lw=0)
            ax.plot(rho * s_, rho * c, color=cm.BLUE, lw=1.0)
            if l == 0:
                ax.text(0.12, 1.15, "$z$", fontsize=8, va="top")
    for l, name in enumerate("spd"):
        axes[l, 0].text(-1.3, 0, f"${name}$\n$(l={l})$", ha="right", va="center", fontsize=8)
    for m, lab in enumerate(["$m=0$", "$|m|=1$", "$|m|=2$"]):
        axes[0, m].set_title(lab, fontsize=8, pad=2)
    cm.save(fig, "hydrogen-angular")


def degeneracy():
    """Схема уровней водорода: уровень n вырожден по l и m, всего n² состояний."""
    fig, ax = cm.subplots(width=3.6, height=2.3)
    ax.axis("off")
    ys = {1: 0.0, 2: 1.6, 3: 2.6, 4: 3.4}       # условное расположение уровней
    energies = {1: "−13,6", 2: "−3,40", 3: "−1,51", 4: "−0,85"}
    w, gap = 0.16, 0.05
    for n, y in ys.items():
        ax.text(-0.35, y, f"$n={n}$", ha="right", va="center", fontsize=8)
        ax.text(-1.25, y, energies[n], ha="right", va="center", fontsize=8, color=cm.INK2)
        ax.plot([0.1, 5.85], [y, y], color=cm.C_LEVEL, lw=0.8, zorder=0)
        for l in range(n):
            x0 = 0.2 + 1.45 * l
            k = 2 * l + 1
            width = k * w + (k - 1) * gap
            xs = x0 + (1.25 - width) / 2
            for j in range(k):
                ax.add_patch(Rectangle((xs + j * (w + gap), y - 0.13), w, 0.26,
                                       fc="white", ec=cm.ORANGE, lw=0.7, zorder=2))
        ax.text(6.15, y, f"${n**2}$", ha="center", va="center", fontsize=8)
    for l, name in enumerate("spdf"):
        ax.text(0.2 + 1.45 * l + 0.625, 4.0, f"${name}$", ha="center", va="bottom", fontsize=9)
    ax.text(6.15, 4.0, "$n^2$", ha="center", va="bottom", fontsize=9)
    ax.text(-1.25, 4.0, "$E$, эВ", ha="right", va="bottom", fontsize=8, color=cm.INK2)
    ax.set_xlim(-2.0, 6.5)
    ax.set_ylim(-0.4, 4.4)
    cm.save(fig, "hydrogen-degeneracy")


if __name__ == "__main__":
    angular()
    degeneracy()
    radial()

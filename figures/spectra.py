"""Спектр атома водорода и диаграмма его уровней энергии."""
import numpy as np
from matplotlib.colors import to_rgb

import common as cm

R_H = 109677.58e2     # постоянная Ридберга для водорода, 1/м
RY_EV = 13.598        # энергия ионизации водорода, эВ

SERIES = [(1, "Лаймана"), (2, "Бальмера"), (3, "Пашена"), (4, "Брэккета"), (5, "Пфунда")]
GREEK = ["α", "β", "γ", "δ"]


def wavelength_nm(n1, n2):
    return 1e9 / (R_H * (1 / n1**2 - 1 / n2**2))


def spectral_rgb(lam):
    """Приближённый цвет монохроматического излучения с длиной волны lam (нм)."""
    if lam < 380 or lam > 750:
        return (0, 0, 0)
    if lam < 440:
        r, g, b = -(lam - 440) / 60, 0.0, 1.0
    elif lam < 490:
        r, g, b = 0.0, (lam - 440) / 50, 1.0
    elif lam < 510:
        r, g, b = 0.0, 1.0, -(lam - 510) / 20
    elif lam < 580:
        r, g, b = (lam - 510) / 70, 1.0, 0.0
    elif lam < 645:
        r, g, b = 1.0, -(lam - 645) / 65, 0.0
    else:
        r, g, b = 1.0, 0.0, 0.0
    # ослабление на краях видимого диапазона
    f = 1.0
    if lam < 420:
        f = 0.3 + 0.7 * (lam - 380) / 40
    elif lam > 700:
        f = 0.3 + 0.7 * (750 - lam) / 50
    return tuple((f * c) ** 0.8 for c in (r, g, b))


def visible():
    """Видимая часть спектра излучения водорода — так её видно в спектроскоп."""
    fig, ax = cm.subplots(height=1.05)
    x0, x1 = 380, 720
    ax.set_xlim(x0, x1)
    ax.set_ylim(0, 1)
    ax.set_facecolor("black")
    for n2 in range(3, 12):
        lam = wavelength_nm(2, n2)
        if lam < x0:
            continue
        w = 2.2 if n2 <= 6 else 1.0
        ax.axvline(lam, color=spectral_rgb(lam), lw=w)
        if n2 <= 6:
            ax.text(lam, 1.04, r"$H_\%s$" % ["alpha", "beta", "gamma", "delta"][n2 - 3],
                    ha="center", va="bottom", fontsize=9, transform=ax.get_xaxis_transform())
    ax.set_yticks([])
    for sp in ("left", "right", "top"):
        ax.spines[sp].set_visible(False)
    ax.set_xticks(range(400, 701, 50))
    ax.set_xlabel(r"$\lambda$, нм")
    cm.save(fig, "spectrum-hydrogen-visible")


def full():
    """Спектральные серии водорода в логарифмическом масштабе длин волн."""
    fig, ax = cm.subplots(height=2.3)
    x0, x1 = 70, 9000
    ax.set_xscale("log")
    ax.set_xlim(x0, x1)
    nrows = len(SERIES)
    ax.set_ylim(-0.6, nrows - 0.15)
    # видимый диапазон
    lam = np.linspace(380, 750, 200)
    for a, b in zip(lam[:-1], lam[1:]):
        c = np.array(spectral_rgb(a))
        ax.axvspan(a, b, color=tuple(0.55 + 0.45 * c), lw=0, zorder=0)
    ax.text(530, nrows - 0.2, "видимый\nдиапазон", ha="center", va="top", fontsize=7,
            color=cm.INK2)
    for row, (n1, name) in enumerate(SERIES):
        y = nrows - 1 - row
        lims = wavelength_nm(n1, np.inf)
        lines = [wavelength_nm(n1, n2) for n2 in range(n1 + 1, n1 + 40)]
        for k, lam in enumerate(lines):
            col = spectral_rgb(lam) if 380 <= lam <= 750 else cm.INK
            if 380 <= lam <= 750:
                col = tuple(0.8 * np.array(col))
            ax.plot([lam, lam], [y - 0.32, y + 0.32], color=col, lw=1.0 if k < 4 else 0.5)
        ax.plot([lims, lims], [y - 0.38, y + 0.38], color=cm.MUTED, lw=0.8, ls=(0, (2, 1.5)))
        ax.text(lines[0] * 1.06, y + 0.12, "α", fontsize=8, ha="left", va="center")
        ax.text(lims / 1.08, y, f"серия {name}", ha="right", va="center", fontsize=8)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xticks([100, 200, 500, 1000, 2000, 5000])
    ax.set_xticklabels(["100", "200", "500", "1000", "2000", "5000"])
    ax.minorticks_off()
    ax.set_xlabel(r"$\lambda$, нм")
    cm.save(fig, "spectrum-hydrogen")


def levels():
    """Диаграмма уровней энергии атома водорода и переходы спектральных серий."""
    fig, ax = cm.subplots(width=3.9, height=3.5)
    E = {n: -RY_EV / n**2 for n in range(1, 9)}
    xl, xr = 0.0, 10.0
    ax.set_xlim(-1.6, xr + 1.0)
    ax.set_ylim(-14.6, 1.6)
    ax.axis("off")
    # непрерывный спектр выше границы ионизации
    ax.axhspan(0, 1.6, xmin=0, xmax=1, color=cm.GRID, lw=0)
    ax.text((xl + xr) / 2, 0.8, "непрерывный спектр (ионизация)", ha="center", va="center",
            fontsize=7.5, color=cm.INK2)
    for n, e in E.items():
        ax.plot([xl, xr], [e, e], color=cm.C_LEVEL if n <= 6 else cm.MUTED,
                lw=1.2 if n <= 6 else 0.5)
        if n <= 4:
            ax.text(xr + 0.15, e, f"$n={n}$", va="center", fontsize=8)
            txt = f"{e:.1f}" if abs(e) > 3 else f"{e:.2f}"
            ax.text(xl - 0.15, e, txt.replace(".", ",").replace("-", "−"),
                    ha="right", va="center", fontsize=8)
    ax.plot([xl, xr], [0, 0], color=cm.INK2, lw=0.8)
    ax.text(xr + 0.15, 0, r"$n=\infty$", va="center", fontsize=8)
    ax.text(xl - 0.15, 0, "0", ha="right", va="center", fontsize=8)
    ax.text(xl - 0.15, 1.15, r"$E$, эВ", ha="right", va="center", fontsize=8)
    # переходы
    groups = [(1, "Лайман", cm.C_PHOTON, 0.5), (2, "Бальмер", cm.BLUE, 4.3), (3, "Пашен", cm.AQUA, 7.6)]
    for n1, name, col, x in groups:
        for k, n2 in enumerate(range(n1 + 1, 7)):
            xx = x + 0.42 * k
            cm.arrow(ax, (xx, E[n2]), (xx, E[n1]), color=col, lw=1.0, ms=6)
        ax.text(x + 0.42 * (5 - n1) / 2, E[n1] - 0.35, f"серия\n{name}a", ha="center",
                va="top", fontsize=7.5, color=cm.INK)
    cm.save(fig, "hydrogen-levels")


if __name__ == "__main__":
    visible()
    full()
    levels()

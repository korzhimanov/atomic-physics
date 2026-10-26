"""Глава 2 и семинар 1: распределение Планка и его предельные случаи."""
import numpy as np
from matplotlib.patches import Wedge, Circle
from scipy.constants import h, c, k

import common as cm


def planck_nu(nu, T):
    return 8 * np.pi * h * nu**3 / c**3 / np.expm1(h * nu / (k * T))


def planck_lambda(lam, T):
    return 8 * np.pi * h * c / lam**5 / np.expm1(h * c / (lam * k * T))


def wien_nu(nu, T):
    return 8 * np.pi * h * nu**3 / c**3 * np.exp(-h * nu / (k * T))


def rj_nu(nu, T):
    return 8 * np.pi * nu**2 / c**3 * k * T


TEMPS = [2000, 3000, 4000, 5000]
VISIBLE_NU = (c / 750e-9, c / 400e-9)   # Гц
VISIBLE_LAM = (0.40, 0.75)              # мкм


def frequency():
    fig, ax = cm.subplots(height=2.7)
    nu = np.linspace(1e11, 1.0e15, 4000)
    ax.axvspan(VISIBLE_NU[0] / 1e14, VISIBLE_NU[1] / 1e14, color=cm.GRID, lw=0, zorder=0)
    ax.text(np.mean(VISIBLE_NU) / 1e14, 11.6, "видимый\nдиапазон", ha="center",
            va="top", color=cm.INK2, fontsize=8)
    for T, col in zip(TEMPS, cm.RAMP_BLUE):
        u = planck_nu(nu, T) * 1e16
        ax.plot(nu / 1e14, u, color=col)
        i = np.argmax(u)
        ax.text(nu[i] / 1e14, u[i] + 0.25, f"{T} К", ha="center", va="bottom",
                color=cm.INK, fontsize=8)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.set_xlabel(r"$\nu$, $10^{14}$ Гц")
    ax.set_ylabel(r"$u_\nu$, $10^{-16}$ Дж$\cdot$с/м$^3$")
    cm.save(fig, "blackbody-planck-frequency")


def wavelength():
    fig, ax = cm.subplots(height=2.7)
    lam = np.linspace(0.05e-6, 3.0e-6, 4000)
    ax.axvspan(*VISIBLE_LAM, color=cm.GRID, lw=0, zorder=0)
    ax.text(np.mean(VISIBLE_LAM), 0.745, "видимый\nдиапазон", ha="center",
            va="top", color=cm.INK2, fontsize=8)
    peaks = []
    for T, col in zip(TEMPS, cm.RAMP_BLUE):
        u = planck_lambda(lam, T) * 1e-6
        ax.plot(lam * 1e6, u, color=col)
        i = np.argmax(u)
        peaks.append((lam[i] * 1e6, u[i]))
        ax.text(lam[i] * 1e6 + 0.08, u[i] + 0.008, f"{T} К", ha="left", va="bottom",
                color=cm.INK, fontsize=8)
    # штриховая линия — положение максимумов (закон смещения Вина)
    b = 2.897771955e-3
    Ts = np.linspace(1800, 5100, 100)
    lm = b / Ts
    ax.plot(lm * 1e6, planck_lambda(lm, Ts) * 1e-6, color=cm.INK2, lw=0.8, ls="--")
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 0.75)
    ax.set_xlabel(r"$\lambda$, мкм")
    ax.set_ylabel(r"$u_\lambda$, Дж/(м$^3\cdot$мкм)")
    cm.save(fig, "blackbody-planck-wavelength")


def comparison():
    T = 4000
    fig, ax = cm.subplots(height=2.7)
    nu = np.linspace(1e11, 1.0e15, 4000)
    x = nu / 1e14
    ax.plot(x, rj_nu(nu, T) * 1e16, color=cm.ORANGE)
    ax.plot(x, wien_nu(nu, T) * 1e16, color=cm.BLUE)
    ax.plot(x, planck_nu(nu, T) * 1e16, color=cm.INK, lw=1.6)
    ax.text(1.12, 5.6, "Рэлей — Джинс", color=cm.INK, ha="left", fontsize=8)
    for name, f, x0, xy in [("Планк", planck_nu, 3.1, (4.3, 5.0)),
                            ("Вин", wien_nu, 1.9, (2.4, 1.3))]:
        y0 = f(x0 * 1e14, T) * 1e16
        ax.annotate(name, xy=(x0, y0), xytext=xy, color=cm.INK, fontsize=8,
                    va="center", arrowprops=dict(arrowstyle="-", color=cm.INK2, lw=0.5,
                                                 shrinkA=1, shrinkB=1))
    # области применимости предельных формул
    nu_T = k * T / h / 1e14   # частота, при которой hν = kT
    ax.axvline(nu_T, color=cm.MUTED, lw=0.6, ls=":")
    ax.text(nu_T + 0.1, 0.25, r"$h\nu = kT$", color=cm.INK2, fontsize=8)
    ax.annotate("", xy=(0.05, 6.4), xytext=(nu_T, 6.4),
                arrowprops=dict(arrowstyle="-|>", color=cm.INK2, lw=0.7))
    ax.text(nu_T / 2, 6.55, r"$h\nu \ll kT$", ha="center", color=cm.INK2, fontsize=8)
    ax.annotate("", xy=(9.9, 6.4), xytext=(nu_T, 6.4),
                arrowprops=dict(arrowstyle="-|>", color=cm.INK2, lw=0.7))
    ax.text(7.5, 6.55, r"$h\nu \gg kT$", ha="center", color=cm.INK2, fontsize=8)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.2)
    ax.set_xlabel(r"$\nu$, $10^{14}$ Гц")
    ax.set_ylabel(r"$u_\nu$, $10^{-16}$ Дж$\cdot$с/м$^3$")
    cm.save(fig, "blackbody-comparison-4000K")


def cavity():
    """Модель абсолютно чёрного тела: полость с малым отверстием."""
    fig, ax = cm.subplots(width=2.4, height=1.9)
    cm.scheme_axes(ax, (-1.35, 2.0), (-1.3, 1.3))
    R, wall, gap = 1.0, 0.16, 9      # радиус, толщина стенки, полуширина отверстия в градусах
    ax.add_patch(Wedge((0, 0), R + wall, gap, 360 - gap, width=wall, color=cm.INK2, lw=0))
    ax.add_patch(Circle((0, 0), R, color=cm.ORANGE_LIGHT, lw=0, zorder=0))
    # луч входит в отверстие и многократно отражается, ослабевая
    pts = [(1.95, -0.27), (np.cos(np.radians(150)), np.sin(np.radians(150)))]
    for ang in (265, 30, 200, 320, 110):
        pts.append((np.cos(np.radians(ang)), np.sin(np.radians(ang))))
    for i, (p, q) in enumerate(zip(pts[:-1], pts[1:])):
        a = 1.0 * 0.62 ** i
        cm.arrow(ax, p, q, color=cm.ORANGE, lw=1.4 * a + 0.3, ms=7, alpha=max(a, 0.25))
    ax.text(1.22, 0.12, "отверстие", fontsize=8, va="bottom")
    ax.text(0, -1.27, r"стенки при температуре $T$", fontsize=8, ha="center", va="top")
    cm.save(fig, "blackbody-cavity")


def modes():
    """Подсчёт мод: узлы решётки в k-пространстве и слой между k и k + dk."""
    fig, ax = cm.subplots(width=2.6, height=2.5)
    step = 1.0
    N = 9
    kk, dk = 6.3, 1.0
    ax.add_patch(Wedge((0, 0), kk + dk, 0, 90, width=dk, color=cm.ORANGE_LIGHT, lw=0))
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            r = np.hypot(i, j) * step
            inside = kk <= r < kk + dk
            ax.plot(i * step, j * step, "o", ms=3.2 if inside else 2.2,
                    color=cm.ORANGE if inside else cm.MUTED, zorder=3)
    cm.arrow(ax, (0, 0), (N + 1.0, 0), color=cm.INK2, lw=0.7, ms=7)
    cm.arrow(ax, (0, 0), (0, N + 1.0), color=cm.INK2, lw=0.7, ms=7)
    ax.text(N + 1.0, -0.25, r"$k_x$", ha="right", va="top", fontsize=10)
    ax.text(-0.2, N + 1.0, r"$k_y$", ha="right", va="top", fontsize=10)
    for i, lab in [(1, r"$\frac{\pi}{l_x}$"), (2, r"$\frac{2\pi}{l_x}$")]:
        ax.plot([i, i], [-0.12, 0.12], color=cm.INK2, lw=0.7)
        ax.text(i, -0.25, lab, ha="center", va="top", fontsize=8)
    for j, lab in [(1, r"$\frac{\pi}{l_y}$"), (2, r"$\frac{2\pi}{l_y}$")]:
        ax.plot([-0.12, 0.12], [j, j], color=cm.INK2, lw=0.7)
        ax.text(-0.25, j, lab, ha="right", va="center", fontsize=8)
    t = np.radians(68)
    cm.arrow(ax, (0, 0), (kk * np.cos(t), kk * np.sin(t)), color=cm.INK, lw=0.8, ms=7)
    ax.text(0.5 * kk * np.cos(t) - 0.15, 0.5 * kk * np.sin(t) + 0.2, r"$k$", fontsize=10,
            ha="right")
    t2 = np.radians(20)
    p1 = (kk * np.cos(t2), kk * np.sin(t2))
    p2 = ((kk + dk) * np.cos(t2), (kk + dk) * np.sin(t2))
    cm.arrow(ax, p1, p2, color=cm.INK, lw=0.8, ms=5, style="<|-|>")
    ax.text(p2[0] + 0.1, p2[1] - 0.1, r"$dk$", fontsize=10, va="top")
    ax.set_xlim(-1.3, N + 1.2)
    ax.set_ylim(-1.3, N + 1.2)
    ax.set_aspect("equal")
    ax.axis("off")
    cm.save(fig, "blackbody-modes")


if __name__ == "__main__":
    cavity()
    modes()
    frequency()
    wavelength()
    comparison()

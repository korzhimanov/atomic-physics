"""Рисунки к семинарам."""
import numpy as np

import common as cm


def infinite_well():
    """Семинар 4: уровни и волновые функции в бесконечно глубокой яме."""
    fig, ax = cm.subplots(width=2.6, height=2.5)
    a = 1.0
    x = np.linspace(0, a, 400)
    for n in (1, 2, 3):
        En = n**2
        psi = np.sin(np.pi * n * x / a)
        ax.plot([0, a], [En, En], color=cm.C_LEVEL, lw=1.0)
        ax.plot(x, En + 0.8 * psi, color=cm.C_PSI, lw=1.1)
        ax.text(a + 0.06, En, f"$E_{n}$", va="center", fontsize=8)
    ax.plot([0, 0], [0, 11], color=cm.C_POT, lw=1.6)
    ax.plot([a, a], [0, 11], color=cm.C_POT, lw=1.6)
    ax.plot([0, a], [0, 0], color=cm.C_POT, lw=1.0)
    ax.text(0, -0.3, "$0$", ha="center", va="top", fontsize=8)
    ax.text(a, -0.3, "$a$", ha="center", va="top", fontsize=8)
    ax.text(-0.06, 10.4, r"$U = \infty$", ha="right", va="center", fontsize=8)
    ax.text(a + 0.06, 10.4, r"$U = \infty$", ha="left", va="center", fontsize=8)
    ax.set_xlim(-0.45, 1.45)
    ax.set_ylim(-1.2, 11.2)
    ax.axis("off")
    cm.save(fig, "infinite-well")


def spherical_well():
    """Семинар 4: графическое решение уравнения для сферической прямоугольной ямы.

    В переменных ξ = ka, η = κa условие сшивки имеет вид η = −ξ ctg ξ, а
    ξ² + η² = ρ², где ρ = √(2mU₀)a/ħ. Уровни — точки пересечения кривых."""
    fig, ax = cm.subplots(width=3.4, height=2.5)
    for k in range(3):
        xi = np.linspace((k + 0.5) * np.pi + 1e-3, (k + 1) * np.pi - 0.03, 400)
        ax.plot(xi, -xi / np.tan(xi), color=cm.BLUE, lw=1.3)
    t = np.linspace(0, np.pi / 2, 200)
    for rho, col in [(1.2, cm.MUTED), (4.0, cm.ORANGE), (7.0, cm.ORANGE)]:
        ax.plot(rho * np.cos(t), rho * np.sin(t), color=col, lw=0.9, ls=(0, (4, 2)))
        ax.text(rho * np.cos(np.radians(78)) + 0.1, rho * np.sin(np.radians(78)),
                f"$\\rho = {rho:g}$".replace(".", "{,}"), fontsize=7.5, va="bottom")
        # точки пересечения
        for k in range(3):
            lo, hi = (k + 0.5) * np.pi + 1e-6, min((k + 1) * np.pi - 1e-6, rho)
            if lo >= hi:
                continue
            f = lambda x: x**2 * (1 + 1 / np.tan(x) ** 2) - rho**2
            from scipy.optimize import brentq
            try:
                xs = brentq(f, lo, hi - 1e-9)
            except ValueError:
                continue
            ax.plot(xs, -xs / np.tan(xs), "o", ms=3.5, color=cm.INK, zorder=4)
    for k in range(1, 4):
        ax.axvline(k * np.pi - np.pi / 2, color=cm.GRID, lw=0.6, zorder=0)
    ax.set_xticks([np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi, 5 * np.pi / 2, 3 * np.pi])
    ax.set_xticklabels([r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$",
                        r"$\frac{5\pi}{2}$", r"$3\pi$"])
    ax.set_xlim(0, 9.6)
    ax.set_ylim(0, 7.6)
    ax.set_xlabel(r"$\xi = ka$")
    ax.set_ylabel(r"$\eta = \kappa a$")
    ax.text(5.3, 0.3, r"$\eta = -\xi\,\mathrm{ctg}\,\xi$", fontsize=8, color=cm.INK)
    cm.save(fig, "spherical-well-solution")


if __name__ == "__main__":
    infinite_well()
    spherical_well()

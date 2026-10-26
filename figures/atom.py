"""Схемы атома: модели Томсона и Резерфорда, электрон на орбите в теории Бора,
стоячая волна де Бройля на орбите."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Arc

import common as cm

ELEV = np.radians(28)   # угол, под которым мы смотрим на плоскость орбиты


def proj(x, y, z):
    """Проекция точки (x, y, z) на плоскость рисунка (вид спереди и сверху)."""
    return np.asarray(x), np.asarray(z) * np.cos(ELEV) + np.asarray(y) * np.sin(ELEV)


def charge(ax, xy, r, color, sign, fs=9):
    ax.add_patch(Circle(xy, r, color=color, zorder=5))
    ax.text(*xy, sign, color="white", ha="center", va="center_baseline",
            fontsize=fs, fontweight="bold", zorder=6)


def bohr_orbit():
    """Раздел «Теория Бора водородоподобных атомов»: обозначения вывода."""
    fig, ax = cm.subplots(width=3.0, height=2.5)
    cm.scheme_axes(ax, (-2.1, 2.4), (-1.35, 2.4))
    R = 1.6
    phi = np.linspace(0, 2 * np.pi, 400)
    X, Y = proj(R * np.cos(phi), R * np.sin(phi), 0)
    ax.plot(X, Y, color=cm.INK2, lw=0.8)

    # ось и момент импульса
    cm.arrow(ax, (0, 0), proj(0, 0, 2.2), color=cm.INK, lw=1.2)
    ax.text(*proj(0.12, 0, 2.15), r"$\vec L$", fontsize=11, va="top")
    # угловая скорость: дуга вокруг оси
    rho, z0 = 0.35, 1.55
    t = np.radians(np.linspace(-200, 60, 100))
    ax.plot(*proj(rho * np.cos(t), rho * np.sin(t), z0), color=cm.INK2, lw=0.8)
    xe, ye = proj(rho * np.cos(t[-1]), rho * np.sin(t[-1]), z0)
    xp, yp = proj(rho * np.cos(t[-3]), rho * np.sin(t[-3]), z0)
    cm.arrow(ax, (xp, yp), (xe, ye), color=cm.INK2, lw=0.8, ms=7)
    ax.text(*proj(-0.55, 0, z0 + 0.05), r"$\omega$", fontsize=11, ha="right")

    # электрон на орбите
    pe = -np.radians(38)
    ex, ey = proj(R * np.cos(pe), R * np.sin(pe), 0)
    d = np.hypot(ex, ey)
    ux, uy = ex / d, ey / d            # единичный вектор от ядра к электрону
    nx, ny = -uy, ux                   # нормаль к радиусу (вверх)
    # радиус
    ax.plot([0, ex], [0, ey], color=cm.INK2, lw=0.8, ls=(0, (4, 2)))
    ax.text(0.42 * ex + 0.13 * nx, 0.42 * ey + 0.13 * ny, r"$r$", fontsize=11,
            ha="center", va="center")
    # сила — к ядру, чуть ниже линии радиуса
    off = -0.09
    cm.arrow(ax, (ex + off * nx - 0.12 * ux, ey + off * ny - 0.12 * uy),
             (ex + off * nx - 0.85 * ux, ey + off * ny - 0.85 * uy), color=cm.ORANGE, lw=1.3)
    ax.text(ex - 0.55 * ux - 0.25 * nx, ey - 0.55 * uy - 0.25 * ny, r"$\vec F$", fontsize=11,
            ha="center", va="center")
    # скорость — по касательной
    vx, vy = proj(-np.sin(pe), np.cos(pe), 0)
    nrm = np.hypot(vx, vy)
    cm.arrow(ax, (ex, ey), (ex + 0.95 * vx / nrm, ey + 0.95 * vy / nrm), color=cm.BLUE, lw=1.3)
    ax.text(ex + 0.95 * vx / nrm + 0.05, ey + 0.95 * vy / nrm, r"$\vec v$", fontsize=11, va="bottom")

    charge(ax, (0, 0), 0.17, cm.C_NUCLEUS, "+")
    ax.text(-0.22, -0.06, r"$+Ze$", ha="right", va="top", fontsize=10)
    charge(ax, (ex, ey), 0.11, cm.C_ELECTRON, "−", fs=8)
    ax.text(ex + 0.1, ey - 0.14, r"$-e,\ m_e$", ha="left", va="top", fontsize=10)
    cm.save(fig, "atom-bohr-orbit")


def thomson():
    fig, ax = cm.subplots(width=1.9, height=1.9)
    cm.scheme_axes(ax, (-1.1, 1.1), (-1.1, 1.1))
    ax.add_patch(Circle((0, 0), 1.0, color=cm.ORANGE_LIGHT, ec=cm.ORANGE, lw=1.0))
    rng = np.random.default_rng(3)
    # знаки «+» — равномерно распределённый положительный заряд
    for _ in range(40):
        r, a = np.sqrt(rng.uniform(0, 0.85)), rng.uniform(0, 2 * np.pi)
        ax.text(r * np.cos(a), r * np.sin(a), "+", color=cm.ORANGE, ha="center",
                va="center_baseline", fontsize=7)
    # электроны, вкраплённые в положительный заряд
    for r, a in [(0, 0), (0.55, 0.3), (0.55, 1.9), (0.55, 3.5), (0.55, 5.1),
                 (0.82, 1.1), (0.82, 2.7), (0.82, 4.3), (0.82, 5.9)]:
        charge(ax, (r * np.cos(a), r * np.sin(a)), 0.09, cm.C_ELECTRON, "−", fs=7)
    cm.save(fig, "atom-model-thomson")


def rutherford():
    fig, ax = cm.subplots(width=1.9, height=1.9)
    cm.scheme_axes(ax, (-1.1, 1.1), (-1.1, 1.1))
    for k, ang in enumerate((0, 60, 120)):
        ax.add_patch(Ellipse((0, 0), 2.0, 0.7, angle=ang, fill=False, ec=cm.INK2, lw=0.7))
        t = np.radians([40, 230][k % 2] + 25 * k)
        x, y = np.cos(t), 0.35 * np.sin(t)
        c, s = np.cos(np.radians(ang)), np.sin(np.radians(ang))
        charge(ax, (x * c - y * s, x * s + y * c), 0.08, cm.C_ELECTRON, "−", fs=6)
    charge(ax, (0, 0), 0.07, cm.C_NUCLEUS, "", fs=6)
    cm.save(fig, "atom-model-rutherford")


def standing_wave():
    """Стоячая волна де Бройля на круговой орбите: n = 4 и нецелое число длин волн."""
    fig, axes = cm.subplots(1, 2, width=3.6, height=1.9)
    R, A = 1.0, 0.16
    for ax, n, title in [(axes[0], 4, r"$2\pi r = 4\lambda$"),
                         (axes[1], 3.5, r"$2\pi r = 3{,}5\lambda$")]:
        cm.scheme_axes(ax, (-1.35, 1.35), (-1.45, 1.3))
        phi = np.linspace(0, 2 * np.pi, 500)
        ax.plot(R * np.cos(phi), R * np.sin(phi), color=cm.MUTED, lw=0.6, ls=(0, (3, 2)))
        rr = R + A * np.cos(n * phi)
        ax.plot(rr * np.cos(phi), rr * np.sin(phi), color=cm.C_PSI, lw=1.3)
        charge(ax, (0, 0), 0.08, cm.C_NUCLEUS, "", fs=6)
        ax.text(0, -1.42, title, ha="center", va="bottom", fontsize=9)
    # разрыв волны после обхода орбиты при нецелом числе длин волн
    axes[1].plot([R - A, R + A], [0, 0], color=cm.RED, lw=1.4, zorder=4)
    cm.save(fig, "de-broglie-orbit")


def coulomb():
    """Раздел «Электрон в кулоновском потенциале»: обозначения и потенциал."""
    import angular
    fig, (ax, ax2) = cm.subplots(1, 2, width=4.78, height=2.3,
                                 gridspec_kw=dict(width_ratios=[1, 1.25], wspace=0.15))
    cm.scheme_axes(ax, (-1.25, 2.4), (-1.0, 2.35))
    p = angular.spherical_scheme(ax, r=1.6, labels=True)
    charge(ax, (0, 0), 0.09, cm.C_NUCLEUS, "", fs=6)
    ax.text(-0.12, 0.1, "$+Ze$", ha="right", va="bottom", fontsize=9)
    charge(ax, p, 0.1, cm.C_ELECTRON, "−", fs=7)
    ax.text(p[0] + 0.12, p[1] + 0.05, "$-e$", ha="left", va="bottom", fontsize=9)
    # кулоновский потенциал (Z = 1): U = -2 Ry · r_B / r, уровни E_n = -Ry/n^2
    r = np.linspace(0.08, 20, 800)
    U = -2 / r
    ax2.axhspan(0, 0.35, color=cm.GRID, lw=0)
    ax2.text(19.5, 0.17, "$E > 0$: электрон свободен", ha="right", va="center",
             fontsize=7, color=cm.INK2)
    for n in (1, 2, 3):
        E = -1 / n**2
        rt = 2 * n**2                      # классическая точка поворота
        ax2.plot([0, rt], [E, E], color=cm.C_LEVEL, lw=1.2)
        ax2.plot([rt, 20], [E, E], color=cm.C_LEVEL, lw=0.5, ls=(0, (3, 2)))
        ax2.text(20.3, E, f"$E_{n}$", va="center", fontsize=8)
    ax2.plot(r, U, color=cm.C_POT, lw=1.4)
    ax2.text(3.2, -0.88, r"$U(r) = -\dfrac{Ze^2}{r}$", fontsize=9)
    ax2.axhline(0, color=cm.INK2, lw=0.6)
    ax2.set_xlim(0, 21.5)
    ax2.set_ylim(-1.35, 0.35)
    ax2.set_xticks([0, 2, 8, 18])
    ax2.set_xlabel(r"$r/r_B$")
    ax2.set_yticks([-1, -0.25, 0])
    ax2.set_yticklabels([r"$-\mathrm{Ry}$", r"$-\mathrm{Ry}/4$", "0"])
    ax2.spines["bottom"].set_visible(False)
    ax2.tick_params(axis="x", length=0)
    ax2.set_ylabel("$E$")
    cm.save(fig, "coulomb-potential")


if __name__ == "__main__":
    coulomb()
    bohr_orbit()
    thomson()
    rutherford()
    standing_wave()

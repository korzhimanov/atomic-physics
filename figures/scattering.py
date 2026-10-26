"""Глава «Теория атома Бора»: рассеяние альфа-частиц и установка Гейгера — Марсдена."""
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib.patches import Circle, Rectangle, Arc, FancyBboxPatch

import common as cm


def trajectory(b, kappa, x0=-3.2, rmax=3.4):
    """Траектория частицы с единичной начальной скоростью в поле отталкивающего
    кулоновского центра в начале координат: a = kappa * r / |r|^3."""
    def rhs(t, s):
        x, y, vx, vy = s
        r3 = (x * x + y * y) ** 1.5
        return [vx, vy, kappa * x / r3, kappa * y / r3]

    def leave(t, s):
        return np.hypot(s[0], s[1]) - rmax
    leave.terminal = True
    leave.direction = 1
    sol = solve_ivp(rhs, (0, 20), [x0, b, 1.0, 0.0], events=leave, max_step=0.01,
                    rtol=1e-9, atol=1e-11)
    return sol.y[0], sol.y[1]


def rutherford_scattering():
    fig, (a1, a2) = cm.subplots(1, 2, width=4.78, height=2.1, gridspec_kw=dict(wspace=0.08))
    for ax in (a1, a2):
        cm.scheme_axes(ax, (-3.2, 3.2), (-3.0, 2.75))
    bs = [-1.5, -1.0, -0.6, -0.3, -0.12, -0.03, 0.03, 0.12, 0.3, 0.6, 1.0, 1.5]
    # атом Томсона: положительный заряд размазан по шару, отклонения очень малы
    a1.add_patch(Circle((0, 0), 1.6, color=cm.ORANGE_LIGHT, ec=cm.ORANGE, lw=0.8))
    for b in bs:
        a1.plot([-3.1, 3.1], [b, b], color=cm.BLUE, lw=0.8)
        cm.arrow(a1, (2.7, b), (3.1, b), color=cm.BLUE, lw=0.8, ms=5)
    a1.text(0, -2.95, "модель Томсона", ha="center", va="bottom", fontsize=8)
    # атом Резерфорда: точечное ядро, траектории — гиперболы
    a2.add_patch(Circle((0, 0), 1.6, fill=False, ec=cm.MUTED, lw=0.6, ls=(0, (3, 2))))
    for b in bs:
        x, y = trajectory(b, kappa=0.18, rmax=2.75)
        a2.plot(x, y, color=cm.BLUE, lw=0.8)
        cm.arrow(a2, (x[-8], y[-8]), (x[-1], y[-1]), color=cm.BLUE, lw=0.8, ms=5)
    a2.add_patch(Circle((0, 0), 0.07, color=cm.C_NUCLEUS, zorder=5))
    a2.text(0, -2.95, "модель Резерфорда", ha="center", va="bottom", fontsize=8)
    cm.save(fig, "rutherford-scattering")


def geiger_marsden_1913():
    """Схема установки Гейгера — Марсдена 1913 года (вид сверху)."""
    fig, ax = cm.subplots(width=3.0, height=2.5)
    cm.scheme_axes(ax, (-2.9, 2.4), (-1.85, 2.6))
    ax.add_patch(Circle((0, 0), 1.75, fill=False, ec=cm.INK2, lw=0.8))
    ax.text(-1.45, -1.25, "откачиваемая\nкамера", ha="right", va="top", fontsize=7, color=cm.INK2)
    # источник и диафрагма
    ax.add_patch(Rectangle((-2.75, -0.18), 0.5, 0.36, color=cm.INK2))
    ax.text(-2.5, 0.25, "источник", ha="center", va="bottom", fontsize=7)
    for y0 in (-0.35, 0.08):
        ax.add_patch(Rectangle((-1.3, y0), 0.08, 0.27, color=cm.INK))
    ax.text(-1.26, -0.42, "диафрагма", ha="center", va="top", fontsize=7)
    ax.plot([-2.25, 0], [0, 0], color=cm.C_PHOTON, lw=1.0)
    cm.arrow(ax, (-0.55, 0), (-0.06, 0), color=cm.C_PHOTON, lw=1.0, ms=6)
    ax.text(-1.85, 0.08, r"$\alpha$", fontsize=9, va="bottom", color=cm.INK)
    # фольга
    ax.plot([0, 0], [-0.3, 0.3], color=cm.ORANGE, lw=2.2)
    ax.text(0.08, -0.32, "фольга", va="top", fontsize=7)
    # экран и микроскоп на поворотном рычаге
    phi = np.radians(55)
    ux, uy = np.cos(phi), np.sin(phi)
    ax.plot([0, 1.45 * ux], [0, 1.45 * uy], color=cm.C_PHOTON, lw=1.0)
    cm.arrow(ax, (1.0 * ux, 1.0 * uy), (1.45 * ux, 1.45 * uy), color=cm.C_PHOTON, lw=1.0, ms=6)
    nx, ny = -uy, ux
    s0 = np.array([1.55 * ux, 1.55 * uy])
    ax.plot([s0[0] - 0.3 * nx, s0[0] + 0.3 * nx], [s0[1] - 0.3 * ny, s0[1] + 0.3 * ny],
            color=cm.AQUA, lw=2.4)
    ax.text(s0[0] + 0.32 * nx - 0.05, s0[1] + 0.32 * ny, "экран", ha="right", va="bottom", fontsize=7)
    m0, m1 = s0 + 0.08 * np.array([ux, uy]), s0 + 0.95 * np.array([ux, uy])
    ax.plot([m0[0], m1[0]], [m0[1], m1[1]], color=cm.INK2, lw=6, solid_capstyle="butt")
    ax.text(m1[0] + 0.1, m1[1] - 0.05, "микроскоп", ha="left", va="top", fontsize=7)
    ax.plot([0, 1.4], [0, 0], color=cm.MUTED, lw=0.5, ls=(0, (3, 2)))
    ax.add_patch(Arc((0, 0), 1.3, 1.3, theta1=0, theta2=np.degrees(phi), color=cm.INK, lw=0.7))
    ax.text(0.72, 0.38, r"$\varphi$", fontsize=10)
    # поворот рычага
    ax.add_patch(Arc((0, 0), 4.5, 4.5, theta1=35, theta2=75, color=cm.INK2, lw=0.7))
    t = np.radians(75)
    cm.arrow(ax, (2.25 * np.cos(np.radians(73)), 2.25 * np.sin(np.radians(73))),
             (2.25 * np.cos(t), 2.25 * np.sin(t)), color=cm.INK2, lw=0.7, ms=6)
    cm.save(fig, "geiger-marsden-1913")


if __name__ == "__main__":
    rutherford_scattering()
    geiger_marsden_1913()

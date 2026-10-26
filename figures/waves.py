"""Глава «Волновые свойства частиц»: волновой пакет, дифракция электронов,
микроскоп Гейзенберга."""
import numpy as np
from matplotlib.patches import Ellipse, Arc, Circle, Rectangle

import common as cm


def wave_packet():
    """Чем уже пакет в координатном пространстве, тем шире его спектр."""
    fig, axes = cm.subplots(2, 2, width=4.78, height=2.6,
                            gridspec_kw=dict(width_ratios=[1.6, 1], hspace=0.35, wspace=0.12))
    x = np.linspace(-7, 7, 1500)
    k = np.linspace(0, 12, 800)
    k0 = 6.0
    for row, sx in enumerate((0.7, 1.9)):
        ax, axk = axes[row]
        env = np.exp(-x**2 / (2 * sx**2))
        ax.plot(x, env * np.cos(k0 * x), color=cm.C_PSI, lw=0.9)
        ax.plot(x, env, color=cm.INK2, lw=0.7, ls=(0, (3, 2)))
        ax.plot(x, -env, color=cm.INK2, lw=0.7, ls=(0, (3, 2)))
        hw = sx * np.sqrt(2 * np.log(2))      # полуширина на половине высоты
        cm.arrow(ax, (-hw, -1.2), (hw, -1.2), color=cm.INK, lw=0.7, ms=5, style="<|-|>")
        ax.text(hw + 0.2, -1.2, r"$\Delta x$", va="center", fontsize=9)
        cm.axis_arrows(ax, r"$x$", r"$\mathrm{Re}\,\Psi$", xlim=(-7.2, 7.4), ylim=(-1.15, 1.45))
        ax.set_xlim(-7.6, 7.6)
        ax.set_ylim(-1.35, 1.5)
        sk = 1 / sx
        spec = np.exp(-(k - k0)**2 / (2 * sk**2))
        axk.fill_between(k, spec, color=cm.ORANGE_LIGHT, lw=0)
        axk.plot(k, spec, color=cm.ORANGE, lw=1.1)
        hk = sk * np.sqrt(2 * np.log(2))
        cm.arrow(axk, (k0 - hk, 0.5), (k0 + hk, 0.5), color=cm.INK, lw=0.7, ms=5, style="<|-|>")
        axk.text(k0, 0.56, r"$\Delta k$", ha="center", va="bottom", fontsize=9)
        cm.axis_arrows(axk, r"$k$", r"$|c(k)|$", xlim=(0, 12.4), ylim=(0, 1.45))
        axk.plot([k0, k0], [-0.05, 0.05], color=cm.INK2, lw=0.7)
        axk.text(k0, -0.07, r"$k_0$", ha="center", va="top", fontsize=8)
        axk.set_xlim(-0.6, 12.6)
        axk.set_ylim(-0.25, 1.5)
    cm.save(fig, "wave-packet")


def bragg():
    """Отражение от двух соседних атомных плоскостей; разность хода 2d sin θ."""
    fig, ax = cm.subplots(width=3.3, height=2.0)
    cm.scheme_axes(ax, (-3.4, 3.4), (-2.2, 1.9))
    d = 1.0
    th = np.radians(32)
    for j in range(3):
        y = -j * d
        ax.plot([-3.3, 3.3], [y, y], color=cm.MUTED, lw=0.5, zorder=0)
        for xx in np.arange(-3.0, 3.01, 0.75):
            ax.add_patch(Circle((xx, y), 0.07, color=cm.INK2, zorder=1))
    ux, uy = np.cos(th), np.sin(th)
    L = 2.6
    # точки отражения: на первой плоскости в 0, на второй — под ней со сдвигом,
    # чтобы падающие лучи были параллельны
    A = np.array([0.0, 0.0])
    B = np.array([d / np.tan(th), -d]) - np.array([d / np.tan(th), 0])  # (0, -d)
    for P in (A, B):
        start = P - L * np.array([ux, -uy]) * (1 if P is A else 1.0) - (0 if P is A else 0)
        cm.arrow(ax, P + np.array([-L * ux, L * uy]) + (np.array([0, 0]) if P is A else np.array([-d / np.tan(th) * 0, 0])),
                 P, color=cm.BLUE, lw=1.0, ms=6)
        cm.arrow(ax, P, P + np.array([L * ux, L * uy]), color=cm.BLUE, lw=1.0, ms=6)
    # перпендикуляры из точки A на лучи, отражённые от второй плоскости
    n_in = np.array([ux, -uy])         # направление падающего луча
    n_out = np.array([ux, uy])         # направление отражённого луча
    # проекции: точки C и D на луче через B
    C = B - n_in * np.dot(B - A, n_in)
    D = B + n_out * np.dot(A - B, n_out)
    ax.plot(*zip(A, C), color=cm.INK2, lw=0.6, ls=(0, (2, 1.5)))
    ax.plot(*zip(A, D), color=cm.INK2, lw=0.6, ls=(0, (2, 1.5)))
    ax.plot(*zip(C, B), color=cm.ORANGE, lw=2.2, solid_capstyle="butt")
    ax.plot(*zip(B, D), color=cm.ORANGE, lw=2.2, solid_capstyle="butt")
    ax.text(*(0.5 * (B + D) + np.array([0.12, -0.12])), r"$d\sin\theta$", fontsize=8,
            ha="left", va="top", color=cm.INK)
    # угол скольжения
    ax.add_patch(Arc(A, 1.6, 1.6, theta1=0, theta2=np.degrees(th), color=cm.INK, lw=0.7))
    ax.text(0.95, 0.22, r"$\theta$", fontsize=10, va="center")
    # межплоскостное расстояние
    cm.arrow(ax, (2.7, 0), (2.7, -d), color=cm.INK, lw=0.7, ms=5, style="<|-|>")
    ax.text(2.82, -d / 2, r"$d$", fontsize=10, va="center")
    cm.save(fig, "bragg-diffraction")


def microscope():
    """Мысленный эксперимент Гейзенберга: γ-микроскоп."""
    fig, ax = cm.subplots(width=2.6, height=2.6)
    cm.scheme_axes(ax, (-2.3, 2.3), (-0.9, 3.7))
    H, half = 2.6, 1.0                 # высота объектива и его полуширина
    eps2 = np.arctan(half / H)          # половина угла раствора
    ax.add_patch(Ellipse((0, H), 2 * half + 0.3, 0.32, fc=cm.BLUE_LIGHT, ec=cm.BLUE_DARK, lw=0.8))
    ax.text(half + 0.3, H, "объектив", va="center", fontsize=8)
    for sgn in (-1, 1):
        ax.plot([0, sgn * half], [0, H], color=cm.C_PHOTON, lw=0.9)
    ax.plot([0, 0], [0, H], color=cm.MUTED, lw=0.5, ls=(0, (3, 2)))
    ax.add_patch(Arc((0, 0), 2.6, 2.6, theta1=90 - np.degrees(eps2), theta2=90 + np.degrees(eps2),
                     color=cm.INK, lw=0.7))
    ax.text(0, 1.42, r"$\varepsilon$", ha="center", va="bottom", fontsize=10)
    # падающий γ-квант — волнистая стрелка слева
    xs = np.linspace(-2.2, -0.35, 300)
    ax.plot(xs, 0.09 * np.sin(2 * np.pi * (xs + 2.2) / 0.28), color=cm.C_PHOTON, lw=0.9)
    cm.arrow(ax, (-0.42, 0), (-0.18, 0), color=cm.C_PHOTON, lw=0.9, ms=6)
    ax.text(-1.3, 0.2, r"$\gamma$-квант, $\lambda$", ha="center", va="bottom", fontsize=8)
    ax.add_patch(Circle((0, 0), 0.09, color=cm.C_ELECTRON, zorder=5))
    ax.text(0.15, -0.15, "электрон", va="top", fontsize=8)
    # неопределённость координаты
    cm.arrow(ax, (-0.55, -0.55), (0.55, -0.55), color=cm.INK, lw=0.7, ms=5, style="<|-|>")
    ax.text(-0.65, -0.55, r"$\Delta x$", ha="right", va="center", fontsize=9)
    cm.save(fig, "heisenberg-microscope")


def davisson_polar():
    """Качественная полярная диаграмма рассеяния электронов (54 В)."""
    fig, ax = cm.subplots(width=2.6, height=1.9)
    cm.scheme_axes(ax, (-0.9, 1.6), (-0.35, 1.9))
    ax.add_patch(Rectangle((-0.85, -0.3), 2.4, 0.3, color=cm.GRID, lw=0))
    ax.text(-0.75, -0.15, "кристалл никеля", va="center", fontsize=7, color=cm.INK2)
    cm.arrow(ax, (0, 1.85), (0, 0.02), color=cm.INK, lw=0.9, ms=6)
    ax.text(0.07, 1.8, "пучок электронов,\n54 эВ", va="top", fontsize=7)
    phi = np.radians(np.linspace(0, 90, 400))     # угол от направления назад, к пучку
    I = 0.75 * np.cos(phi) ** 0.6 + 0.55 * np.exp(-((phi - np.radians(50)) / np.radians(5)) ** 2)
    xx, yy = I * np.sin(phi), I * np.cos(phi)
    ax.plot(xx, yy, color=cm.C_PSI, lw=1.2)
    t = np.radians(50)
    ax.plot([0, 1.45 * np.sin(t)], [0, 1.45 * np.cos(t)], color=cm.MUTED, lw=0.5, ls=(0, (3, 2)))
    ax.add_patch(Arc((0, 0), 0.9, 0.9, theta1=90 - 50, theta2=90, color=cm.INK, lw=0.6))
    ax.text(0.17, 0.5, r"$50^\circ$", fontsize=8)
    cm.save(fig, "davisson-germer-polar")


def debye_scherrer():
    """Метод Дебая — Шеррера: конусы дифрагированных лучей и кольца на экране."""
    fig, (ax, ax2) = cm.subplots(1, 2, width=4.0, height=1.7,
                                 gridspec_kw=dict(width_ratios=[2.3, 1], wspace=0.05))
    cm.scheme_axes(ax, (-2.6, 2.7), (-1.6, 1.6))
    cm.arrow(ax, (-2.5, 0), (-0.12, 0), color=cm.INK, lw=1.0, ms=6)
    ax.text(-2.5, 0.12, "пучок", va="bottom", fontsize=8)
    ax.add_patch(Circle((0, 0), 0.12, color=cm.INK2))
    ax.text(-0.15, -0.18, "порошок", ha="right", va="top", fontsize=8)
    X = 2.3
    ax.plot([X, X], [-1.5, 1.5], color=cm.INK, lw=1.4)
    ax.text(X + 0.08, -1.5, "экран", va="bottom", fontsize=8)
    for ang, col in [(18, cm.BLUE), (31, cm.ORANGE)]:
        y = X * np.tan(np.radians(ang))
        for sgn in (-1, 1):
            ax.plot([0, X], [0, sgn * y], color=col, lw=0.8)
    ax.plot([0, X], [0, 0], color=cm.INK, lw=0.6, ls=(0, (3, 2)))
    ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=0, theta2=31, color=cm.INK, lw=0.6))
    ax.text(0.65, 0.2, r"$2\theta$", fontsize=8)
    cm.scheme_axes(ax2, (-1.6, 1.6), (-1.6, 1.6))
    ax2.add_patch(Rectangle((-1.5, -1.5), 3.0, 3.0, fill=False, ec=cm.INK, lw=0.8))
    for ang, col in [(18, cm.BLUE), (31, cm.ORANGE)]:
        ax2.add_patch(Circle((0, 0), X * np.tan(np.radians(ang)), fill=False, ec=col, lw=1.2))
    ax2.plot([0], [0], "o", ms=2, color=cm.INK)
    cm.save(fig, "debye-scherrer")


if __name__ == "__main__":
    wave_packet()
    bragg()
    microscope()
    davisson_polar()
    debye_scherrer()

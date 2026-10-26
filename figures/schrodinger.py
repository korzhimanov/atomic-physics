"""Глава «Уравнение Шрёдингера и его простейшие решения».

Везде используются единицы ħ = m = 1; волновые функции рассчитаны численно
или по точным формулам и нарисованы со смещением на уровень своей энергии.
"""
import numpy as np
from numpy.polynomial.hermite import hermval
from math import factorial, pi
from scipy.integrate import solve_ivp
from scipy.linalg import eigh_tridiagonal
from matplotlib.patches import Rectangle

import common as cm


def bound_states(U, x):
    """Связанные состояния в потенциале U(x) методом конечных разностей."""
    h = x[1] - x[0]
    d = 1 / h**2 + U
    e = -0.5 / h**2 * np.ones(len(x) - 1)
    E, V = eigh_tridiagonal(d, e)
    V = V / np.sqrt(h)
    return E, V


def level_label(ax, x, y, text, **kw):
    ax.text(x, y, text, va="center", fontsize=8, **kw)


def well():
    """Связанные состояния в потенциальной яме и сплошной спектр."""
    fig, ax = cm.subplots(width=3.6, height=2.5)
    x = np.linspace(-6, 6, 2400)
    U0 = 6.36
    U = -U0 / np.cosh(x) ** 2
    E, V = bound_states(U, x)
    nb = int(np.sum(E < 0))
    ax.axhspan(0, 1.3, color=cm.GRID, lw=0)
    ax.text(4.6, 0.65, "$E > 0$: сплошной\nспектр", ha="center", va="center", fontsize=7.5,
            color=cm.INK2)
    for n in range(nb):
        En = E[n]
        psi = V[:, n] * np.sign(V[np.argmax(np.abs(V[:, n])), n])
        xt = np.arccosh(np.sqrt(U0 / -En))           # точки поворота
        ax.plot([-5.6, 5.6], [En, En], color=cm.C_LEVEL, lw=0.6, ls=(0, (3, 2)))
        ax.plot([-xt, xt], [En, En], color=cm.C_LEVEL, lw=1.1)
        ax.plot(x, En + 0.7 * psi, color=cm.C_PSI, lw=1.0)
        level_label(ax, -5.75, En, f"$E_{n}$", ha="right")
    # точки поворота для основного состояния и запрещённые области
    xt0 = np.arccosh(np.sqrt(U0 / -E[0]))
    for sgn in (-1, 1):
        ax.plot([sgn * xt0, sgn * xt0], [E[0], -6.05], color=cm.MUTED, lw=0.5, ls=":")
    ax.text(-xt0, -6.1, "$x_1$", ha="center", va="top", fontsize=8)
    ax.text(xt0, -6.1, "$x_2$", ha="center", va="top", fontsize=8)
    ax.plot(x, U, color=cm.C_POT, lw=1.4)
    ax.text(1.65, -3.6, "$U(x)$", fontsize=9)
    cm.axis_arrows(ax, "$x$", "$E$", xlim=(-6, 6.3), ylim=(-6.6, 1.6))
    ax.set_xlim(-6.1, 6.4)
    ax.set_ylim(-6.7, 1.6)
    cm.save(fig, "potential-well")


def oscillator():
    """Гармонический осциллятор: уровни энергии и волновые функции."""
    fig, ax = cm.subplots(width=3.2, height=2.7)
    x = np.linspace(-4, 4, 1200)
    U = x**2 / 2
    for n in range(4):
        En = n + 0.5
        c = np.zeros(n + 1)
        c[n] = 1
        psi = hermval(x, c) * np.exp(-x**2 / 2) / np.sqrt(2**n * factorial(n) * np.sqrt(pi))
        xt = np.sqrt(2 * En)
        ax.plot([-xt, xt], [En, En], color=cm.C_LEVEL, lw=1.1)
        m = np.abs(x) <= 3.05
        ax.plot(x[m], En + 0.42 * psi[m], color=cm.C_PSI, lw=1.0)
        frac = {0: r"\frac{1}{2}", 1: r"\frac{3}{2}", 2: r"\frac{5}{2}", 3: r"\frac{7}{2}"}[n]
        level_label(ax, 3.3, En, f"$n={n}$")
        level_label(ax, -3.3, En, f"${frac}\\hbar\\omega$", ha="right")
    ax.plot(x, U, color=cm.C_POT, lw=1.4)
    ax.text(2.75, 4.8, "$U(x)$", fontsize=9, ha="right")
    cm.arrow(ax, (3.85, 1.5), (3.85, 2.5), color=cm.INK, lw=0.7, ms=5, style="<|-|>")
    ax.text(3.92, 2.0, r"$\hbar\omega$", ha="left", va="center", fontsize=8)
    cm.axis_arrows(ax, "$x$", "$E$", xlim=(-3.6, 3.6), ylim=(-0.25, 5.0))
    ax.set_xlim(-4.3, 4.6)
    ax.set_ylim(-0.3, 5.1)
    cm.save(fig, "harmonic-oscillator")


def barrier_solution(k, kap, d, x):
    den = (kap + 1j * k) ** 2 * np.exp(-kap * d) - (kap - 1j * k) ** 2 * np.exp(kap * d)
    B1 = (kap**2 + k**2) * (np.exp(kap * d) - np.exp(-kap * d)) / den
    A3 = 4j * k * kap * np.exp(-1j * k * d) / den
    # амплитуды под барьером из непрерывности в точке x = 0
    A2 = ((1 + B1) + (1j * k / kap) * (1 - B1)) / 2
    B2 = ((1 + B1) - (1j * k / kap) * (1 - B1)) / 2
    psi = np.where(x < 0, np.exp(1j * k * x) + B1 * np.exp(-1j * k * x),
                   np.where(x < d, A2 * np.exp(kap * x) + B2 * np.exp(-kap * x),
                            A3 * np.exp(1j * k * x)))
    return psi


def barrier():
    """Прямоугольный барьер: волновая функция при E < U0."""
    fig, ax = cm.subplots(width=4.2, height=2.0)
    U0, E, d = 3.0, 1.8, 1.0
    k, kap = np.sqrt(2 * E), np.sqrt(2 * (U0 - E))
    x = np.linspace(-7, 6, 3000)
    psi = barrier_solution(k, kap, d, x)
    ax.add_patch(Rectangle((0, 0), d, U0, color=cm.GRID, lw=0))
    ax.plot([-7, 0, 0, d, d, 6], [0, 0, U0, U0, 0, 0], color=cm.C_POT, lw=1.3)
    ax.plot([-7, 6], [E, E], color=cm.C_LEVEL, lw=0.8, ls=(0, (3, 2)))
    ax.plot(x, E + 0.55 * psi.real, color=cm.C_PSI, lw=1.0)
    ax.text(6.05, E, "$E$", va="center", fontsize=9)
    ax.text(d + 0.08, U0, "$U_0$", va="bottom", fontsize=9)
    for xx, lab in [(-3.5, "I"), (d / 2, "II"), (3.5, "III")]:
        ax.text(xx, 3.35, lab, ha="center", fontsize=9)
    ax.text(-0.05, -0.12, "$0$", ha="right", va="top", fontsize=8)
    ax.text(d, -0.12, "$d$", ha="center", va="top", fontsize=8)
    ax.set_xlim(-7.2, 6.5)
    ax.set_ylim(-0.5, 3.7)
    ax.axis("off")
    cm.save(fig, "potential-barrier")


def smooth_barrier():
    """Плавный барьер, приближённый прямоугольными, и качественный вид ψ(x)."""
    fig, (ax, ax2) = cm.subplots(2, 1, width=4.2, height=3.3, sharex=True,
                                 gridspec_kw=dict(height_ratios=[1.15, 1], hspace=0.08))
    U0, E, w = 4.0, 2.5, 1.0
    Ufun = lambda x: U0 * np.exp(-(x / w) ** 2)
    x1, x2 = -w * np.sqrt(np.log(U0 / E)), w * np.sqrt(np.log(U0 / E))
    # прямоугольники ширины dx
    dx = 0.4
    edges = np.arange(-2.2, 2.2001, dx)
    for a in edges[:-1]:
        ax.add_patch(Rectangle((a, 0), dx, Ufun(a + dx / 2), fc=cm.BLUE_LIGHT, ec=cm.BLUE, lw=0.4))
    xs = np.linspace(-7, 7, 2000)
    ax.plot(xs, Ufun(xs), color=cm.C_POT, lw=1.3)
    ax.plot([-7, 7], [E, E], color=cm.C_LEVEL, lw=1.0)
    ax.text(7.05, E, "$E$", va="center", fontsize=9)
    ax.text(0.95, 3.6, "$U(x)$", fontsize=9)
    # ширина одного прямоугольника
    i0 = 7
    a = edges[i0]
    ax.annotate("", xy=(a, -0.3), xytext=(a + dx, -0.3),
                arrowprops=dict(arrowstyle="<|-|>", color=cm.INK, lw=0.6, mutation_scale=5,
                                shrinkA=0, shrinkB=0))
    ax.text(a + dx + 0.08, -0.3, "$dx$", va="center", fontsize=8)
    for xt, lab in [(x1, "$x_1$"), (x2, "$x_2$")]:
        for axx in (ax, ax2):
            axx.axvline(xt, color=cm.MUTED, lw=0.5, ls=":")
        ax.text(xt, 4.35, lab, ha="center", va="bottom", fontsize=8)
    ax.set_ylim(-0.6, 4.3)
    ax.axis("off")

    # волновая функция: интегрируем уравнение Шрёдингера справа налево,
    # начиная с прошедшей волны e^{ikx}, и нормируем на падающую волну
    k = np.sqrt(2 * E)
    xr, xl = 7.0, -7.0

    def rhs(x, y):
        return [y[1], 2 * (Ufun(x) - E) * y[0]]
    y0 = [np.exp(1j * k * xr), 1j * k * np.exp(1j * k * xr)]
    sol = solve_ivp(rhs, (xr, xl), y0, t_eval=xs[::-1], rtol=1e-10, atol=1e-12)
    xx = sol.t[::-1]
    psi = sol.y[0][::-1]
    dpsi = sol.y[1][::-1]
    A = 0.5 * (psi[0] + dpsi[0] / (1j * k)) * np.exp(-1j * k * xx[0])   # падающая волна
    psi = psi / A
    ax2.axvspan(x1, x2, color=cm.GRID, lw=0)
    ax2.plot(xx, psi.real, color=cm.C_PSI, lw=1.0)
    ax2.axhline(0, color=cm.INK2, lw=0.6)
    ax2.text(-6.9, 2.15, r"$\mathrm{Re}\,\psi(x)$", fontsize=9, va="center")
    ax2.text(x2 + 0.15, 2.3, "под барьером\nволновая функция\nэкспоненциально\nубывает",
             fontsize=7, va="top", color=cm.INK2)
    ax2.set_ylim(-2.4, 2.4)
    ax2.set_xlim(-7.2, 7.5)
    ax2.axis("off")
    cm.save(fig, "smooth-barrier")


def tunneling_examples():
    """Автоэлектронная эмиссия и альфа-распад как туннелирование."""
    fig, (a1, a2) = cm.subplots(1, 2, width=4.78, height=2.0, gridspec_kw=dict(wspace=0.15))
    # автоэлектронная эмиссия: треугольный барьер у поверхности металла
    W, F = 1.0, 0.45
    a1.add_patch(Rectangle((-2.0, -2.2), 2.0, 1.2, color=cm.BLUE_LIGHT, lw=0))
    a1.plot([-2.0, 0, 0, 3.6], [-1.0, -1.0, 0, -F * 3.6], color=cm.C_POT, lw=1.3)
    a1.plot([0, 3.6], [0, 0], color=cm.MUTED, lw=0.6, ls=(0, (3, 2)))
    a1.text(3.65, 0.0, "без поля", fontsize=7, va="center", color=cm.INK2)
    a1.text(-1.0, -1.6, "электроны\nметалла", ha="center", va="center", fontsize=7)
    a1.text(-1.0, 0.25, "металл", ha="center", fontsize=8)
    a1.text(2.0, 0.25, "вакуум", ha="center", fontsize=8)
    xt = W / F
    a1.plot([-0.6, 0], [-1.0, -1.0], color=cm.ORANGE, lw=1.0)
    a1.plot([0, xt], [-1.0, -1.0], color=cm.ORANGE, lw=1.0, ls=(0, (2, 1.5)))
    cm.arrow(a1, (xt, -1.0), (xt + 0.6, -1.0), color=cm.ORANGE, lw=1.0, ms=6)
    a1.text(xt + 0.65, -1.0, r"$e^-$", va="center", fontsize=8)
    a1.plot([-2.0, 0], [0, 0], color=cm.MUTED, lw=0.6, ls=(0, (3, 2)))
    cm.arrow(a1, (-0.35, -1.0), (-0.35, 0), color=cm.INK, lw=0.6, ms=4, style="<|-|>")
    a1.text(-0.42, -0.5, r"$A_{\mathrm{вых}}$", va="center", ha="right", fontsize=8)
    a1.text(1.4, -2.0, "внешнее поле\nнаклоняет барьер", fontsize=7, color=cm.INK2, va="center")
    cm.scheme_axes(a1, (-2.1, 4.6), (-2.4, 0.6))
    a1.set_aspect("auto")
    # альфа-распад: прямоугольная яма ядра и кулоновский барьер
    R, B, E = 1.0, 2.0, 0.8
    r = np.linspace(R, 6.0, 400)
    a2.plot([0, R, R], [-1.2, -1.2, B], color=cm.C_POT, lw=1.3)
    a2.plot(r, B * R / r, color=cm.C_POT, lw=1.3)
    rt = B * R / E
    a2.plot([rt + 0.7, 6.0], [E, E], color=cm.MUTED, lw=0.6, ls=(0, (3, 2)))
    a2.plot([0.3, R], [E, E], color=cm.ORANGE, lw=1.0)
    a2.plot([R, rt], [E, E], color=cm.ORANGE, lw=1.0, ls=(0, (2, 1.5)))
    cm.arrow(a2, (rt, E), (rt + 0.7, E), color=cm.ORANGE, lw=1.0, ms=6)
    a2.text(rt + 0.75, E, r"$\alpha$", va="center", fontsize=9)
    a2.text(6.05, E, "$E$", va="center", fontsize=8)
    a2.text(0.5, -0.9, "ядро", ha="center", fontsize=8)
    a2.text(2.4, 1.3, "кулоновский\nбарьер", fontsize=7, color=cm.INK2)
    a2.axhline(0, color=cm.INK2, lw=0.6)
    a2.text(R, -1.35, "$R$", ha="center", va="top", fontsize=8)
    cm.scheme_axes(a2, (-0.2, 6.6), (-1.6, 2.3))
    a2.set_aspect("auto")
    cm.save(fig, "tunneling-examples")


if __name__ == "__main__":
    well()
    oscillator()
    barrier()
    smooth_barrier()
    tunneling_examples()

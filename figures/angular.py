"""Глава «Операторы физических величин и момент импульса»: сферические
координаты, векторная модель момента импульса, сложение моментов."""
import numpy as np
from matplotlib.patches import Circle

import common as cm

K_OBL, A_OBL = 0.55, np.radians(220)   # косоугольная проекция: ось x — на читателя


def proj3(x, y, z):
    """Косоугольная проекция: y — вправо, z — вверх, x — под углом A_OBL с сокращением K_OBL."""
    x, y, z = map(np.asarray, (x, y, z))
    return y + K_OBL * x * np.cos(A_OBL), z + K_OBL * x * np.sin(A_OBL)


def spherical_scheme(ax, r=1.6, theta=np.radians(50), phi=np.radians(55), point=None,
                     axis_len=2.1, labels=True):
    """Оси x, y, z, точка (r, θ, φ), её проекция и углы. Возвращает координаты точки."""
    for v, lab in [((1, 0, 0), "$x$"), ((0, 1, 0), "$y$"), ((0, 0, 1), "$z$")]:
        end = proj3(*(axis_len * np.array(v)))
        cm.arrow(ax, (0, 0), end, color=cm.INK2, lw=0.7, ms=6)
        ax.text(end[0] + 0.06, end[1] + 0.02, lab, fontsize=9)
    P = np.array([r * np.sin(theta) * np.cos(phi), r * np.sin(theta) * np.sin(phi), r * np.cos(theta)])
    Q = np.array([P[0], P[1], 0])
    p, q = proj3(*P), proj3(*Q)
    ax.plot([0, p[0]], [0, p[1]], color=cm.INK, lw=1.1)
    ax.plot([0, q[0]], [0, q[1]], color=cm.MUTED, lw=0.6, ls=(0, (3, 2)))
    ax.plot([q[0], p[0]], [q[1], p[1]], color=cm.MUTED, lw=0.6, ls=(0, (3, 2)))
    # дуга угла θ — в плоскости, содержащей ось z и точку
    t = np.linspace(0, theta, 40)
    rr = 0.55
    arc = proj3(rr * np.sin(t) * np.cos(phi), rr * np.sin(t) * np.sin(phi), rr * np.cos(t))
    ax.plot(*arc, color=cm.INK, lw=0.7)
    tm = proj3(*(0.75 * np.array([np.sin(theta / 2) * np.cos(phi), np.sin(theta / 2) * np.sin(phi),
                                  np.cos(theta / 2)])))
    ax.text(tm[0], tm[1], r"$\vartheta$", ha="center", va="center", fontsize=9)
    # дуга угла φ — в плоскости xy
    f = np.linspace(0, phi, 40)
    arc = proj3(0.5 * np.cos(f), 0.5 * np.sin(f), 0 * f)
    ax.plot(*arc, color=cm.INK, lw=0.7)
    fm = proj3(0.72 * np.cos(phi / 2), 0.72 * np.sin(phi / 2), 0)
    ax.text(fm[0], fm[1], r"$\varphi$", ha="center", va="center", fontsize=9)
    if labels:
        mid = proj3(*(0.55 * P))
        ax.text(mid[0] + 0.1, mid[1] - 0.06, "$r$", ha="left", va="top", fontsize=10)
    return p


def spherical():
    fig, ax = cm.subplots(width=2.4, height=2.2)
    cm.scheme_axes(ax, (-1.2, 2.4), (-0.95, 2.3))
    p = spherical_scheme(ax)
    ax.add_patch(Circle(p, 0.06, color=cm.INK, zorder=5))
    cm.save(fig, "spherical-coordinates")


def vector_model():
    """Векторная модель: при l = 2 проекция L_z = mħ, |L| = ħ√6."""
    fig, ax = cm.subplots(width=2.5, height=2.6)
    l = 2
    L = np.sqrt(l * (l + 1))
    cm.scheme_axes(ax, (-1.2, 3.3), (-2.9, 3.1))
    t = np.linspace(-np.pi / 2, np.pi / 2, 200)
    ax.plot(L * np.cos(t), L * np.sin(t), color=cm.MUTED, lw=0.6, ls=(0, (3, 2)))
    cm.arrow(ax, (0, -2.8), (0, 3.0), color=cm.INK2, lw=0.7, ms=6)
    ax.text(0.08, 3.0, "$z$", va="top", fontsize=9)
    for m in range(-l, l + 1):
        x = np.sqrt(L**2 - m**2)
        ax.plot([0, x + 0.25], [m, m], color=cm.GRID, lw=0.6, zorder=0)
        cm.arrow(ax, (0, 0), (x, m), color=cm.BLUE, lw=1.1, ms=6)
        lab = {0: "$0$", 1: r"$\hbar$", -1: r"$-\hbar$"}.get(m, f"${m}\\hbar$")
        ax.text(-0.1, m, lab, ha="right", va="center", fontsize=8)
        ax.text(x + 0.3, m, f"$m={m}$", va="center", fontsize=8)
    ax.text(3.3, 2.75, r"$|\vec L| = \hbar\sqrt{6}$", fontsize=8, ha="right", color=cm.INK)
    cm.save(fig, "angular-momentum-vector-model")


def addition():
    """Сложение моментов l1 = 2 и l2 = 1: возможные l = 3, 2, 1."""
    fig, (ax, ax2) = cm.subplots(1, 2, width=4.78, height=2.4,
                                 gridspec_kw=dict(width_ratios=[1.35, 1], wspace=0.12))
    l1, l2 = 2, 1
    L1, L2 = np.sqrt(l1 * (l1 + 1)), np.sqrt(l2 * (l2 + 1))
    cm.scheme_axes(ax, (-0.3, 9.6), (-0.9, 4.2))
    a1 = np.radians(75)                     # направление L1 на всех трёх схемах
    for i, l in enumerate((3, 2, 1)):
        o = np.array([0.4 + 3.2 * i, 0.0])
        L = np.sqrt(l * (l + 1))
        ca = (L**2 - L1**2 - L2**2) / (2 * L1 * L2)
        alpha = np.arccos(ca)               # угол между L1 и L2
        v1 = L1 * np.array([np.cos(a1), np.sin(a1)])
        v2 = L2 * np.array([np.cos(a1 - alpha), np.sin(a1 - alpha)])
        cm.arrow(ax, o, o + v1, color=cm.BLUE, lw=1.1, ms=6)
        cm.arrow(ax, o + v1, o + v1 + v2, color=cm.ORANGE, lw=1.1, ms=6)
        cm.arrow(ax, o, o + v1 + v2, color=cm.INK, lw=1.3, ms=7)
        def side_label(start, vec, text, away_from, d=0.28):
            mid = start + vec / 2
            nrm = np.array([-vec[1], vec[0]]) / np.hypot(*vec)
            if np.dot(nrm, mid - away_from) < 0:
                nrm = -nrm
            p = mid + d * nrm
            ax.text(p[0], p[1], text, ha="center", va="center", fontsize=9)
        cL = o + (v1 + v2) / 2
        side_label(o, v1, r"$\vec L_1$", cL)
        side_label(o + v1, v2, r"$\vec L_2$", cL)
        side_label(o, v1 + v2, r"$\vec L$", o + v1 / 2)
        ax.text(o[0] + 0.9, -0.55, f"$l={l}$", ha="center", va="top", fontsize=9)
    # плоскость (m1, m2): каждое состояние — точка, диагонали m = m1 + m2
    cm.scheme_axes(ax2, (-3.5, 3.6), (-2.6, 2.3))
    for m in range(-(l1 + l2), l1 + l2 + 1):
        pts = [(a, m - a) for a in range(-l1, l1 + 1) if -l2 <= m - a <= l2]
        xs = [p[0] for p in pts]
        x0, x1 = min(xs) - 0.3, max(xs) + 0.3
        ax2.plot([x0, x1], [m - x0, m - x1], color=cm.ORANGE, lw=0.6)
        if m - max(xs) == -l2:          # диагональ заканчивается на нижнем ряду
            ax2.text(max(xs) + 0.35, -l2 - 0.4, f"${m}$", ha="left", va="top", fontsize=7,
                     color=cm.INK2)
        else:                            # диагональ заканчивается на правом столбце
            ax2.text(l1 + 0.4, m - l1 - 0.35, f"${m}$", ha="left", va="top", fontsize=7,
                     color=cm.INK2)
    for a in range(-l1, l1 + 1):
        for b in range(-l2, l2 + 1):
            ax2.plot(a, b, "o", ms=4, color=cm.BLUE, zorder=3)
    cm.arrow(ax2, (-2.9, -2.3), (3.2, -2.3), color=cm.INK2, lw=0.6, ms=5)
    ax2.text(3.2, -2.4, "$m_1$", ha="right", va="top", fontsize=9)
    cm.arrow(ax2, (-2.9, -2.3), (-2.9, 1.9), color=cm.INK2, lw=0.6, ms=5)
    ax2.text(-3.0, 1.9, "$m_2$", ha="right", va="top", fontsize=9)
    for a in range(-l1, l1 + 1):
        ax2.text(a, -2.4, f"${a}$", ha="center", va="top", fontsize=7)
    for b in range(-l2, l2 + 1):
        ax2.text(-3.0, b, f"${b}$", ha="right", va="center", fontsize=7)
    ax2.text(3.5, 2.25, "значения $m = m_1 + m_2$\nна диагоналях", ha="right", va="top",
             fontsize=7, color=cm.INK2)
    cm.save(fig, "angular-momentum-addition")


if __name__ == "__main__":
    spherical()
    vector_model()
    addition()

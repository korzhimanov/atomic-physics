"""Глава «Магнитные свойства атомов»: опыт Штерна — Герлаха, сложение L и S."""
import numpy as np
from matplotlib.patches import Rectangle

import common as cm


def stern_gerlach_patterns():
    """След пучка на пластинке: без поля, ожидания классической и боровской теорий, опыт.

    Щель вертикальна, поле неоднородно по горизонтали — как на фотографиях 1922 года."""
    fig = cm.figure(width=3.6, height=1.75)
    gs = fig.add_gridspec(1, 4, wspace=0.12)
    titles = ["без поля", "классическая\nтеория", "квантование\nпо Бору", "опыт\n(серебро)"]
    y = np.linspace(-1, 1, 200)
    env = np.sqrt(np.clip(1 - y**2, 0, None))   # отклонение максимально в середине щели
    for i, title in enumerate(titles):
        a = fig.add_subplot(gs[0, i])
        cm.scheme_axes(a, (-0.95, 0.95), (-1.75, 1.2))
        a.add_patch(Rectangle((-0.85, -1.1), 1.7, 2.2, fc=cm.BLUE_LIGHT, ec=cm.BLUE, lw=0.6))
        if i == 0:
            a.plot(0 * y, y, color=cm.INK, lw=1.4)
        elif i == 1:
            a.fill_betweenx(y, -0.55 * env, 0.55 * env, color=cm.INK2, lw=0, alpha=0.55)
        elif i == 2:
            for k in (-1, 0, 1):
                a.plot(k * 0.55 * env, y, color=cm.INK, lw=1.2)
        else:
            for k in (-1, 1):
                a.plot(k * 0.45 * env, y, color=cm.INK, lw=1.4)
        a.text(0, -1.2, title, ha="center", va="top", fontsize=7)
    cm.save(fig, "stern-gerlach-patterns")


def ls_addition():
    """Сложение орбитального момента (l = 1) и спина (s = 1/2): j = 3/2 и j = 1/2."""
    fig, ax = cm.subplots(width=2.8, height=1.9)
    cm.scheme_axes(ax, (-0.3, 4.4), (-0.75, 2.2))
    Lm, Sm = np.sqrt(2), np.sqrt(3) / 2
    aL = np.radians(70)
    for i, (j, txt) in enumerate([(1.5, "$j = l + 1/2$"), (0.5, "$j = l - 1/2$")]):
        o = np.array([0.3 + 2.3 * i, 0.0])
        J = np.sqrt(j * (j + 1))
        ca = (J**2 - Lm**2 - Sm**2) / (2 * Lm * Sm)
        alpha = np.arccos(ca)
        vL = Lm * np.array([np.cos(aL), np.sin(aL)])
        vS = Sm * np.array([np.cos(aL - alpha), np.sin(aL - alpha)])
        cm.arrow(ax, o, o + vL, color=cm.BLUE, lw=1.1, ms=6)
        cm.arrow(ax, o + vL, o + vL + vS, color=cm.ORANGE, lw=1.1, ms=6)
        cm.arrow(ax, o, o + vL + vS, color=cm.INK, lw=1.3, ms=7)
        for start, vec, lab, away in [(o, vL, r"$\vec L$", o + (vL + vS) / 2),
                                      (o + vL, vS, r"$\vec S$", o + (vL + vS) / 2),
                                      (o, vL + vS, r"$\vec J$", o + vL / 2)]:
            mid = start + vec / 2
            nrm = np.array([-vec[1], vec[0]]) / np.hypot(*vec)
            if np.dot(nrm, mid - away) < 0:
                nrm = -nrm
            p = mid + 0.22 * nrm
            ax.text(p[0], p[1], lab, ha="center", va="center", fontsize=9)
        ax.text(o[0] + 0.55, -0.4, txt, ha="center", va="top", fontsize=8)
    cm.save(fig, "spin-orbit-addition")


def current_loop():
    """Виток с током: площадь S, нормаль n, магнитный момент μ; заряд dq со скоростью v."""
    fig, ax = cm.subplots(width=2.4, height=2.1)
    cm.scheme_axes(ax, (-1.6, 1.7), (-0.8, 2.1))
    a, b = 1.3, 0.45
    t = np.linspace(0, 2 * np.pi, 300)
    ax.fill(a * np.cos(t), b * np.sin(t), color=cm.BLUE_LIGHT, lw=0)
    ax.plot(a * np.cos(t), b * np.sin(t), color=cm.BLUE, lw=1.2)
    ax.text(-0.55, -0.12, "$S$", fontsize=10, color=cm.INK)
    # направление тока
    t0 = np.radians(-60)
    p = np.array([a * np.cos(t0), b * np.sin(t0)])
    v = np.array([-a * np.sin(t0), b * np.cos(t0)])
    cm.arrow(ax, p, p + 0.45 * v / np.hypot(*v), color=cm.BLUE_DARK, lw=1.2, ms=7)
    ax.text(p[0] + 0.15, p[1] - 0.12, "$i$", fontsize=10, va="top")
    # радиус-вектор и элемент контура
    t1 = np.radians(25)
    q = np.array([a * np.cos(t1), b * np.sin(t1)])
    w = np.array([-a * np.sin(t1), b * np.cos(t1)])
    cm.arrow(ax, (0, 0), q, color=cm.INK2, lw=0.8, ms=6)
    ax.text(q[0] * 0.55, q[1] * 0.55 - 0.05, r"$\vec r$", fontsize=9, va="top")
    cm.arrow(ax, q, q + 0.4 * w / np.hypot(*w), color=cm.ORANGE, lw=1.1, ms=6)
    ax.text(q[0] + 0.12, q[1] + 0.3, r"$d\vec r$", fontsize=9)
    # нормаль и магнитный момент
    cm.arrow(ax, (0, 0), (0, 1.9), color=cm.INK, lw=1.3, ms=7)
    ax.text(0.08, 1.85, r"$\vec\mu = \frac{iS}{c}\vec n$", fontsize=9, va="top")
    cm.arrow(ax, (0, 0), (0, 0.8), color=cm.INK, lw=0.8, ms=5)
    ax.text(-0.08, 0.7, r"$\vec n$", fontsize=9, ha="right")
    cm.save(fig, "current-loop")


if __name__ == "__main__":
    current_loop()
    stern_gerlach_patterns()
    ls_addition()

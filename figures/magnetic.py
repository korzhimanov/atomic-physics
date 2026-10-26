"""Глава «Магнитные свойства атомов»: опыт Штерна — Герлаха, сложение L и S."""
import numpy as np
from matplotlib.patches import Rectangle, Polygon, Circle

import common as cm


def stern_gerlach():
    fig = cm.figure(width=4.78, height=2.7)
    gs = fig.add_gridspec(2, 4, height_ratios=[1.25, 1], hspace=0.12, wspace=0.12)
    ax = fig.add_subplot(gs[0, :3])
    axc = fig.add_subplot(gs[0, 3])
    # --- схема установки, вид сбоку
    cm.scheme_axes(ax, (-0.3, 10.2), (-1.7, 1.9))
    ax.add_patch(Rectangle((0, -0.5), 1.1, 1.0, fc=cm.ORANGE_LIGHT, ec=cm.ORANGE, lw=0.8))
    ax.text(0.55, -0.6, "печь", ha="center", va="top", fontsize=7)
    for x in (2.0, 2.8):
        ax.add_patch(Rectangle((x, 0.06), 0.08, 0.5, color=cm.INK))
        ax.add_patch(Rectangle((x, -0.56), 0.08, 0.5, color=cm.INK))
    ax.text(2.44, -0.65, "щели", ha="center", va="top", fontsize=7)
    # полюса магнита
    ax.add_patch(Polygon([(3.6, 0.35), (6.6, 0.35), (6.6, 1.3), (3.6, 1.3)], fc=cm.GRID, ec=cm.INK2, lw=0.6))
    ax.add_patch(Polygon([(3.6, -0.35), (6.6, -0.35), (6.6, -1.3), (3.6, -1.3)], fc=cm.GRID, ec=cm.INK2, lw=0.6))
    ax.text(5.1, 0.82, "N", ha="center", va="center", fontsize=8)
    ax.text(5.1, -0.82, "S", ha="center", va="center", fontsize=8)
    ax.text(5.1, 1.4, "магнит", ha="center", va="bottom", fontsize=7)
    # пучок и его расщепление
    ax.plot([1.1, 3.6], [0, 0], color=cm.C_PHOTON, lw=1.2)
    xs = np.linspace(3.6, 6.6, 50)
    for sgn in (-1, 1):
        y = sgn * 0.12 * ((xs - 3.6) / 3.0) ** 2
        ax.plot(xs, y, color=cm.C_PHOTON, lw=1.0)
        ax.plot([6.6, 9.0], [y[-1], y[-1] + sgn * 0.24 * 2.4 / 1.5], color=cm.C_PHOTON, lw=1.0)
    ax.add_patch(Rectangle((9.0, -1.0), 0.12, 2.0, fc=cm.BLUE_LIGHT, ec=cm.BLUE, lw=0.6))
    ax.text(9.06, -1.1, "стеклянная\nпластинка", ha="center", va="top", fontsize=7)
    cm.arrow(ax, (9.7, -0.6), (9.7, 0.7), color=cm.INK2, lw=0.6, ms=5)
    ax.text(9.8, 0.7, "$z$", fontsize=8, va="top")
    # --- поперечное сечение магнита
    cm.scheme_axes(axc, (-1.3, 1.3), (-1.9, 1.5))
    axc.add_patch(Polygon([(-1.1, 1.3), (1.1, 1.3), (1.1, 0.75), (0.0, 0.25), (-1.1, 0.75)],
                          fc=cm.GRID, ec=cm.INK2, lw=0.6))
    axc.add_patch(Polygon([(-1.1, -0.9), (1.1, -0.9), (1.1, -0.45), (-1.1, -0.45)],
                          fc=cm.GRID, ec=cm.INK2, lw=0.6))
    # силовые линии: от плоского нижнего полюса сходятся к острию верхнего
    t = np.linspace(0, 1, 40)
    for x0 in (-0.85, -0.5, 0.5, 0.85):
        xs_ = x0 * (1 - t) ** 1.5 + np.sign(x0) * 0.05 * t
        ys_ = -0.45 + (0.25 - 0.06 + 0.45) * t
        axc.plot(xs_, ys_, color=cm.MUTED, lw=0.5)
    axc.add_patch(Circle((0, 0.0), 0.07, color=cm.C_PHOTON))
    axc.text(0.0, -0.95, "пучок — в центре\nзазора", fontsize=6.5, ha="center", va="top")
    axc.text(0, 1.38, "сечение магнита", ha="center", va="bottom", fontsize=7)
    # --- картины на пластинке
    titles = ["без поля", "классическая\nтеория", "квантование\nпо Бору", "опыт\n(серебро)"]
    x = np.linspace(-1, 1, 200)
    env = np.sqrt(np.clip(1 - x**2, 0, None))   # отклонение максимально в середине щели
    for i, title in enumerate(titles):
        a = fig.add_subplot(gs[1, i])
        cm.scheme_axes(a, (-1.3, 1.3), (-1.0, 1.0))
        a.add_patch(Rectangle((-1.25, -0.8), 2.5, 1.6, fc=cm.BLUE_LIGHT, ec=cm.BLUE, lw=0.6))
        if i == 0:
            a.plot(x, 0 * x, color=cm.INK, lw=1.4)
        elif i == 1:
            a.fill_between(x, -0.55 * env, 0.55 * env, color=cm.INK2, lw=0, alpha=0.55)
        elif i == 2:
            for k in (-1, 0, 1):
                a.plot(x, k * 0.55 * env, color=cm.INK, lw=1.2)
        else:
            for k in (-1, 1):
                a.plot(x, k * 0.45 * env, color=cm.INK, lw=1.4)
        a.text(0, -0.88, title, ha="center", va="top", fontsize=7)
    cm.save(fig, "stern-gerlach")


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


if __name__ == "__main__":
    stern_gerlach()
    ls_addition()

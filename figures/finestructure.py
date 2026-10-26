"""Глава «Спин-орбитальное взаимодействие и тонкая структура спектральных линий»."""
import numpy as np
from matplotlib.patches import Ellipse

import common as cm


def level(ax, x0, x1, y, label=None, side="right", **kw):
    ax.plot([x0, x1], [y, y], color=kw.pop("color", cm.C_LEVEL), lw=kw.pop("lw", 1.3))
    if label:
        if side == "right":
            ax.text(x1 + 0.1, y, label, va="center", fontsize=8)
        else:
            ax.text(x0 - 0.1, y, label, va="center", ha="right", fontsize=8)


def fine_structure():
    """Тонкая структура: уровень n = 2 водорода и резонансный дублет натрия."""
    fig, (a1, a2) = cm.subplots(1, 2, width=4.78, height=2.4, gridspec_kw=dict(wspace=0.25))
    for a in (a1, a2):
        a.axis("off")
    # --- водород (масштаб тонкого расщепления сильно увеличен)
    a1.set_xlim(-0.2, 5.2)
    a1.set_ylim(-0.6, 4.6)
    level(a1, 0.0, 1.4, 3.0, "$n=2$", side="left", color=cm.MUTED, lw=1.0)
    a1.plot([1.4, 2.0], [3.0, 2.6], color=cm.MUTED, lw=0.5, ls=":")
    a1.plot([1.4, 2.0], [3.0, 3.6], color=cm.MUTED, lw=0.5, ls=":")
    level(a1, 2.0, 2.9, 2.6, r"$2s_{1/2},\ 2p_{1/2}$")
    level(a1, 2.0, 2.9, 3.6, r"$2p_{3/2}$")
    level(a1, 0.0, 2.9, 0.0, r"$1s_{1/2}$")
    a1.text(-0.1, 0.0, "$n=1$", ha="right", va="center", fontsize=8)
    for x, y in [(2.3, 2.6), (2.6, 3.6)]:
        cm.arrow(a1, (x, y), (x, 0.0), color=cm.C_PHOTON, lw=0.9, ms=6)
    cm.arrow(a1, (1.85, 2.6), (1.85, 3.6), color=cm.INK, lw=0.6, ms=4, style="<|-|>")
    a1.text(1.75, 3.75, r"$4{,}5\cdot10^{-5}$ эВ", ha="right", va="bottom", fontsize=7.5)
    a1.text(2.45, -0.25, "линия $L_\\alpha$ — дублет", ha="center", va="top", fontsize=8)
    a1.text(2.5, 4.5, "водород", ha="center", va="top", fontsize=9)
    # --- натрий: резонансный дублет
    a2.set_xlim(-0.2, 5.2)
    a2.set_ylim(-0.6, 4.6)
    level(a2, 0.0, 1.4, 3.0, "$3p$", side="left", color=cm.MUTED, lw=1.0)
    a2.plot([1.4, 2.0], [3.0, 2.6], color=cm.MUTED, lw=0.5, ls=":")
    a2.plot([1.4, 2.0], [3.0, 3.6], color=cm.MUTED, lw=0.5, ls=":")
    level(a2, 2.0, 2.9, 2.6, r"$3p_{1/2}$")
    level(a2, 2.0, 2.9, 3.6, r"$3p_{3/2}$")
    level(a2, 0.0, 2.9, 0.0, r"$3s_{1/2}$")
    a2.text(-0.1, 0.0, "$3s$", ha="right", va="center", fontsize=8)
    for x, y, lab in [(2.3, 2.6, "$D_1$\n589,6 нм"), (2.6, 3.6, "$D_2$\n589,0 нм")]:
        cm.arrow(a2, (x, y), (x, 0.0), color=cm.YELLOW, lw=1.0, ms=6)
    a2.text(2.05, 1.3, "$D_1$", ha="right", va="center", fontsize=8)
    a2.text(2.75, 1.3, "$D_2$", ha="left", va="center", fontsize=8)
    cm.arrow(a2, (1.85, 2.6), (1.85, 3.6), color=cm.INK, lw=0.6, ms=4, style="<|-|>")
    a2.text(1.75, 3.75, r"$2{,}1\cdot10^{-3}$ эВ", ha="right", va="bottom", fontsize=7.5)
    a2.text(2.45, -0.25, "$D_1$: 589,6 нм;  $D_2$: 589,0 нм", ha="center", va="top", fontsize=8)
    a2.text(2.5, 4.5, "натрий", ha="center", va="top", fontsize=9)
    cm.save(fig, "fine-structure")


def ls_coupling():
    """LS-связь: прецессия L и S вокруг J; расщепление терма с L = 1, S = 1."""
    fig, (a1, a2) = cm.subplots(1, 2, width=4.4, height=2.3,
                                gridspec_kw=dict(width_ratios=[1, 1.2], wspace=0.15))
    cm.scheme_axes(a1, (-1.5, 1.6), (-0.4, 3.1))
    J = np.array([0, 2.7])
    cm.arrow(a1, (0, 0), J, color=cm.INK, lw=1.4, ms=7)
    a1.text(0.08, 2.7, r"$\vec J$", fontsize=10, va="top")
    # конусы прецессии
    L = np.array([-0.75, 1.6])
    a1.add_patch(Ellipse((0, L[1]), 1.5, 0.3, fill=False, ec=cm.BLUE, lw=0.6, ls=(0, (3, 2))))
    a1.add_patch(Ellipse((0, 2.7), 1.5, 0.3, fill=False, ec=cm.ORANGE, lw=0.6, ls=(0, (3, 2))))
    cm.arrow(a1, (0, 0), L, color=cm.BLUE, lw=1.2, ms=6)
    cm.arrow(a1, L, J, color=cm.ORANGE, lw=1.2, ms=6)
    a1.text(-0.55, 0.75, r"$\vec L$", fontsize=10, ha="right")
    a1.text(-0.45, 2.3, r"$\vec S$", fontsize=10, ha="right")
    a1.plot([0, 0], [-0.2, 0], color=cm.MUTED, lw=0.5)
    # расщепление терма 3P
    a2.axis("off")
    a2.set_xlim(-0.3, 4.6)
    a2.set_ylim(-0.3, 3.2)
    level(a2, 0.0, 1.2, 1.4, r"$^3P$", side="left", color=cm.MUTED, lw=1.0)
    ys = {0: 0.45, 1: 0.9, 2: 1.8}          # правило интервалов Ланде: 1 : 2
    for Jv, y in ys.items():
        a2.plot([1.2, 2.0], [1.4, y], color=cm.MUTED, lw=0.5, ls=":")
        level(a2, 2.0, 3.0, y, f"$^3P_{Jv}$")
    a2.text(1.5, 2.8, "триплет:\n$L = 1,\\ S = 1,\\ J = 0, 1, 2$", ha="center", va="top", fontsize=8)
    cm.save(fig, "ls-coupling")


if __name__ == "__main__":
    fine_structure()
    ls_coupling()

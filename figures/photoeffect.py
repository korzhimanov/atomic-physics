"""Глава «Фотоны»: вольт-амперная характеристика фотоэлемента и зависимость
запирающего напряжения от частоты."""
import numpy as np
from scipy.constants import h, e

import common as cm


def iv_curve(V, Vz, Is, w=1.2):
    """Качественная ВАХ: ток появляется при V > -Vz и выходит на насыщение Is."""
    t = np.clip(V + Vz, 0, None)
    return Is * (1 - np.exp(-(t / w) ** 2))


def iv():
    fig, ax = cm.subplots(width=3.4, height=2.3)
    V = np.linspace(-3.2, 4.0, 600)
    # синие — одна частота и две интенсивности; оранжевая (штрих) — большая частота
    # при том же числе падающих фотонов, что и для нижней синей кривой
    curves = [
        (1.2, 1.0, cm.BLUE, "-"),
        (1.2, 1.7, cm.BLUE_DARK, "-"),
        (2.4, 1.0, cm.ORANGE, (0, (4, 2))),
    ]
    for Vz, Is, col, ls in curves:
        ax.plot(V, iv_curve(V, Vz, Is), color=col, ls=ls)
    ax.text(1.0, 1.78, r"$\nu_1$, большая интенсивность", fontsize=8, va="bottom")
    ax.text(1.0, 1.06, r"$\nu_1$ и $\nu_2 > \nu_1$", fontsize=8, va="bottom")
    ax.annotate(r"$\nu_2$", xy=(-1.3, iv_curve(-1.3, 2.4, 1.0)), xytext=(-2.6, 0.75),
                fontsize=8, arrowprops=dict(arrowstyle="-", color=cm.INK2, lw=0.5))
    cm.axis_arrows(ax, r"$V$", r"$I$", xlim=(-3.4, 4.6), ylim=(-0.35, 2.15))
    for Vz, lab in [(1.2, r"$V_{\mathrm{з}1}$"), (2.4, r"$V_{\mathrm{з}2}$")]:
        ax.plot([-Vz, -Vz], [-0.06, 0.06], color=cm.INK2, lw=0.8)
        ax.text(-Vz, -0.12, "$-$" + lab, ha="center", va="top", fontsize=8)
    for Is, lab in [(1.0, r"$I_{\mathrm{н}1}$"), (1.7, r"$I_{\mathrm{н}2}$")]:
        ax.text(4.05, Is, lab, ha="left", va="center", fontsize=8)
    ax.set_xlim(-3.4, 4.6)
    ax.set_ylim(-0.4, 2.15)
    cm.save(fig, "photoeffect-i-v")


def stopping_voltage():
    """V_з(ν) для двух металлов: прямые параллельны, их наклон равен h/e."""
    fig, ax = cm.subplots(width=3.4, height=2.3)
    metals = [("цезий", 2.1, cm.BLUE), ("цинк", 4.3, cm.ORANGE)]   # работа выхода, эВ
    nu = np.linspace(0, 16e14, 400)
    for name, A, col in metals:
        nu0 = A * e / h
        Vz = h / e * nu - A
        ok = nu >= nu0
        ax.plot(nu[ok] / 1e14, Vz[ok], color=col)
        ax.plot(nu[~ok] / 1e14, Vz[~ok], color=col, lw=0.8, ls=(0, (3, 2)))
        ax.plot([nu0 / 1e14], [0], "o", ms=3.5, color=col)
        ax.text(nu0 / 1e14, 0.18, r"$\nu_0$", ha="center", va="bottom", fontsize=8)
        ax.text(15.9, h / e * 15.9e14 - A - 0.35, name, ha="right", va="top", fontsize=8)
        ax.text(-0.2, -A, r"$-\varphi_{\mathrm{вых}}$" if name == "цинк" else "",
                ha="right", va="center", fontsize=8)
    # треугольник наклона
    x1, x2 = 9.5, 12.5
    y1 = h / e * x1 * 1e14 - 2.1
    y2 = h / e * x2 * 1e14 - 2.1
    ax.plot([x1, x2, x2], [y1, y1, y2], color=cm.INK2, lw=0.6)
    ax.text(x2 + 0.15, (y1 + y2) / 2, r"наклон $h/e$", va="center", fontsize=8)
    ax.axhline(0, color=cm.INK2, lw=0.6)
    ax.set_xlim(0, 16)
    ax.set_ylim(-4.6, 4.8)
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks([4, 8, 12, 16])
    ax.set_xlabel(r"$\nu$, $10^{14}$ Гц", loc="right")
    ax.set_ylabel(r"$V_{\mathrm{з}}$, В")
    cm.save(fig, "photoeffect-stopping-voltage")


if __name__ == "__main__":
    iv()
    stopping_voltage()

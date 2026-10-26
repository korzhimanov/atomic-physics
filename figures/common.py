"""Общий стиль рисунков конспекта.

Все скрипты в этой папке импортируют этот модуль, рисуют фигуру matplotlib
и сохраняют её функцией save() в img/<имя>.svg.

Размеры фигур задаются в дюймах в реальном масштабе: ширина полосы набора
в PDF (класс book, 10 pt, A4) равна 345 pt ≈ 4,78 дюйма. Рисунок шириной w
дюймов вставляется в текст с атрибутом {width=P%}, где P = w / 4,78 · 100;
тогда шрифт на рисунке совпадает по размеру с подписями в тексте.
"""
import os
import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "img")

TEXTWIDTH = 4.78  # дюймы, ширина полосы набора

# Палитра: категориальные цвета проверены на различимость при дальтонизме
# (первые три — для любых сочетаний); остальные используются только с подписями.
INK = "#0b0b0b"      # основные линии и текст
INK2 = "#52514e"     # вторичный текст, вспомогательные линии
MUTED = "#898781"    # оси, засечки, штриховка
GRID = "#e1e0d9"     # сетка
BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
YELLOW = "#eda100"
MAGENTA = "#e87ba4"
GREEN = "#008300"
VIOLET = "#6250d6"
RED = "#e34948"
BLUE_DARK = "#1c5cab"
BLUE_LIGHT = "#cde2fb"
ORANGE_LIGHT = "#fbd9c9"
SERIES = [BLUE, ORANGE, AQUA]
# упорядоченная шкала одного тона (для величины, растущей монотонно)
RAMP_BLUE = ["#86b6ef", "#3987e5", "#1c5cab", "#0d366b"]

# Смысловые цвета, единые для всей книги
C_PSI = BLUE          # волновая функция
C_LEVEL = ORANGE      # уровни энергии
C_POT = INK           # потенциальная энергия
C_ELECTRON = BLUE     # электрон
C_NUCLEUS = RED       # ядро
C_PHOTON = VIOLET     # фотон


def setup():
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Liberation Serif", "Times New Roman", "DejaVu Serif"],
        "font.size": 9,
        # формулы набираются шрифтом Computer Modern, как формулы в тексте книги
        "mathtext.fontset": "cm",
        "axes.unicode_minus": True,
        "axes.linewidth": 0.6,
        "axes.edgecolor": INK2,
        "axes.labelcolor": INK,
        "axes.titlesize": 9,
        "axes.labelsize": 9,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.prop_cycle": matplotlib.cycler(color=SERIES),
        "xtick.color": INK2,
        "ytick.color": INK2,
        "xtick.labelcolor": INK,
        "ytick.labelcolor": INK,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.major.size": 3,
        "ytick.major.size": 3,
        "grid.color": GRID,
        "grid.linewidth": 0.5,
        "lines.linewidth": 1.4,
        "legend.fontsize": 8,
        "legend.frameon": False,
        "figure.dpi": 100,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.03,
        "svg.fonttype": "path",
        "svg.hashsalt": "atomic-physics",
    })


def figure(width=TEXTWIDTH, height=2.6, **kw):
    setup()
    return plt.figure(figsize=(width, height), **kw)


def subplots(nrows=1, ncols=1, width=TEXTWIDTH, height=2.6, **kw):
    setup()
    return plt.subplots(nrows, ncols, figsize=(width, height), **kw)


def scheme_axes(ax, xlim, ylim):
    """Оси для схемы: равный масштаб, без рамки и засечек."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    return ax


def arrow(ax, start, end, color=INK, lw=1.0, style="-|>", ms=8, **kw):
    """Стрелка от start к end в координатах данных."""
    a = FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=ms,
                        color=color, lw=lw, shrinkA=0, shrinkB=0, **kw)
    ax.add_patch(a)
    return a


def axis_arrows(ax, xlabel=None, ylabel=None, xlim=None, ylim=None,
                color=INK2, lw=0.7):
    """Оси координат со стрелками (для качественных графиков без чисел)."""
    x0, x1 = xlim if xlim else ax.get_xlim()
    y0, y1 = ylim if ylim else ax.get_ylim()
    ax.axis("off")
    arrow(ax, (x0, 0), (x1, 0), color=color, lw=lw, ms=7)
    arrow(ax, (0, y0), (0, y1), color=color, lw=lw, ms=7)
    if xlabel:
        ax.text(x1, 0, xlabel, ha="right", va="top", color=INK)
    if ylabel:
        ax.text(0, y1, " " + ylabel, ha="left", va="top", color=INK)


def save(fig, name):
    """Сохраняет фигуру в img/<name>.svg и сообщает ширину для вставки в текст."""
    path = os.path.join(IMG, name + ".svg")
    fig.savefig(path, metadata={"Date": None, "Creator": None})
    w = fig.get_size_inches()[0]
    print(f"{os.path.relpath(path, ROOT)}: ширина {w:.2f} in ≈ "
          f"{min(100, round(w / TEXTWIDTH * 100))}% полосы")
    plt.close(fig)

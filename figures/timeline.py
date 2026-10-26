"""Глава 1: хронология открытий, приведших к квантовой физике."""
from matplotlib.lines import Line2D

import common as cm

ATOM, RAD, QM = "atom", "rad", "qm"
COLOR = {ATOM: cm.BLUE, RAD: cm.ORANGE, QM: cm.AQUA}
LEGEND = {ATOM: "электрон и строение атома",
          RAD: "излучение и его кванты",
          QM: "квантовая теория"}

# (начало, конец, подпись, категория, уровень подписи, сдвиг подписи в годах);
# уровень > 0 — над осью, < 0 — под осью
EVENTS = [
    (1874, 1874, "1874\nСтони:\nэлементарный\nзаряд", ATOM, 1, 0),
    (1895, 1895, "1895\nРентген:\nX-лучи", RAD, 1, -1.5),
    (1896, 1897, "1896–1897\nТомсон,\nВихерт:\nэлектрон", ATOM, -1, -0.5),
    (1900, 1900, "1900\nПланк:\nкванты\nэнергии", RAD, 2, 0),
    (1905, 1905, "1905\nЭйнштейн:\nкванты\nсвета", RAD, -2, 0),
    (1906, 1911, "1906–1911\nРезерфорд:\nатомное\nядро", ATOM, 1, 0),
    (1910, 1910, "1910\nМилликен:\nзаряд\nэлектрона", ATOM, -1, 1.0),
    (1913, 1913, "1913\nБор:\nмодель\nатома", ATOM, 2, 1.5),
    (1922, 1922, "1922\nКомптон:\nрассеяние\nфотонов", RAD, 1, 0),
    (1924, 1924, "1924\nде Бройль:\nволны\nматерии", QM, -1, 0),
    (1925, 1927, "1925–1927\nквантовая\nмеханика", QM, 2, 1.0),
]

X0, X1 = 1868, 1932
LEVEL = 1.6       # шаг уровней подписей по вертикали (в условных единицах)
GAP = 0.3         # минимальный зазор между подписями по горизонтали, годы


def main():
    fig, ax = cm.subplots(height=3.1)
    ax.set_xlim(X0, X1)
    ax.set_ylim(-3.9, 3.7)
    ax.axis("off")
    fig.canvas.draw()
    renderer = fig._get_renderer()
    inv = ax.transData.inverted()

    # ось времени с засечками через 10 лет
    cm.arrow(ax, (X0, 0), (X1, 0), color=cm.INK2, lw=0.8, ms=7)
    for year in range(1870, 1931, 10):
        ax.plot([year, year], [-0.08, 0.08], color=cm.INK2, lw=0.8)
        ax.text(year, -0.15, str(year), ha="center", va="top", fontsize=7, color=cm.INK2)

    placed = []   # прямоугольники уже размещённых подписей: (x0, x1, y0, y1)
    stems = []    # вертикальные выноски: (x, y_low, y_high)

    def overlaps(box):
        x0, x1, y0, y1 = box
        for (a0, a1, b0, b1) in placed:
            if x0 < a1 + GAP and a0 - GAP < x1 and y0 < b1 and b0 < y1:
                return True
        for (sx, s0, s1) in stems:
            if x0 - GAP < sx < x1 + GAP and y0 < s1 and s0 < y1:
                return True
        return False

    def stem_hits(x, ya, yb):
        lo, hi = min(ya, yb), max(ya, yb)
        return any(a0 - GAP < x < a1 + GAP and b0 < hi and lo < b1
                   for (a0, a1, b0, b1) in placed)

    for start, end, label, cat, level, dx in EVENTS:
        col = COLOR[cat]
        xc = (start + end) / 2
        if end > start:
            ax.plot([start, end], [0, 0], color=col, lw=4, solid_capstyle="butt", zorder=3)
        else:
            ax.plot([xc], [0], "o", ms=4.5, color=col, mec="white", mew=0.8, zorder=3)
        t = ax.text(xc, 0, label, ha="center", va="bottom", fontsize=7,
                    color=cm.INK, linespacing=1.05)
        bb = t.get_window_extent(renderer)
        (bx0, by0), (bx1, by1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
        w, h = bx1 - bx0, by1 - by0
        # первый уровень над осью начинается сразу, под осью — ниже подписей годов
        y = (level - 1) * LEVEL + 0.35 if level > 0 else (level + 1) * LEVEL - 0.75
        lx = xc + dx
        box = (lx - w / 2, lx + w / 2, y, y + h) if level > 0 else (lx - w / 2, lx + w / 2, y - h, y)
        stem = (0.0, y) if level > 0 else (y, 0.0)
        if overlaps(box) or stem_hits(xc, *stem):
            raise RuntimeError("подпись перекрывается: " + label.replace("\n", " "))
        t.set_position((lx, y))
        t.set_va("bottom" if level > 0 else "top")
        placed.append(box)
        stems.append((xc, min(stem), max(stem)))
        ax.plot([xc, xc], stem, color=col, lw=0.7, zorder=1)

    ylo = min(b[2] for b in placed)
    yhi = max(b[3] for b in placed)
    assert ax.get_ylim()[0] <= ylo and yhi <= ax.get_ylim()[1], (ylo, yhi)
    handles = [Line2D([], [], color=COLOR[c], marker="o", ms=4.5, lw=0) for c in LEGEND]
    ax.legend(handles, LEGEND.values(), loc="upper left", fontsize=7.5,
              bbox_to_anchor=(0.0, 1.0), handletextpad=0.3, borderaxespad=0.2)
    cm.save(fig, "timeline")


if __name__ == "__main__":
    main()

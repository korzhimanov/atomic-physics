"""Глава «Многоэлектронные квантовые системы»."""
import numpy as np
from matplotlib.patches import Circle
from matplotlib.colors import LinearSegmentedColormap

import common as cm

# энергии уровней гелия относительно основного состояния 1s², эВ (NIST ASD)
HE_LEVELS = {
    ("S", 1): [(1, 0.0), (2, 20.616), (3, 22.920)],
    ("P", 1): [(2, 21.218), (3, 23.087)],
    ("D", 1): [(3, 23.074)],
    ("S", 3): [(2, 19.820), (3, 22.718)],
    ("P", 3): [(2, 20.964), (3, 23.007)],
    ("D", 3): [(3, 23.074)],
}
HE_ION = 24.587


def paths():
    """Траектории двух частиц до и после столкновения (общие для обеих панелей)."""
    t_in = np.linspace(0, 1, 50)
    p1_in = np.stack([-2.6 + 2.45 * t_in, -0.12 + 0 * t_in], 1)
    p2_in = np.stack([2.6 - 2.45 * t_in, 0.12 + 0 * t_in], 1)
    t_out = np.linspace(0, 1, 50)
    p1_out = np.stack([-0.15 - 1.6 * t_out, -0.12 + 1.5 * t_out], 1)
    p2_out = np.stack([0.15 + 1.6 * t_out, 0.12 - 1.5 * t_out], 1)
    return p1_in, p2_in, p1_out, p2_out


def identical():
    """Классические траектории против квантовых волновых пакетов."""
    fig, (a1, a2) = cm.subplots(1, 2, width=4.78, height=2.3, gridspec_kw=dict(wspace=0.08))
    for a in (a1, a2):
        cm.scheme_axes(a, (-2.9, 2.9), (-2.75, 1.9))
    p1_in, p2_in, p1_out, p2_out = paths()
    # --- классическая механика
    for path, col in [(p1_in, cm.BLUE), (p1_out, cm.BLUE), (p2_in, cm.ORANGE), (p2_out, cm.ORANGE)]:
        a1.plot(path[:, 0], path[:, 1], color=col, lw=0.8, ls=(0, (3, 2)))
    for k, frac in enumerate((0.0, 0.5, 1.0)):
        i = int(frac * 49)
        alpha = 0.35 + 0.3 * k
        for p, col, lab in [(p1_in, cm.BLUE, "1"), (p2_in, cm.ORANGE, "2")]:
            a1.add_patch(Circle(p[i], 0.17, color=col, alpha=alpha, lw=0))
            a1.text(*p[i], lab, ha="center", va="center_baseline", fontsize=7, color="white")
    for frac in (0.5, 1.0):
        i = int(frac * 49)
        for p, col, lab in [(p1_out, cm.BLUE, "1"), (p2_out, cm.ORANGE, "2")]:
            a1.add_patch(Circle(p[i], 0.17, color=col, lw=0))
            a1.text(*p[i], lab, ha="center", va="center_baseline", fontsize=7, color="white")
    a1.text(0, -2.7, "классическая механика:\nкаждая частица движется по своей траектории",
            ha="center", va="bottom", fontsize=7)
    # --- квантовая механика: плотность вероятности волновых пакетов
    x = np.linspace(-2.9, 2.9, 400)
    y = np.linspace(-1.95, 1.9, 300)
    X, Y = np.meshgrid(x, y)
    rho = np.zeros_like(X)
    snaps = [(p1_in, 0.0), (p1_in, 0.5), (p2_in, 0.0), (p2_in, 0.5),
             (p1_in, 1.0), (p2_in, 1.0),
             (p1_out, 0.5), (p1_out, 1.0), (p2_out, 0.5), (p2_out, 1.0)]
    for path, frac in snaps:
        i = int(frac * 49)
        tt = frac if path is p1_in or path is p2_in else 1 + frac
        w = 0.18 + 0.12 * tt                       # пакеты расплываются со временем
        rho += np.exp(-((X - path[i, 0]) ** 2 + (Y - path[i, 1]) ** 2) / (2 * w**2)) * (0.18 / w) ** 0.5
    cmap = LinearSegmentedColormap.from_list("psi", ["#ffffff", cm.VIOLET])
    a2.imshow(rho, extent=(x[0], x[-1], y[0], y[-1]), origin="lower", cmap=cmap,
              vmin=0, vmax=rho.max() * 0.75, interpolation="bilinear")
    for p, lab in [(p1_in[0], "1"), (p2_in[0], "2")]:
        a2.text(*p, lab, ha="center", va="center_baseline", fontsize=7, color="white")
    for p, dx, ha in [(p1_out[-1], 0.45, "left"), (p2_out[-1], -0.45, "right")]:
        a2.text(p[0] + dx, p[1], "1 или 2?", ha=ha, va="center", fontsize=7, color=cm.INK)
    a2.add_patch(Circle((0, 0), 0.55, fill=False, ec=cm.INK2, lw=0.6, ls=(0, (2, 1.5))))
    a2.text(0.62, 0.42, "пакеты\nперекрываются", fontsize=6.5, color=cm.INK2, va="bottom")
    a2.text(0, -2.7, "квантовая механика: после перекрытия\nнельзя сказать, где какая частица",
            ha="center", va="bottom", fontsize=7)
    cm.save(fig, "identical-particles")


def madelung():
    """Порядок заполнения подоболочек: по росту n + l, при равных n + l — по росту n."""
    fig, ax = cm.subplots(width=2.4, height=2.6)
    ax.axis("off")
    names = "spdf"
    for n in range(1, 8):
        for l in range(min(n, 4)):
            ax.text(l, -n, f"{n}{names[l]}", ha="center", va="center", fontsize=8.5)
    # диагонали n + l = const
    for s in range(1, 9):
        cells = [(n, s - n) for n in range(1, 8) if 0 <= s - n < min(n, 4)]
        if not cells:
            continue
        (n0, l0), (n1, l1) = cells[0], cells[-1]
        p0 = np.array([l0 + 0.35, -n0 + 0.35])
        p1 = np.array([l1 - 0.35, -n1 - 0.35])
        cm.arrow(ax, p0, p1, color=cm.ORANGE, lw=0.9, ms=6)
    ax.set_xlim(-0.6, 3.6)
    ax.set_ylim(-7.7, -0.4)
    cm.save(fig, "madelung")


def helium_terms():
    """Уровни гелия: пара- (синглеты) и ортогелий (триплеты)."""
    fig, (ax, axb) = cm.subplots(2, 1, width=3.6, height=3.2, sharex=True,
                                 gridspec_kw=dict(height_ratios=[4.2, 1], hspace=0.06))
    cols = {("S", 1): 0, ("P", 1): 1.2, ("D", 1): 2.4, ("S", 3): 4.0, ("P", 3): 5.2, ("D", 3): 6.4}
    # подписи — конфигурация внешнего электрона (второй электрон всегда в состоянии 1s)
    for key, lv in HE_LEVELS.items():
        L, S = key
        x = cols[key]
        for n, E in lv:
            target = axb if E < 5 else ax
            target.plot([x - 0.35, x + 0.35], [E, E], color=cm.C_LEVEL, lw=1.3)
            name = f"${n}{L.lower()}$" if E > 0 else "$1s^2$"
            target.text(x + 0.38, E, name, va="center", fontsize=7)
    ax.axhline(HE_ION, color=cm.MUTED, lw=0.6, ls=(0, (3, 2)))
    ax.text(7.1, HE_ION + 0.05, "ионизация", ha="right", va="bottom", fontsize=7, color=cm.INK2)
    for key, x in cols.items():
        ax.text(x, 24.95, f"$^{key[1]}{key[0]}$", ha="center", va="bottom", fontsize=9)
    ax.text(1.2, 25.5, "парагелий ($S = 0$)", ha="center", va="bottom", fontsize=8)
    ax.text(5.2, 25.5, "ортогелий ($S = 1$)", ha="center", va="bottom", fontsize=8)
    # переходы внутри каждой системы
    for (xa, Ea), (xb, Eb), col in [((1.2, 23.087), (0.0, 20.616), cm.BLUE),
                                    ((2.4, 23.074), (1.2, 21.218), cm.BLUE),
                                    ((5.2, 20.964), (4.0, 19.820), cm.AQUA),
                                    ((6.4, 23.074), (5.2, 20.964), cm.AQUA)]:
        cm.arrow(ax, (xa - 0.15, Ea), (xb + 0.15, Eb), color=col, lw=0.8, ms=5)
    ax.annotate("", xy=(0.1, 19.5), xytext=(1.05, 21.218),
                arrowprops=dict(arrowstyle="-|>", color=cm.BLUE, lw=0.8, mutation_scale=5,
                                shrinkA=0, shrinkB=0))
    axb.annotate("", xy=(0.1, 0.0), xytext=(0.1, 1.2),
                 arrowprops=dict(arrowstyle="-|>", color=cm.BLUE, lw=0.8, mutation_scale=5,
                                 shrinkA=0, shrinkB=0))
    ax.set_ylim(19.5, 26.2)
    axb.set_ylim(-0.6, 1.2)
    for a in (ax, axb):
        a.spines["bottom"].set_visible(False)
        a.tick_params(axis="x", length=0)
        a.set_xticks([])
    axb.spines["top"].set_visible(False)
    ax.set_yticks([20, 21, 22, 23, 24])
    axb.set_yticks([0])
    ax.set_ylabel("$E$, эВ")
    # знаки разрыва оси
    d = 0.015
    kw = dict(transform=ax.transAxes, color=cm.INK2, clip_on=False, lw=0.6)
    ax.plot((-d, d), (-d, d), **kw)
    kw.update(transform=axb.transAxes)
    axb.plot((-d, d), (1 - 4 * d, 1 + 4 * d), **kw)
    ax.set_xlim(-0.7, 7.2)
    cm.save(fig, "helium-terms")


def h2_geometry():
    fig, ax = cm.subplots(width=2.6, height=1.6)
    cm.scheme_axes(ax, (-0.6, 3.6), (-0.9, 1.6))
    A, B = np.array([0.0, 0.0]), np.array([3.0, 0.0])
    e1, e2 = np.array([0.5, 1.2]), np.array([2.0, -0.8])
    lines = [(e1, A, "-", r"$r_{1A}$", (-0.2, 0.05)), (e2, B, "-", r"$r_{2B}$", (0.2, -0.05)),
             (e1, B, (0, (3, 2)), r"$r_{1B}$", (0.12, 0.12)), (e2, A, (0, (3, 2)), r"$r_{2A}$", (-0.12, -0.15)),
             (e1, e2, (0, (1, 1.5)), r"$r_{12}$", None)]
    for p, q, ls, lab, off in lines:
        ax.plot([p[0], q[0]], [p[1], q[1]], color=cm.INK2, lw=0.8, ls=ls)
        m = (p + q) / 2 + np.array(off) if off is not None else p + 0.3 * (q - p) + np.array([0.2, 0.02])
        ax.text(*m, lab, ha="center", va="center", fontsize=8)
    ax.plot([A[0], B[0]], [A[1], B[1]], color=cm.INK, lw=0.8)
    ax.text(2.4, 0.05, "$R$", ha="center", va="bottom", fontsize=9)
    for P, lab in [(A, "A"), (B, "B")]:
        ax.add_patch(Circle(P, 0.11, color=cm.C_NUCLEUS, zorder=5))
        ax.text(P[0], P[1] - 0.2, lab, ha="center", va="top", fontsize=9)
    for P, lab in [(e1, "1"), (e2, "2")]:
        ax.add_patch(Circle(P, 0.09, color=cm.C_ELECTRON, zorder=5))
        ax.text(P[0] + 0.13, P[1] + 0.05, lab, ha="left", va="bottom", fontsize=9)
    cm.save(fig, "h2-geometry")


def h2_energy():
    """Энергия взаимодействия атомов водорода по Гайтлеру — Лондону."""
    from scipy.special import expi
    g = 0.5772156649

    def parts(R):
        S = np.exp(-R) * (1 + R + R**2 / 3)
        Sp = np.exp(R) * (1 - R + R**2 / 3)
        j = 1 / R - np.exp(-2 * R) * (1 + 1 / R)
        k = np.exp(-R) * (1 + R)
        jp = 1 / R - np.exp(-2 * R) * (1 / R + 11 / 8 + 3 * R / 4 + R**2 / 6)
        kp = (1 / 5) * (-np.exp(-2 * R) * (-25 / 8 + 23 * R / 4 + 3 * R**2 + R**3 / 3)
                        + (6 / R) * (S**2 * (g + np.log(R)) + Sp**2 * expi(-4 * R)
                                     - 2 * S * Sp * expi(-2 * R)))
        Q = -2 * j + jp + 1 / R          # кулоновский интеграл (в атомных единицах)
        A = -2 * S * k + kp + S**2 / R   # обменный интеграл
        return S, Q, A
    HARTREE = 27.2114
    R = np.linspace(0.6, 6, 600)
    S, Q, A = parts(R)
    Es = (Q + A) / (1 + S**2) * HARTREE
    Ea = (Q - A) / (1 - S**2) * HARTREE
    fig, ax = cm.subplots(width=3.4, height=2.4)
    ax.axhline(0, color=cm.INK2, lw=0.6)
    ax.plot(R, Ea, color=cm.ORANGE)
    ax.plot(R, Es, color=cm.BLUE)
    from scipy.optimize import minimize_scalar
    res = minimize_scalar(lambda r: (lambda S, Q, A: (Q + A) / (1 + S**2))(*parts(r)),
                          bounds=(1, 3), method="bounded")
    R0, E0 = res.x, res.fun * HARTREE
    ax.plot(R0, E0, "o", ms=3.5, color=cm.BLUE)
    ax.annotate(f"$R_0 \\approx {R0:.2f}\\,r_B$".replace(".", "{,}"), xy=(R0, E0),
                xytext=(R0 + 0.6, E0 - 0.9), fontsize=8,
                arrowprops=dict(arrowstyle="-", color=cm.INK2, lw=0.5))
    ax.plot([1.401], [-4.75], "s", ms=3.5, color=cm.INK)
    ax.text(1.55, -4.75, "эксперимент", va="center", fontsize=7.5)
    ax.text(2.55, 2.4, r"$\Delta E_a$: спины сонаправлены", fontsize=8)
    ax.text(3.4, -1.9, r"$\Delta E_s$: спины" + "\nпротивоположны", fontsize=8)
    ax.set_xlim(0.6, 6)
    ax.set_ylim(-5.6, 4.5)
    ax.set_xlabel(r"$R/r_B$")
    ax.set_ylabel(r"$\Delta E$, эВ")
    cm.save(fig, "h2-energy")


if __name__ == "__main__":
    identical()
    madelung()
    helium_terms()
    h2_geometry()
    h2_energy()

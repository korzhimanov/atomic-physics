"""Глава 2 и семинар 1: распределение Планка и его предельные случаи."""
import numpy as np
from scipy.constants import h, c, k

import common as cm


def planck_nu(nu, T):
    return 8 * np.pi * h * nu**3 / c**3 / np.expm1(h * nu / (k * T))


def planck_lambda(lam, T):
    return 8 * np.pi * h * c / lam**5 / np.expm1(h * c / (lam * k * T))


def wien_nu(nu, T):
    return 8 * np.pi * h * nu**3 / c**3 * np.exp(-h * nu / (k * T))


def rj_nu(nu, T):
    return 8 * np.pi * nu**2 / c**3 * k * T


TEMPS = [2000, 3000, 4000, 5000]
VISIBLE_NU = (c / 750e-9, c / 400e-9)   # Гц
VISIBLE_LAM = (0.40, 0.75)              # мкм


def frequency():
    fig, ax = cm.subplots(height=2.7)
    nu = np.linspace(1e11, 1.0e15, 4000)
    ax.axvspan(VISIBLE_NU[0] / 1e14, VISIBLE_NU[1] / 1e14, color=cm.GRID, lw=0, zorder=0)
    ax.text(np.mean(VISIBLE_NU) / 1e14, 11.6, "видимый\nдиапазон", ha="center",
            va="top", color=cm.INK2, fontsize=8)
    for T, col in zip(TEMPS, cm.RAMP_BLUE):
        u = planck_nu(nu, T) * 1e16
        ax.plot(nu / 1e14, u, color=col)
        i = np.argmax(u)
        ax.text(nu[i] / 1e14, u[i] + 0.25, f"{T} К", ha="center", va="bottom",
                color=cm.INK, fontsize=8)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.set_xlabel(r"$\nu$, $10^{14}$ Гц")
    ax.set_ylabel(r"$u_\nu$, $10^{-16}$ Дж$\cdot$с/м$^3$")
    cm.save(fig, "blackbody-planck-frequency")


def wavelength():
    fig, ax = cm.subplots(height=2.7)
    lam = np.linspace(0.05e-6, 3.0e-6, 4000)
    ax.axvspan(*VISIBLE_LAM, color=cm.GRID, lw=0, zorder=0)
    ax.text(np.mean(VISIBLE_LAM), 0.745, "видимый\nдиапазон", ha="center",
            va="top", color=cm.INK2, fontsize=8)
    peaks = []
    for T, col in zip(TEMPS, cm.RAMP_BLUE):
        u = planck_lambda(lam, T) * 1e-6
        ax.plot(lam * 1e6, u, color=col)
        i = np.argmax(u)
        peaks.append((lam[i] * 1e6, u[i]))
        ax.text(lam[i] * 1e6 + 0.08, u[i] + 0.008, f"{T} К", ha="left", va="bottom",
                color=cm.INK, fontsize=8)
    # штриховая линия — положение максимумов (закон смещения Вина)
    b = 2.897771955e-3
    Ts = np.linspace(1800, 5100, 100)
    lm = b / Ts
    ax.plot(lm * 1e6, planck_lambda(lm, Ts) * 1e-6, color=cm.INK2, lw=0.8, ls="--")
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 0.75)
    ax.set_xlabel(r"$\lambda$, мкм")
    ax.set_ylabel(r"$u_\lambda$, Дж/(м$^3\cdot$мкм)")
    cm.save(fig, "blackbody-planck-wavelength")


def comparison():
    T = 4000
    fig, ax = cm.subplots(height=2.7)
    nu = np.linspace(1e11, 1.0e15, 4000)
    x = nu / 1e14
    ax.plot(x, rj_nu(nu, T) * 1e16, color=cm.ORANGE)
    ax.plot(x, wien_nu(nu, T) * 1e16, color=cm.BLUE)
    ax.plot(x, planck_nu(nu, T) * 1e16, color=cm.INK, lw=1.6)
    ax.text(1.12, 5.6, "Рэлей — Джинс", color=cm.INK, ha="left", fontsize=8)
    for name, f, x0, xy in [("Планк", planck_nu, 3.1, (4.3, 5.0)),
                            ("Вин", wien_nu, 1.9, (2.4, 1.3))]:
        y0 = f(x0 * 1e14, T) * 1e16
        ax.annotate(name, xy=(x0, y0), xytext=xy, color=cm.INK, fontsize=8,
                    va="center", arrowprops=dict(arrowstyle="-", color=cm.INK2, lw=0.5,
                                                 shrinkA=1, shrinkB=1))
    # области применимости предельных формул
    nu_T = k * T / h / 1e14   # частота, при которой hν = kT
    ax.axvline(nu_T, color=cm.MUTED, lw=0.6, ls=":")
    ax.text(nu_T + 0.1, 0.25, r"$h\nu = kT$", color=cm.INK2, fontsize=8)
    ax.annotate("", xy=(0.05, 6.4), xytext=(nu_T, 6.4),
                arrowprops=dict(arrowstyle="-|>", color=cm.INK2, lw=0.7))
    ax.text(nu_T / 2, 6.55, r"$h\nu \ll kT$", ha="center", color=cm.INK2, fontsize=8)
    ax.annotate("", xy=(9.9, 6.4), xytext=(nu_T, 6.4),
                arrowprops=dict(arrowstyle="-|>", color=cm.INK2, lw=0.7))
    ax.text(7.5, 6.55, r"$h\nu \gg kT$", ha="center", color=cm.INK2, fontsize=8)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.2)
    ax.set_xlabel(r"$\nu$, $10^{14}$ Гц")
    ax.set_ylabel(r"$u_\nu$, $10^{-16}$ Дж$\cdot$с/м$^3$")
    cm.save(fig, "blackbody-comparison-4000K")


if __name__ == "__main__":
    frequency()
    wavelength()
    comparison()

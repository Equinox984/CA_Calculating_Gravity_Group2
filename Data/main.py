"""Physics Project - Method I"""

import pandas as pd
import numpy as np

# --- Constants ---
theta_max = 5        # degrees
n_osc = 30           # oscillations per trial
delta_L0 = 0.0023    # m
delta_tn = 0.3       # s
g_accepted = 9.7808   # m/s²

# --- Data ---
data = pd.read_csv("table1.txt", sep=r"\s+")
N = len(data)
mid = N // 2  # row 8 (index 7)

# --- Length statistics ---
L0 = data["L0"]
mean_L = L0.mean()
sigma_L = L0.std(ddof=1)
sigma_mL = sigma_L / np.sqrt(N)
delta_L = np.sqrt(delta_L0**2 + sigma_mL**2)

# --- Period statistics ---
tn = data["tn"]
T0 = tn / n_osc
mean_T = T0.mean()
sigma_T = T0.std(ddof=1)
sigma_mT = sigma_T / np.sqrt(N)
delta_T0 = delta_tn / n_osc
delta_T = np.sqrt(delta_T0**2 + sigma_mT**2)

# --- g ---
g = 4 * np.pi**2 * mean_L / mean_T**2
dg = 4 * np.pi**2 * np.sqrt((delta_L / mean_T**2)**2 + (2 * mean_L * delta_T / mean_T**3)**2)

# ===================== TABLE 1 =====================
t1 = pd.DataFrame({
    "#":        range(1, N + 1),
    "θmax(°)":  "",
    "L0(m)":    L0.values,
    "δL0(m)":   "",
    "L̄(m)":    "",
    "σL(m)":    "",
    "σL̄(m)":   ""
})
t1.loc[mid, "θmax(°)"] = theta_max
t1.loc[mid, "δL0(m)"]  = round(delta_L0, 4)
t1.loc[mid, "L̄(m)"]   = round(mean_L, 4)
t1.loc[mid, "σL(m)"]   = round(sigma_L, 4)
t1.loc[mid, "σL̄(m)"]  = round(sigma_mL, 4)

print("=" * 60)
print("TABLE 1: Length analysis (Method I)")
print("=" * 60)
print(t1.to_string(index=False))

# ===================== TABLE 2 =====================
t2 = pd.DataFrame({
    "#":        range(1, N + 1),
    "θmax(°)":  "",
    "tn(s)":    tn.values,
    "δtn(s)":   "",
    "T0(s)":    T0.round(4).values,
    "δT0(s)":   "",
    "T̄(s)":    "",
    "σT(s)":    "",
    "σT̄(s)":   ""
})
t2.loc[mid, "θmax(°)"] = theta_max
t2.loc[mid, "δtn(s)"]  = round(delta_tn, 4)
t2.loc[mid, "δT0(s)"]  = round(delta_T0, 4)
t2.loc[mid, "T̄(s)"]   = round(mean_T, 4)
t2.loc[mid, "σT(s)"]   = round(sigma_T, 4)
t2.loc[mid, "σT̄(s)"]  = round(sigma_mT, 4)

print()
print("=" * 60)
print("TABLE 2: Period analysis (Method I)")
print("=" * 60)
print(t2.to_string(index=False))

# ===================== SUMMARY =====================
pct_err = (g - g_accepted) / g_accepted * 100
Ip = dg / g * 100

print()
print("=" * 60)
print("SUMMARY: Method I")
print("=" * 60)
print(f"L̄   = {mean_L:.4f} m")
print(f"σL   = {sigma_L:.4f} m")
print(f"σL̄  = {sigma_mL:.4f} m")
print(f"δL   = {delta_L:.4f} m")
print()
print(f"T̄   = {mean_T:.4f} s")
print(f"σT   = {sigma_T:.4f} s")
print(f"σT̄  = {sigma_mT:.4f} s")
print(f"δT   = {delta_T:.4f} s")
print()
print(f"g    = {g:.4f} ± {dg:.4f} m/s²")
print(f"%err = {pct_err:.3f} %")
print(f"Ip   = {Ip:.3f} %")

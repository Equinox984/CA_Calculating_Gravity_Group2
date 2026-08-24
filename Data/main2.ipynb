"""Physics Project - Method II"""

import pandas as pd
import numpy as np

# --- Constants ---
theta_max = 5        # degrees
n_osc = 30           # oscillations per trial
delta_L = 0.0023     # m
delta_tn = 0.3       # s
g_accepted = 9.778   # m/s²

# --- Data ---
data = pd.read_csv("table2.txt", sep=r"\s+")
N = len(data)
mid = N // 2  # row 8 (index 7)

# --- Per-row calculations ---
data["T"]  = data["tn"] / n_osc
data["dT"] = delta_tn / n_osc
data["g"]  = 4 * np.pi**2 * data["L"] / data["T"]**2
data["dg"] = data["g"] * np.sqrt((delta_L / data["L"])**2 + (2 * data["dT"] / data["T"])**2)

# --- Statistics ---
gbar = data["g"].mean()
sig_g = data["g"].std(ddof=1)
sig_gbar = sig_g / np.sqrt(N)

# ===================== TABLE 3 =====================
t3 = pd.DataFrame({
    "#":       range(1, N + 1),
    "θmax(°)": "",
    "L(m)":    data["L"].values,
    "δL(m)":   "",
    "tn(s)":   data["tn"].values,
    "δtn(s)":  "",
    "T(s)":    data["T"].round(4).values,
    "δT(s)":   "",
    "g(m/s²)": data["g"].round(4).values,
    "δg(m/s²)":"",
    "ḡ(m/s²)": "",
    "σg(m/s²)":"",
    "σḡ(m/s²)":""
})
t3.loc[mid, "θmax(°)"]  = theta_max
t3.loc[mid, "δL(m)"]    = round(delta_L, 4)
t3.loc[mid, "δtn(s)"]   = round(delta_tn, 4)
t3.loc[mid, "δT(s)"]    = round(data["dT"].iloc[0], 4)
t3.loc[mid, "ḡ(m/s²)"] = round(gbar, 4)
t3.loc[mid, "σg(m/s²)"] = round(sig_g, 4)
t3.loc[mid, "σḡ(m/s²)"]= round(sig_gbar, 4)

# δg goes in every row (it's per-trial)
t3["δg(m/s²)"] = data["dg"].round(4).values

print("=" * 80)
print("TABLE 3: Calculation of g by varying the pendulum length (Method II)")
print("=" * 80)
print(t3.to_string(index=False))

# ===================== SUMMARY =====================
pct_err = (gbar - g_accepted) / g_accepted * 100
Ip = sig_gbar / gbar * 100

print()
print("=" * 60)
print("SUMMARY: Method II")
print("=" * 60)
print(f"ḡ    = {gbar:.4f} m/s²")
print(f"σg   = {sig_g:.4f} m/s²")
print(f"σḡ   = {sig_gbar:.4f} m/s²")
print()
print(f"g    = {gbar:.4f} ± {sig_gbar:.4f} m/s²")
print(f"%err = {pct_err:.3f} %")
print(f"Ip   = {Ip:.3f} %")

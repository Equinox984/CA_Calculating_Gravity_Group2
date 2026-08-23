"""Physics Project - Method I"""

import pandas as pd
import numpy as np

# --- Constants ---
theta_max = 5        # degrees
n_osc = 30           # oscillations per trial
delta_L0 = 0.0023    # m  (measuring tape, 2.3 mm)
delta_tn = 0.01      # s  (timer resolution)  <-- EDIT if teacher says otherwise

# --- Data ---
data = pd.read_csv("table1.txt", sep=r"\s+")
N = len(data)

# --- Table 1: length statistics ---
L0 = data["L0"]
mean_L, sigma_L = L0.mean(), L0.std(ddof=1)
sigma_mL = sigma_L / np.sqrt(N)
delta_L  = np.sqrt(delta_L0**2 + sigma_mL**2)

# --- Table 2: period statistics ---
tn = data["tn"]
T0 = tn / n_osc
mean_T, sigma_T = T0.mean(), T0.std(ddof=1)
sigma_mT = sigma_T / np.sqrt(N)
delta_T0 = delta_tn / n_osc
delta_T  = np.sqrt(delta_T0**2 + sigma_mT**2)

# --- Fill tables teacher-style: stats in middle row ---
df1 = data[["L0"]].copy()
for c in ["theta_max","delta_L0","Avr_L0","sigma_L0","sigma_Avr_L0"]:
    df1[c] = ""
df2 = pd.DataFrame({"tn": tn, "T0": T0.round(4)})
for c in ["theta_max","delta_tn","delta_T0","Avr_T","sigma_T","sigma_Avr_T"]:
    df2[c] = ""
mid = N // 2
df1.loc[mid, ["theta_max","delta_L0","Avr_L0","sigma_L0","sigma_Avr_L0"]] = [
    theta_max, delta_L0, round(mean_L,4), round(sigma_L,4), round(sigma_mL,4)]
df2.loc[mid, ["theta_max","delta_tn","delta_T0","Avr_T","sigma_T","sigma_Avr_T"]] = [
    theta_max, delta_tn, round(delta_T0,4), round(mean_T,4), round(sigma_T,4), round(sigma_mT,4)]

print("TABLE 1 - Length\n", df1.to_string(index=True))
print("\nTABLE 2 - Period\n", df2.to_string(index=True))

# --- Method I: g ---
g = 4*np.pi**2 * mean_L / mean_T**2
dg = 4*np.pi**2 * np.sqrt((delta_L/mean_T**2)**2 + (2*mean_L*delta_T/mean_T**3)**2)
print(f"\nL̄ = {mean_L:.4f} m, δL = {delta_L:.4f} m")
print(f"T̄ = {mean_T:.4f} s, δT = {delta_T:.4f} s")
print(f"g = {g:.4f} ± {dg:.4f} m/s²   ->   g = {g:.2f} ± {dg:.2f} m/s²")
print(f"%error = {(g-9.778)/9.778*100:.3f} %   |   relative unc. = {dg/g*100:.3f} %")

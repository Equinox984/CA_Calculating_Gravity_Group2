# CA Calculating Gravity Group 2 🔬
> Data analysis pipeline for measuring gravitational acceleration using a simple pendulum.

This Python project automates the calculation of the local gravitational acceleration $g$ from real experimental data collected at **Cadmus Academies Bilingual School** (Tegucigalpa, Honduras). It processes raw pendulum measurements, computes periods and uncertainties through proper error propagation, and outputs publication-ready tables matching the format of the companion LaTeX report.

## 🛠️ Technologies
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 🧠 How does it work?

The project is split into two independent notebooks, one for each experimental method:

### 📐 Method I — Fixed length
The pendulum is released from $\theta_{\max} = 5°$ at a **constant length** and the time $t_n$ for 30 oscillations is recorded across 16 trials. The notebook computes:

- **Length statistics:** mean, standard deviation, and standard deviation of the mean.
- **Period statistics:** individual periods $T_0 = t_n / 30$, mean, standard deviation, and standard deviation of the mean.
- **Total uncertainties:** combines instrumental error ($\delta L_0 = 2.3\,\text{mm}$, $\delta t_n = 0.3\,\text{s}$) with statistical uncertainty via $\delta x = \sqrt{(\delta x_{\text{med}})^2 + (\sigma_{\bar{x}})^2}$.
- **Gravitational acceleration:** $\bar{g} = 4\pi^2 \bar{L} / \bar{T}^2$ with propagated uncertainty.

### 📏 Method II — Variable length
The length is systematically shortened across 16 trials. The notebook computes:

- **Per-trial values:** $T$, $g = 4\pi^2 L / T^2$, and $\delta g$ (propagated from $\delta L$ and $\delta T$).
- **Statistics:** mean, standard deviation, and standard deviation of the mean of the 16 $g$ values.
- **Final estimate:** $\bar{g} \pm \sigma_{\bar{g}}$ as the Method II result.

### 📊 Output format
Both notebooks print:
1. A formatted table matching the style of the LaTeX report (statistical values shown in the middle row).
2. A separate summary block with the final $g \pm \delta g$, percentage error, and relative uncertainty.

## 🚀 Installation and Use

**Requirement:** Have **Python 3.x** and **Git** installed on your system.

Clone the repository and run any of the notebooks in your preferred Python environment (Jupyter, VSCode, SciServer, etc.):

1. **Clone the repository:**
```bash
   git clone https://github.com/Equinox984/CA_Calculating_Gravity_Group2.git
   cd CA_Calculating_Gravity_Group2/
```

2. **Run a notebook:**
```bash
   jupyter notebook main.ipynb     # Method I (fixed length)
   jupyter notebook main2.ipynb    # Method II (variable length)
```

3. **Data files:**
   - `table1.txt` → raw $(L_0, t_n)$ pairs for Method I (16 trials).
   - `table2.txt` → raw $(L, t_n)$ pairs for Method II (16 trials).


---

**Developed with ❤️ for the Physics 2026 Q3 Project at Cadmus Academies Bilingual School**

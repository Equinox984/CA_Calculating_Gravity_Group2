"""Physics Project"""

# Import Packages
import pandas as pd
import numpy as np

# Variables
theta_max = 5
data1_method = pd.read_csv("table1.txt", sep=r"\s+") # Create the Datafrane
df1 = pd.DataFrame(data1_method, columns = ["theta_max", "L0", "delta_L0", "Avr_L0", "sigma_L0", "sigma_Avr_L0"])

def data_analysis1(df1):
    middle = len(df1)//2
    average_lo = np.mean(df1["L0"])
    df1.loc[middle, "Av1_L0"] = average_lo
    return df1

print(data_analysis1(df1))


# print(df1)
# print(data1_method)

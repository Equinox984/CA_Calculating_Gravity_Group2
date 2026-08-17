"""Physics Project"""

# Import Packages
import pandas as pd
import numpy as np

# Variables
theta_max = 5
data1_method = pd.read_csv("table1.txt", sep=r"\s+") # Create the Datafrane
df1 = pd.DataFrame(data1_method, columns = ["theta_max", "10", "delta_10", "Avr_10", "sigma_10", "sigma_Avr_10"])
# print(data1_method)

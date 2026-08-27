# Importing the libraries

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mp



#-----------------------------------------------------------------------------------------



# Reading the tabulated data in the files
df1 = pd.read_table('data_g.txt', sep=r"\s+")  # Tabulated data in the file data_g.txt




# Overlapping all the previous plots
fig, ax = plt.subplots(figsize=(10,6))  # Defining the frame and the size for the plot



#------------------SCATTER PLOT 1-------------------

ax.plot(df1['N'], df1['g_theoretical'], label="g theoretical")
ax.errorbar(df1['N'], df1['g'], yerr=df1['delta_g'], fmt="o",
            color="purple", label="g data")



# Setting various stuffs for Scatter plot data

ax.set_title('Comparing values for g', color='black', fontsize=16)
ax.set_xlabel('Trial number (N)', fontsize=12)
ax.set_ylabel('g [ m/s^2 ]', fontsize=12)
ax.set_facecolor('floralwhite')
ax.legend(shadow=True, fancybox=True, loc="upper left")
ax.grid( )



#---------------------------------------------------------------------------------------------------


fig.tight_layout()  # Tweak spacing to prevent clipping of ylabel
plt.show()  # Showing the plot

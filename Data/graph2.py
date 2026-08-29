# Importing the libraries

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mp



#-----------------------------------------------------------------------------------------



# Final results from the report (Experimental Results section)
g_theoretical = 9.7808          # accepted local value [m/s^2]

g_m1, dg_m1 = 9.2953, 0.1288   # Method I:  averages of Tables 1 & 2
g_m2, dg_m2 = 9.4663, 0.0311   # Method II: average of Table 3




# Overlapping all the previous plots
fig, ax = plt.subplots(figsize=(10,6))  # Defining the frame and the size for the plot



#------------------THEORETICAL REFERENCE LINE-------------------

ax.axhline(g_theoretical, color="lightblue", linewidth=2, label="g theoretical")



#------------------ERROR BAR PLOTS-------------------

ax.errorbar(0, g_m1, yerr=dg_m1, fmt="o", color="orange", capsize=6, label="Method 1")
ax.errorbar(1, g_m2, yerr=dg_m2, fmt="o", color="purple", capsize=6, label="Method 2")



# Setting various stuffs for the plot

ax.set_title('Comparison of g values with error bars and theoretical line', color='black', fontsize=16)
ax.set_xticks([0, 1])
ax.set_xticklabels(['1)', '2)'])
ax.set_ylabel('g [ m/s^2 ]', fontsize=12)
ax.set_ylim(9.1, 9.9)
ax.set_facecolor('floralwhite')
ax.legend(shadow=True, fancybox=True, loc="upper left")
ax.grid( )



#---------------------------------------------------------------------------------------------------


fig.tight_layout()  # Tweak spacing to prevent clipping of ylabel
plt.savefig('g_comparison.png', dpi=200, bbox_inches='tight')  # saves the figure for the LaTeX report
plt.show()  # Showing the plot

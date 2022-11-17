import numpy as np
import skrf as rf
from matplotlib import pyplot as plt
from matplotlib import cm as cm
from matplotlib.colors import LogNorm  

def polar_2_rectangular(mag, angles):
    return mag * np.exp(1j*angles)

lna_2_cal = rf.Network('/Users/ricardogoncalves/Documents/GitHub/blog-sandbox/images/post15/lna_sparams_2_cal.s2p')
lna_2_cal.name = 'LNA measurement'
lna_2_cal.frequency.unit = 'ghz'

lna_sim = rf.Network('/Users/ricardogoncalves/Documents/GitHub/blog-sandbox/images/post15/analysis_bfp740f.s2p')
lna_sim.name = 'LNA simulation'
lna_sim.frequency.unit = 'ghz'

antenna = rf.Network('/Users/ricardogoncalves/Documents/GitHub/blog-sandbox/images/post15/gnss_antenna.s1p')
antenna.frequency.unit = 'ghz'

#gd = abs(lna_cal.s21.group_delay) *1e9

#fig, ax = plt.subplots()
#antenna.plot_s_db(label='Full Band Response')
#antenna['1.55-1.61ghz'].plot_s_db(lw=3, color = 'r', label='Band of interest')

fig, ax = plt.subplots()
lna_2_cal.plot_s_db()
lna_2_cal['1.55-1.61ghz'].plot_s_db(lw=3, color='r', label='')
ax.set_ylim((-40, 30))

fig, ax = plt.subplots()
lna_sim.plot_s_db()
lna_sim['1.55-1.61ghz'].plot_s_db(lw=3, color='r', label='')
ax.set_ylim((-40, 30))

plt.show()


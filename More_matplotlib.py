import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns


rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
'axes.titlesize' : 18}
sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)


#slice out iptg and gfp
iptg = data_txt[:,0]
gfp = data_txt[:,1]
sem = data_txt[:,2]

#Plot iptg vs gfp
# plt.semilogx(iptg, gfp, linestyle = 'none', marker = '.',
#              markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - semilog X')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()

# Plot iptg vs gfp
# plt.errorbar(iptg, gfp, yerr=sem, linestyle = 'none', marker = '.',
#              markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - Semilog X with error bars')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.xscale('log')
# plt.show()

#Practice exercise 3

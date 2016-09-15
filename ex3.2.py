import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils

rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
'axes.titlesize' : 18}
sns.set(rc=rc)

wt_file = np.loadtxt('wt_lac.csv', skiprows=3, delimiter=',')
q18a_file = np.loadtxt('q18a_lac.csv', skiprows=3, delimiter=',')
q18m_file = np.loadtxt('q18m_lac.csv', skiprows=3, delimiter=',')

plt.semilogx(wt_file[:,0], wt_file[:,1], marker='.', markersize = '20', linestyle='none')
plt.semilogx(q18a_file[:,0], q18a_file[:,1], marker='.', markersize = '20', linestyle='none')
plt.semilogx(q18m_file[:,0], q18m_file[:,1], marker='.', markersize = '20', linestyle='none')
plt.xlabel('IPTG (mM)')
plt.ylabel('Fold change')
plt.legend(('Wild type', 'Q18A type', 'Q18M type'), loc='lower right')

plt.show()

def fold_change(c, rk, kda=0.017, kdi=0.002, kswitch=5.8):
    inv_fc = 1 + (1+c/KdA)**2 * RK/((1+c/KdA)**2 + Kswitch*(1+c/KdI)**2)
    return 1/inv_fc

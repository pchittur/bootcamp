import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils
import pandas as pd
import bootcamp_utils

sns.set()
"""PART 1"""
# df = pd.read_csv('finches_data.csv', comment='#')
# fortis_depth = df.loc[((df['year']==1987) & (df['species']=='fortis')),'depth']
# scandens_depth = df.loc[((df['year']==1987) & (df['species']=='scandens')),'depth']
# x_f, y_f = bootcamp_utils.ecdf(fortis_depth)
# x_s, y_s = bootcamp_utils.ecdf(scandens_depth)
#
# plt.plot(x_f, y_f, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.plot(x_s, y_s, marker ='.', linestyle='none', markersize=20, alpha=0.5)
# plt.xlabel('Beak size')
# plt.ylabel('eCDF')
# plt.xlim(6.5,14)
# plt.ylim(-0.1,1.1)
# plt.legend(('fortis', 'scandens'), loc='lower right')
# plt.savefig('finches_beakdepth.svg')
# plt.show()
"""PART 2"""
# df = pd.read_csv('finches_data.csv', comment='#')
# fortis_length = df.loc[((df['year']==1987) & (df['species']=='fortis')),'length']
# scandens_length = df.loc[((df['year']==1987) & (df['species']=='scandens')),'length']
# x_f, y_f = bootcamp_utils.ecdf(fortis_length)
# x_s, y_s = bootcamp_utils.ecdf(scandens_length)
#
# plt.plot(x_f, y_f, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.plot(x_s, y_s, marker ='.', linestyle='none', markersize=20, alpha=0.5)
# plt.xlabel('Beak size')
# plt.ylabel('eCDF')
# plt.xlim(8,17)
# plt.ylim(-0.1,1.1)
# plt.legend(('fortis', 'scandens'), loc='lower right')
# plt.savefig('finches_beaklength.svg')
# plt.show()
"""PART 3"""
df = pd.read_csv('finches_data.csv', comment='#')
fortis_length = df.loc[((df['year']==2012) & (df['species']=='fortis')),'length']
fortis_depth = df.loc[((df['year']==2012) & (df['species']=='fortis')),'depth']
scandens_length = df.loc[((df['year']==2012) & (df['species']=='scandens')),'length']
scandens_depth = df.loc[((df['year']==2012) & (df['species']=='scandens')),'depth']

plt.plot(fortis_length, fortis_depth, marker='.', linestyle='none', markersize=20, alpha=0.5, color = 'blue')
plt.plot(scandens_length, scandens_depth, marker ='.', linestyle='none', markersize=20, alpha=0.5, color='red')
plt.xlabel('Beak length')
plt.ylabel('Beak depth')
plt.xlim(8,17)
plt.ylim(6,13)
plt.legend(('fortis', 'scandens'), loc='lower right')
plt.savefig('finches_lengthvdepth2012.svg')
plt.show()

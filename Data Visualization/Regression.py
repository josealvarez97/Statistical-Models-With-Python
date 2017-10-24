import numpy as np
import matplotlib.pyplot as plt 


weights = [0,1,3,4,5,8]
heights = [2,1,3,4,6,8]

fit = np.polyfit(weights,heights,1)
fit_fn = np.poly1d(fit)

plt.plot(weights,heights,'yo',weights,fit_fn(weights),'--k')
#https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib
plt.xticks(np.arange(min(weights),max(weights),1.5))
plt.show()
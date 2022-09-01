# crowd computing

import statistics
from statistics import mean
import matplotlib.pyplot as plt
estimates=[30,45,46,60,50,56,57,48,29,10,9,30,29,0,78,90,39,29,40,38,58,60,80,89,30,28,19,20,30,40]
y = []
estimates.sort()
tv= int(len(estimates) *0.1)

#for removing 10 % of smallest value
estimates = estimates[tv:]
#for removing 10 % of largest value
estimates = estimates[:len(estimates)-tv]
print(mean(estimates))

#for ploting
for i in range (len(estimates)):
    y.append(5)
plt.plot(estimates,y,"r--")

plt.plot([statistics.mean(estimates)],[5],'ro')
plt.plot([statistics.median(estimates)],[5],'bs')
plt.plot([45],[5],'g^')       



#another way
#for trim value

from statistics import mean
from scipy import stats
estimates=[30,45,46,60,50,56,57,48,29,10,9,30,29,0,78,90,39,29,40,38,58,60,80,89,30,28,19,20,30,40]
estimates.sort()
#for trim mean
m= stats.trim_mean(estimates,0.1)
print(m)

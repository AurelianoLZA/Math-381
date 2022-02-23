from nonlinear import *
import matplotlib.pyplot as plt


# res_min, res_max = play(2)
# print(res_min)
# print(res_max)

fig,ax = plt.subplots()
x = list(range(1,3))
ans = []
for rate in range(1,11): # rate from 1 to 10
    res_min,res_max = play(rate)
    ans.append([res_min,res_max])

y = []
for i in range(len(ans)):
    avg = (ans[i][1] - ans[i][0])/2
    y.append(avg)

yerr = np.array(ans[:,1]) - np.array(y[:])

ax.errorbar(x,y,yerr,fmt='none')
fig.show()

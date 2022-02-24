# from nonlinear import  *
# import matplotlib.pyplot as plt
# import statistics
# from math import sqrt
#
#
# def plot_confidence_interval(x, values, z=1.96, color='#2187bb', horizontal_line_width=0.25):
#     mean = statistics.mean(values)
#     stdev = statistics.stdev(values)
#     confidence_interval = z * stdev / sqrt(len(values))
#
#     left = x - horizontal_line_width / 2
#     top = mean - confidence_interval
#     right = x + horizontal_line_width / 2
#     bottom = mean + confidence_interval
#     plt.plot([x, x], [top, bottom], color=color)
#     plt.plot([left, right], [top, top], color=color)
#     plt.plot([left, right], [bottom, bottom], color=color)
#     plt.plot(x, mean, 'o', color='#f44336')
#
#     return mean, confidence_interval
#
#
# x =  np.linspace(0.5,5.5,6)
# ans = []
# for rate in x:
#     val = play(rate)
#     print("rate is {rate} and the result is {val}")
#     ans.append(val)
#
# plt.title('Confidence Interval')
# for i in range(len(ans)):
#     plot_confidence_interval(i+1,np.array(ans)[i])
#
# plt.xlabel("value of b")
# plt.ylabel("winning probability")
# plt.savefig("strat3_conf_interval_for_diff_b_version2")
# plt.show()
#
#

from nonlinear import *
res = play()
print(res)
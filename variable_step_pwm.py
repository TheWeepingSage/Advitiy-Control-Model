import numpy as np
import math as math
import actuator as act
import matplotlib.pyplot as plt

v_duty_cycle = np.array([.2, 0.5, .9])
"""
i_applied = act.getCurrentList(0.00001, v_duty_cycle)

plt.plot(i_applied[:, 0], i_applied[:, 1], 'r')
plt.plot(i_applied[:, 0], i_applied[:, 2], 'b')
plt.plot(i_applied[:, 0], i_applied[:, 3], 'g')
plt.show()
"""
t_p = 1/act.PWM_FREQUENCY   #time period of one cycle
dt_p = np.zeros(3)
v_duty_cycle = np.array([.2, 0.5, .9])
for i in range(3):
    dt_p[i] = v_duty_cycle[i] * t_p     #time for which the voltage is high per cycle
n = 100  #sample points per cycle/2
step_h = dt_p/n  #step size for high-voltage sampling
step_l = (t_p-dt_p)/n       #step size for low-voltage sampling
num_cycles = int(act.CONTROL_STEP/t_p)
num_read = 20*num_cycles        #total number of readings
i_applied = np.zeros((num_read, 6))     #six coloumns, the first three for sampling time, the next three for the current at that time
i_applied[0, 0:3] = step_h[0:3]     #initialising the time
for i in range(0, 3):
    for k in range(1, 10):
        i_applied[k, i] = i_applied[k-1, i] + step_h[i]     #setting the time for the high cycle
    for k in range(0, 10):
        i_applied[k+10, i] = i_applied[k+9, i] + step_l[i]      #setting the time for the low cycle
    i_applied[0:10, i+3] = (act.PWM_AMPLITUDE/act.RESISTANCE)*(1-np.exp(-act.RESISTANCE/act.INDUCTANCE*i_applied[0:10, i]))     #V-IR = (V0-I0R)exp(-Rt/L)
    i_applied[10:20, i+3] = i_applied[9, i+3]*np.exp(-act.RESISTANCE/act.INDUCTANCE*i_applied[10:20, i])        #I0*exp(-Rt/L)
    plt.plot(i_applied[0:20, i], i_applied[0:20, i+3])      #show values

plt.show()
print(math.exp(act.RESISTANCE))
"""
for i in range (0,3):
    for k in range (0,20):
        print (i," " ,k)
        print(i_applied[k,i])
"""
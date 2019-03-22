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
n = 10  #sample points per cycle/2
num_cycles = int(act.CONTROL_STEP/t_p)
num_read = 2*n*num_cycles        #total number of readings
i_applied = np.zeros((num_read, 6))     #six coloumns, the first three for sampling time, the next three for the current at that time
for j in range(0, 3):       #setting the time for:
    i_applied[0:n, j] = np.linspace(dt_p[j]/n, dt_p[j], n)   #first cycle (high)
    i_applied[n:2*n, j] = np.linspace((t_p-dt_p[j])/n, (t_p-dt_p[j]), n)        #first cycle (low)
    for i in range(1, num_cycles):
        i_applied[2*n*i:2*n*(i+1), j] = i_applied[2*n*(i-1):2*n*i, j]       #remaining cycles

for i in range(0, 3):
    i_applied[0:n, i+3] = (act.PWM_AMPLITUDE/act.RESISTANCE)*(1-np.exp(-act.RESISTANCE/act.INDUCTANCE*i_applied[0:n, i]))     #V-IR = (V0-I0R)exp(-Rt/L)
    i_applied[n:2*n, i+3] = i_applied[n-1, i+3]*np.exp(-act.RESISTANCE/act.INDUCTANCE*i_applied[n:2*n, i])        #I0*exp(-Rt/L)
plt.plot(i_applied[0:2*n, 0:3], i_applied[0:2*n, 3:6])      #show values
plt.show()

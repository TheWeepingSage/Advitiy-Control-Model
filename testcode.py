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
dt_p = np.zeros(3)
t_p = 1/act.PWM_FREQUENCY
v_duty_cycle = np.array([.2, 0.5, .9])
for i in range(3):
    dt_p[i] = v_duty_cycle[i] * t_p
n = 10
step_h = dt_p/n
step_l = (t_p-dt_p)/n
num_cycles = int(act.CONTROL_STEP/t_p)
num_read = 20*num_cycles
i_applied = np.zeros((num_read, 6))
i_applied[0, 0] = 0
for i in range(0, 3):
    for k in range(1, 10):
        i_applied[k, i] = i_applied[k-1, i] + step_h[i]
        i_applied[k+10, i] = i_applied[k+9, i] + step_l[i]
    i_applied[0:9, i+3] = (act.PWM_AMPLITUDE/act.RESISTANCE)*(1-math.exp(-act.RESISTANCE/act.INDUCTANCE)*np.exp(i_applied[0:9, i]))
    #i_applied[10:19, i+3] = i_applied[9,i]*np.exp(-act.RESISTANCE/act.INDUCTANCE*i_applied[10:19, i])
    plt.plot(i_applied[0:9, i], i_applied[0:9, i+3])
plt.show()

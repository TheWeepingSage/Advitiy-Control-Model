import numpy as np
import matplotlib.pyplot as plt
from constants_1U import RESISTANCE, INDUCTANCE, PWM_AMPLITUDE, PWM_FREQUENCY, CONTROL_STEP


def vstepPWM(v_duty_cycle, n):
    t_p = 1/PWM_FREQUENCY   #time period of one cycle
    dt_p = np.zeros(3)
    dt_p[0:3] = v_duty_cycle[0:3] * t_p     #time for which the voltage is high per cycle
    num_cycles = int(CONTROL_STEP/t_p)
    num_read = 2*n*num_cycles        #total number of readings
    i_applied = np.zeros((num_read, 4))     #six coloumns, the first three for sampling time, the next three for the current at that time
    for i in range(0, num_cycles):
        i_applied[i*n*2:(i+1), 0] = np.linspace(t_p/n, t_p, 2*n)


def plot(i_applied, n, v_duty_cycle):
    t_p = 1 / PWM_FREQUENCY  # time period of one cycle
    num_cycles = int(CONTROL_STEP / t_p)
    num_read = 2 * n * num_cycles  # total number of readings
    plt.plot(i_applied[0:num_read+1, 0], i_applied[0:num_read+1, 3], label=v_duty_cycle[0])      #show values
    #plt.plot(i_applied[0:num_read + 1, 1], i_applied[0:num_read + 1, 4], label=v_duty_cycle[1])
    #plt.plot(i_applied[0:num_read + 1, 2], i_applied[0:num_read + 1, 5], label=v_duty_cycle[2])
    plt.xlabel('Time(s)')
    plt.ylabel('Current(amperes)')
    plt.legend(loc='upper right')
    plt.show()


v_duty_cycle = np.array([0.000001, 0.000001, 0.001])
plot(vstepPWM(v_duty_cycle, 10), 100, v_duty_cycle)

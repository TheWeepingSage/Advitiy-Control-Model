import numpy as np
from constants_1U import RESISTANCE, INDUCTANCE, PWM_AMPLITUDE, PWM_FREQUENCY, CONTROL_STEP
import math


def getEdgeCurrent(v_duty_cycle, I0):   # to return an array with current at the edges
    t_p = 1/PWM_FREQUENCY   # time period
    num_cycles = int(CONTROL_STEP/t_p)  # number of cycles=n
    dt_p = np.zeros(3)
    dt_p[0:3] = v_duty_cycle[0:3] * t_p     # time for which the voltage is high per cycle
    dt_n = np.array(t_p-dt_p[0:3])  # time for which current is low
    edgeCurrentList = np.zeros((num_cycles*2+1, 3))     # edgeCurrentList has 2n+1 rows, 3 columns for the currents
    edgeCurrentList[0, 0:3] = I0[0:3]   # setting initial value of current
    edgeCurrentList[1, 0:3] = 1/RESISTANCE * (PWM_AMPLITUDE-(PWM_AMPLITUDE-I0[0:3]*RESISTANCE)*np.exp(-RESISTANCE*dt_p[0:3]/INDUCTANCE))    # Setting value of current at first edge
    for i in range(1, num_cycles):
        edgeCurrentList[2 * i, 0:3] = edgeCurrentList[2*i-1, 0:3]*np.exp(-RESISTANCE*dt_n[0:3]/INDUCTANCE)
        edgeCurrentList[(2 * i) + 1, 0:3] = (PWM_AMPLITUDE - (PWM_AMPLITUDE - RESISTANCE*edgeCurrentList[2 * i, 0:3])*np.exp(-RESISTANCE*dt_p[0:3]/INDUCTANCE))/RESISTANCE
    edgeCurrentList[2 * num_cycles, 0:3] = edgeCurrentList[2 * num_cycles - 1, 0:3] * np.exp(-RESISTANCE * dt_n[0:3] / INDUCTANCE)  # Setting the current for the last edge
    return edgeCurrentList


def getAnalyticalCurrent(v_duty_cycle, edgeCurrentList, t):
    t_p = 1 / PWM_FREQUENCY  # time period
    dt_p = np.zeros(3)
    dt_p[0:3] = v_duty_cycle[0:3] * t_p  # time for which the voltage is high per cycle
    t_mod_tp = t % t_p  # time elapsed since last rising edge
    cur_cycle = int(t / t_p)    # gives us the index of the cycle we're in
    current_t = np.zeros(3)
    for i in range(0, 3):   # t in the comments indicates the time since last edge
        if t_mod_tp < dt_p[i]:  # if the instant lies before th falling edge
            current_t[i] = (PWM_AMPLITUDE - (PWM_AMPLITUDE - RESISTANCE * edgeCurrentList[cur_cycle*2, i])*math.exp(-RESISTANCE*t_mod_tp/INDUCTANCE)) / RESISTANCE  # I=1/R(V-(V-I0R)exp(-Rt/L))
        else:
            current_t[i] = edgeCurrentList[2*cur_cycle+1, i]*math.exp(-RESISTANCE*(t_mod_tp-dt_p[i])/INDUCTANCE)    # I = I0exp(-Rt/L)
    return current_t


def getCurrentList(v_duty_cycle, t, n, I0):
    edgeCurrentList = getEdgeCurrent(v_duty_cycle, I0)
    currentList = np.zeros((n, 3))
    for i in range(0, n):
        currentList[i, :] = getAnalyticalCurrent(v_duty_cycle, edgeCurrentList, t[i])
    return currentList

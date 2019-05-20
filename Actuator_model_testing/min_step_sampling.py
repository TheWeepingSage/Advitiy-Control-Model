import numpy as np
from constants_1U import PWM_FREQUENCY

def getTime(duty_cycle, n):
    if np.amin(duty_cycle)!=0:
        min_duty = np.abs(np.amin(duty_cycle))
        time_a = min_duty / PWM_FREQUENCY
        timeStep_h = time_a / n
        max_duty = np.abs(np.amax(duty_cycle))
        time_b = max_duty / PWM_FREQUENCY
        timeStep_l = (1 / PWM_FREQUENCY - time_b)/n
        timeArr_h = np.linspace(timeStep_h, time_b, int(time_b / timeStep_h), endpoint=True)
        timeArr_l = np.linspace(timeStep_l+time_b, 1/PWM_FREQUENCY, n, endpoint=True)
        timeArr = np.concatenate((timeArr_h, timeArr_l))
    elif duty_cycle[1] + duty_cycle[0] + duty_cycle[2] - np.amax(duty_cycle) != 0:
        min_duty = duty_cycle[1] + duty_cycle[0] + duty_cycle[2]- np.amax(duty_cycle)
        time_a = min_duty / PWM_FREQUENCY
        timeStep_h = time_a / n
        max_duty = np.abs(np.amax(duty_cycle))
        time_b = max_duty / PWM_FREQUENCY
        timeStep_l = (1 / PWM_FREQUENCY - time_b) / n
        timeArr_h = np.linspace(timeStep_h, time_b, int(time_b / timeStep_h), endpoint=True)
        timeArr_l = np.linspace(timeStep_l + time_b, 1 / PWM_FREQUENCY, n, endpoint=True)
        timeArr = np.concatenate((timeArr_h, timeArr_l))
    elif np.amax(duty_cycle)!=0:
        min_duty = np.amax(duty_cycle)
        time_a = min_duty / PWM_FREQUENCY
        timeStep_h = time_a / n
        max_duty = np.abs(np.amax(duty_cycle))
        time_b = max_duty / PWM_FREQUENCY
        timeStep_l = (1 / PWM_FREQUENCY - time_b) / n
        timeArr_h = np.linspace(timeStep_h, time_b, int(time_b / timeStep_h), endpoint=True)
        timeArr_l = np.linspace(timeStep_l + time_b, 1 / PWM_FREQUENCY, n, endpoint=True)
        timeArr = np.concatenate((timeArr_h, timeArr_l))
    else:
        timeArr = np.linspace(1 / PWM_FREQUENCY / 2 / n, PWM_FREQUENCY, 2*n, endpoint=True)
    return timeArr
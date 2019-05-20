import numpy as np
from constants_1U import PWM_FREQUENCY

def getTime(duty_cycle, n):
    min_duty = np.abs(np.amin(duty_cycle))
    max_duty = np.abs(np.amax(duty_cycle))
    time_a = min_duty / PWM_FREQUENCY
    time_b = max_duty / PWM_FREQUENCY
    timeStep_h = time_a / n
    timeStep_l = (1 / PWM_FREQUENCY - time_b)/n
    timeArr_h = np.linspace(timeStep_h, time_b, int(time_b / timeStep_h), endpoint=True)
    timeArr_l = np.linspace(timeStep_l+time_b, 1/PWM_FREQUENCY, n, endpoint=True)
    timeArr = np.concatenate((timeArr_h, timeArr_l))
    return timeArr

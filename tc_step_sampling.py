import numpy as np
from constants_1U import PWM_FREQUENCY, RESISTANCE, INDUCTANCE

def getTimeArr(duty_cycle):
    print(duty_cycle)
    peak_time = np.abs(duty_cycle)/PWM_FREQUENCY
    time_constant = INDUCTANCE / RESISTANCE * 4.606
    time_prev = np.linspace(peak_time / 4, peak_time, 3, endpoint=False)
    time_tc = np.linspace(peak_time + time_constant/3, peak_time + time_constant, 3, endpoint=True)
    time_post = np.linspace((peak_time + time_constant)/10*9 + 1/PWM_FREQUENCY/10, 1/PWM_FREQUENCY*0.9999, 10, endpoint=True)
    time_post = np.append(time_post, 1/PWM_FREQUENCY)
    time_arr = np.concatenate((time_prev, time_tc, time_post))
    time_arr = time_arr.flatten()
    time_arr = np.concatenate((time_arr, peak_time))
    print(time_arr)
    length_t = len(time_arr)
    timeArr = np.array([])
    while length_t!=0:
        min_element = np.argmin(time_arr)
        timeArr = np.append(timeArr, time_arr[min_element])
        time_arr = np.delete(time_arr, min_element)
        length_t = len(time_arr)
        print(len(timeArr))
        print(len(time_arr))
    print(timeArr)
    return timeArr
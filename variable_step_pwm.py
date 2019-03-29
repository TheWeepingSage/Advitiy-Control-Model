import numpy as np
import actuator as act
import matplotlib.pyplot as plt


def vstepPWM(v_duty_cycle, n):
    t_p = 1/act.PWM_FREQUENCY   #time period of one cycle
    dt_p = np.zeros(3)
    dt_p[0:3] = v_duty_cycle[0:3] * t_p     #time for which the voltage is high per cycle
    num_cycles = int(act.CONTROL_STEP/t_p)
    num_read = 2*n*num_cycles        #total number of readings
    i_applied = np.zeros((num_read, 6))     #six coloumns, the first three for sampling time, the next three for the current at that time
    #setting the time for:
    i_applied[0:n, 0:3] = np.linspace(dt_p[0:3]/n, dt_p[0:3], n)   #first cycle (high)
    i_applied[n:2*n, 0:3] = np.linspace((t_p-dt_p[0:3])/n, (t_p-dt_p[0:3]), n)        #first cycle (low)
    for i in range(1, num_cycles):
        i_applied[2*n*i:2*n*(i+1), 0:3] = i_applied[2*n*(i-1):2*n*i, 0:3]       #remaining cycles

    i_applied[0:n, 3:6] = (act.PWM_AMPLITUDE/act.RESISTANCE)*(1-np.exp(-act.RESISTANCE/act.INDUCTANCE*i_applied[0:n, 0:3]))     #V-IR = (V0-I0R)exp(-Rt/L)
    i_applied[n:2*n, 3:6] = i_applied[n-1, 3:6]*np.exp(-act.RESISTANCE/act.INDUCTANCE*i_applied[n:2*n, 0:3])        #I0*exp(-Rt/L)
    for j in range(1, num_cycles):
        i_applied[j*2*n:(2*j+1)*n, 3:6] = (1/act.RESISTANCE)*(act.PWM_AMPLITUDE-(act.PWM_AMPLITUDE-i_applied[j*2*n-1, 3:6]*act.RESISTANCE)*np.exp(-act.RESISTANCE/act.INDUCTANCE*i_applied[j*2*n:n*(2*j+1), 0:3]))    #I=1/R*(V-(V-I0R)*exp(-Rt/L))
        i_applied[(2*j+1)*n:(j+1)*2*n, 3:6] = i_applied[(2*j+1)*n-1, 3:6]*np.exp(-act.RESISTANCE/act.INDUCTANCE*i_applied[(2*j+1)*n:(j+1)*2*n, 0:3])  #I=I0exp(-Rt/L)

    for j in range(1, num_cycles):     #converting (time since last edge) to (absolute time)
        i_applied[j*2*n:(2*j+1)*n, 0:3] = t_p * j + i_applied[j*2*n:(2*j+1)*n, 0:3] #time in high region
        i_applied[(2*j+1)*n:(j+1)*2*n, 0:3] = i_applied[(2*j+1)*n:(j+1)*2*n, 0:3] + t_p*j + dt_p[0:3] #time in low region
    return i_applied


def plot(i_applied, n, v_duty_cycle):
    t_p = 1 / act.PWM_FREQUENCY  # time period of one cycle
    num_cycles = int(act.CONTROL_STEP / t_p)
    num_read = 2 * n * num_cycles  # total number of readings
    plt.plot(i_applied[0:num_read+1, 0], i_applied[0:num_read+1, 3], label=v_duty_cycle[0])      #show values
    plt.plot(i_applied[0:num_read + 1, 1], i_applied[0:num_read + 1, 4], label=v_duty_cycle[1])
    plt.plot(i_applied[0:num_read + 1, 2], i_applied[0:num_read + 1, 5], label=v_duty_cycle[2])
    plt.xlabel('Time(s)')
    plt.ylabel('Current(amperes)')
    plt.legend(loc='upper right')
    plt.show()


v_duty_cycle = np.array([0.0000001, 0.000001, 0.001])
plot(vstepPWM(v_duty_cycle, 10), 10, v_duty_cycle)

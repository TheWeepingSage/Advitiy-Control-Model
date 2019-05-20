import numpy as np
import matplotlib.pyplot as plt
from constants_1U import CONTROL_STEP, PWM_FREQUENCY
import analytical_act_current as aac
import class_sat
import TorqueApplied
import min_step_sampling
import tc_step_sampling

time1 = np.loadtxt("variable_step_time.csv", delimiter=",")
#time2 = np.linspace(0, CONTROL_STEP, 100001, endpoint=True)
time3 = np.linspace(0, CONTROL_STEP, 1000001, endpoint=True)

sat = class_sat.Satellite(np.array([0, 0, 0, 1, 0, 0, 0]), 0)

sat.setRequiredTorque(0)
Mag_i = np.array([1, 1, 1])*1e-4
sat.setMag_i(Mag_i)
sat.setPos(np.array([1, 1, 1]))
sat.setVel(np.array([1, 1, 2]))
voltageRequired = TorqueApplied.ctrlTorqueToVoltage(sat)
duty_cycle = voltageRequired/3.3

n = 15

num_cycles = int(CONTROL_STEP * PWM_FREQUENCY)
num_instants = int(num_cycles * n * 2)
timeArr = tc_step_sampling.getTimeArr(duty_cycle)
time4 = np.zeros(1)
for i in range(0, num_cycles):
    time4 = np.concatenate((time4, timeArr + i / PWM_FREQUENCY))
'''
sat = class_sat.Satellite(np.array([0, 0, 0, 1, 0, 0, 0]), 0)
sat.setRequiredTorque(0)
sat.setMag_i(np.array([1, 1, 1])*1e-4)
sat.setPos(np.array([1, 1, 1]))
sat.setVel(np.array([1, 1, 2]))

voltage = TorqueApplied.ctrlTorqueToVoltage(sat)
duty_cycle = voltage/3.3
'''

I0 = np.zeros(3)


current1 = aac.getCurrentList(duty_cycle, time1, len(time1), I0)
#current2 = aac.getCurrentList(duty_cycle, time2, len(time2), I0)
current3 = aac.getCurrentList(duty_cycle, time4, len(time4), I0)

current2 = aac.getCurrentList(duty_cycle, time3, len(time3), I0)


#plt.plot(time1, current1[:, 0], label="vstep 0")
plt.plot(time3, current2[:, 0], label="uniform 0")
plt.plot(time4, current3[:, 0], label="base 0")
plt.xlim((-0.0002, 0.0011))
plt.legend()
plt.show()


#plt.plot(time1, -current1[:, 1], label="vstep 1")
plt.plot(time3, -current2[:, 1], label="uniform 1")
plt.plot(time4, -current3[:, 1], label="base 1")
plt.xlim((-0.0002, 0.0011))
plt.legend()
plt.show()


#plt.plot(time1, current1[:, 2], label="vstep 2")
plt.plot(time3, current2[:, 2], label="uniform 2")
plt.plot(time4, current3[:, 2], label="base 2")
plt.xlim((-0.0002, 0.005))
plt.legend()
plt.show()

'''
state_ustep = np.loadtxt("aac_test_uniform_steps.csv", delimiter=",")
state_vstep = np.loadtxt("aac_test_variable_step.csv", delimiter=",")
state_minstep = np.loadtxt("aac_test_min_step.csv", delimiter=",")
plt.plot(time1, state_vstep[:, 5], label="vstep state 5")
plt.plot(time2, state_ustep[:, 5], label="ustep state 5")
plt.plot(time4, state_minstep[:, 5], label="minstep state 5")
plt.legend()
plt.show()
'''

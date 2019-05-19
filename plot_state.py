import numpy as np
import matplotlib.pyplot as plt
from constants_1U import CONTROL_STEP
import analytical_act_current as aac
import class_sat
import TorqueApplied

time1 = np.loadtxt("variable_step_time.csv", delimiter=",")
time2 = np.linspace(0, CONTROL_STEP, 100001, endpoint=True)
time3 = np.linspace(0, CONTROL_STEP, 1000001, endpoint=True)

sat = class_sat.Satellite(np.array([0, 0, 0, 1, 0, 0, 0]), 0)
sat.setRequiredTorque(0)
sat.setMag_i(np.array([1, 1, 1])*1e-4)
sat.setPos(np.array([1, 1, 1]))
sat.setVel(np.array([1, 1, 2]))

voltage = TorqueApplied.ctrlTorqueToVoltage(sat)
duty_cycle = voltage/3.3
I0 = np.zeros(3)

current1 = aac.getCurrentList(duty_cycle, time1, len(time1), I0)
current2 = aac.getCurrentList(duty_cycle, time2, len(time2), I0)
current3 = aac.getCurrentList(duty_cycle, time3, len(time3), I0)

'''
plt.plot(time1, current1[:, 0], label="vstep 0")
plt.plot(time2, current2[:, 0], label="uniform 0")
plt.plot(time3, current3[:, 0], label="base 0")
plt.xlim((-0.0002, 0.0011))
plt.legend()
plt.show()
'''

plt.plot(time1, -current1[:, 1], label="vstep 1")
plt.plot(time2, -current2[:, 1], label="uniform 1")
plt.plot(time3, -current3[:, 1], label="base 1")
plt.xlim((-0.0002, 0.0011))
plt.legend()
plt.show()

'''
plt.plot(time1, current1[:, 2], label="vstep 2")
plt.plot(time2, current2[:, 2], label="uniform 2")
plt.plot(time3, current3[:, 2], label="base 2")
plt.xlim((-0.0002, 0.005))
plt.legend()
plt.show()
'''
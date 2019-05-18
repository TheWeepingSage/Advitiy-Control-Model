import numpy as np
import matplotlib.pyplot as plt
from constants_1U import CONTROL_STEP
import analytical_act_current as aac

curr1 = np.loadtxt("aac_test_variable_step.csv", delimiter=",")
curr2 = np.loadtxt("aac_test_uniform_steps.csv", delimiter=",")
time1 = np.loadtxt("variable_step_time.csv", delimiter=",")
time2 = np.linspace(0, CONTROL_STEP, 100001, endpoint=True)
time1 = time1.transpose()
time2 = time2.transpose()
current1 = aac.getCurrentList(np.array([7.93445021e-04, -7.93445021e-04, 1.86250631e-19]), time1, 30001, np.zeros(3))
current2 = aac.getCurrentList(np.array([7.93445021e-04, -7.93445021e-04, 1.86250631e-19]), time2, 100001, np.zeros(3))


plt.plot(time1, curr1[6], label="vstep state 6")
plt.plot(time2, curr2[6], label="uni state 6")
plt.plot(time1, curr1[5], label="vstep state 5")
plt.plot(time2, curr2[5], label="uni state 5")
plt.plot(time1, curr1[4], label="vstep state 4")
plt.plot(time2, curr2[4], label="uni state 4")
plt.legend()
plt.show()

plt.plot(time1, curr1[2], label="vstep state 2")
plt.plot(time2, curr2[2], label="uni state 2")
plt.legend()
plt.show()
plt.plot(time1, curr1[1], label="vstep state 1")
plt.plot(time2, curr2[1], label="uni state 1")
plt.plot(time1, curr1[0], label="vstep state 0")
plt.plot(time2, curr2[0], label="uni state 0")
plt.legend()
plt.show()
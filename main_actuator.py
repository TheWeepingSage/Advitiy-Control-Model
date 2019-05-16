import numpy as np
import dynamics_actuator
import solver
import class_sat
import analytical_act_current as aac
import TorqueApplied
from constants_1U import CONTROL_STEP

sat = class_sat.Satellite(np.array([0, 0, 0, 1, 0, 0, 0]), 0)
time = np.linspace(0, CONTROL_STEP, 100001, endpoint=True)

sat.setRequiredTorque(0)

voltageRequired = TorqueApplied.ctrlTorqueToVoltage(sat)
duty_cycle = voltageRequired/3.3
current_applied = np.zeros((3,3))
edgeCurrentList = aac.getEdgeCurrent(duty_cycle, np.zeros(3))
state_array = np.zeros((100001, 3))
for i in range(0, 100000):
    current_applied = aac.getCurrentList(duty_cycle, np.linspace(time[i], time[i+1], 3, endpoint=True), np.zeros(3))
    torque_applied = TorqueApplied.currentToTorque(current_applied, sat)
    solver.rk4Quaternion(sat, dynamics_actuator.x_dot_BO, time[1]-time[0], torque_applied)
    state_array[i, :] = sat.getState()

np.savetxt("aac_test.csv", state_array, delimiter=",")

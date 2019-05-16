import numpy as np
import dynamics_actuator
import solver
import class_sat
import analytical_act_current
import TorqueApplied
from constants_1U import CONTROL_STEP

sat = class_sat.Satellite(np.array([0, 0, 0, 1, 0, 0, 0]), 0)
time = np.linspace(0, CONTROL_STEP, 100000, endpoint=False)


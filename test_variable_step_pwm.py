import variable_step_pwm as vsp
import numpy as np
from ddt import ddt, data, unpack
import unittest

@ddt

class testVstepPwm(unittest.TestCase):

    def test_vstepPWM(self):
        duty_cycle = np.array([0.1,0.001,0.00001])
        n = 10
        currentList = vsp.vstepPWM(duty_cycle, n)

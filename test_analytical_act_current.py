from analytical_act_current_test import getEdgeCurrent, getCurrentList, getAnalyticalCurrent
import numpy as np
from ddt import ddt, data, unpack
import unittest

@ddt

class TestCurrents(unittest.TestCase):

    def test_edges(self):
        duty_cycle = np.array([0, 0 , 0])
        I0 = np.array([0, 0, 1])
        current = getEdgeCurrent(duty_cycle, I0)
        testArr = np.array([current[0, 2], current[2, 2], current[4, 2]])
        self.assertTrue(np.allclose(testArr, np.array([1, 0.367879441, 0.135335283])))

        duty_cycle = np.array([0, 0.001, 0])
        I0 = np.array([0, 0, 0])
        current = getEdgeCurrent(duty_cycle, I0)
        testArr = np.array([current[0, 1], current[1, 1], current[2, 1], current[3, 1], current[4, 1]])
        self.assertTrue(np.allclose(testArr, np.array([0, 0.0009995, 0.00036806, 0.001367195, 0.000503466])))

        duty_cycle = np.array([0, 0.5, 0])
        I0 = np.array([0, 0, 0])
        current = getEdgeCurrent(duty_cycle, I0)
        testArr = np.array([current[0, 1], current[1, 1], current[2, 1], current[3, 1], current[4, 1]])
        self.assertTrue(np.allclose(testArr, np.array([0, 0.39346934, 0.2386512184, 0.5382186222, 0.32644609])))

    def testac(self):
        duty_cycle = np.array([0, 0.001, 0])
        I0 = np.array([0, 0, 0])
        edgecurrent = getEdgeCurrent(duty_cycle, I0)
        self.assertAlmostEqual(getAnalyticalCurrent(duty_cycle, edgecurrent, 0.0005)[1], 0.000499875, 7)
        self.assertAlmostEqual(getAnalyticalCurrent(duty_cycle, edgecurrent, 0.501)[1], 0.0006062274954, 7)
        self.assertAlmostEqual(getAnalyticalCurrent(duty_cycle, edgecurrent, 1.0005)[1], 0.0008677544773, 7)
        self.assertAlmostEqual(getAnalyticalCurrent(duty_cycle, edgecurrent, 1.501)[1], 0.0008292461277, 7)
        self.assertAlmostEqual(getAnalyticalCurrent(duty_cycle, edgecurrent, 0)[1], 0, 7)

    def testlist(self):
        duty_cycle = np.array([0, 0.001, 0])
        I0 = np.array([0, 0, 0])
        time = np.array([0, 0.001, 1, 1.001, 2, 0.0005, 0.501, 1.0005, 1.501])
        current = getCurrentList(duty_cycle, time, 9, I0)
        self.assertTrue(np.allclose(current[:, 1], np.array([0, 0.0009995, 0.00036806, 0.001367195, 0.000503466, 0.000499875, 0.0006062274954, 0.0008677544773, 0.0008292461277])))

if __name__=='__main__':
	unittest.main(verbosity=2)
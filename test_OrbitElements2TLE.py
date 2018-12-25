import OrbitElements2TLE as ot	#module to be tested
import unittest	#testing library
from ddt import ddt,file_data,unpack,data
import numpy as np
from datetime import *
from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv

class TestLength(unittest.TestCase):
    def test_length_line1(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.line1),69)
    def test_length_line2(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.line2),69)
                    

@ddt
class TestSymbol(unittest.TestCase):
    @data(1,8,17,32,43,52,61,63)
    def test_space_line1(self,value):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(ot.line1[value],' ')
                    
    @data(1,7,16,25,33,42,51)
    def test_space_line2(self,value):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(ot.line2[value],' ')

    @data(23,34,)
    def test_decimal_line1(self,value):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(ot.line1[value],'.')
    
    @data(11,20,37,46,54)
    def test_decimal_line2(self,value):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(ot.line2[value],'.')

    @data(33,44,50,53,59)
    def test_sign_line1(self,value):	#test the location of sign in TLE's line1 
                    #self.assertEqual((ot.line1[value],'2') or (ot.line1[value],'-'))
                    #self.assertEqual('3','3' and '4','5')
                    self.assertTrue((ot.line1[value]=='+') or (ot.line1[value]=='-')) 

                
class TestRange(unittest.TestCase):
        def test_inclination(self):	# range of inclination in degrees
             inclination= float(ot.line2[8:16]) ## in deg    
             self.assertTrue((inclination<360) and (inclination>0))
        def test_ran(self):	#  range of right ascension in degrees
             ran= float(ot.line2[17:25]) 
             self.assertTrue((ran<360) and (ran>0))
        def test_argP(self):	#  range of argument of perigee in degrees
             argP= float(ot.line2[34:42])
             self.assertTrue((argP<360) and (argP>0))
        def test_argP(self):	#  range of meanAnamoly in degrees
             meanAnamoly= float(ot.line2[43:51])
             self.assertTrue((meanAnamoly<360) and (meanAnamoly>0))
                     
class ElementLength(unittest.TestCase):
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.SatNo),5)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.ClassNo),1)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.EpoachYr),2)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.Epoach),12)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.DMeanMotion),10)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.DDMeanMotion),7)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.BStar),8)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.EphemerisT),1)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.ElementSetNo),4)
                    
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.SanNo2),5)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.Incl_deg),8)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.RAAN_deg),8)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.Eccen),7)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.ArgP),8)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.MeanAnamoly_deg),8)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.MeanMo),11)
        def test_length_SatNo(self):	#test the location of space in TLE's line1 and line2
                    self.assertEqual(len(ot.RevNo),5)
        

	

if __name__=='__main__':
	unittest.main(verbosity=2)
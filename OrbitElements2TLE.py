import numpy as np
#REFER https://en.wikipedia.org/wiki/Two-line_element_set
line1 = '1 NNNNNC NNNNNAAA NNNNN.NNNNNNNN +.NNNNNNNN +NNNNN-N +NNNNN-N N NNNNN'
line2 = '2 NNNNN NNN.NNNN NNN.NNNN NNNNNNN NNN.NNNN NNN.NNNN NN.NNNNNNNNNNNNNN'
line1 = list(line1)
print line1
print len(line1)
#1	01-01	Line number	
#2	03-07	Satellite number	25544
SatNo = '25544'
line1[2:7] = SatNo
#3	08-08	Classification (U=Unclassified)	U
ClassNo = 'U'
line1[7]= ClassNo
#4	10-11	International Designator (Last two digits of launch year)	98
LaunchYear='98'
line1[9:11]=LaunchYear
#5	12-14	International Designator (Launch number of the year)	067
LaunchNumber='067'
line1[11:14]=LaunchNumber
#6	15-17	International Designator (piece of the launch)	A
LaunchPiece='A  '
line1[14:17]=LaunchPiece
#7	19-20	Epoch Year (last two digits of year)	08
EpoachYr = '08'
line1[18:20]=EpoachYr
#8	21-32	Epoch (day of the year and fractional portion of the day)	264.51782528 ##three number than decimal then 8 numbers
Epoach = '264.51782528'
line1[20:32]=Epoach
#9	34-43	First Time Derivative of the Mean Motion divided by two [11]	-.00002182
DMeanMotion ='-.00002182'
line1[33:43]=DMeanMotion
#10 45-52	Second Time Derivative of Mean Motion divided by six (decimal point assumed)	00000-0
DDMeanMotion = '+00000-0' 
line1[44:52] = DDMeanMotion
#11	54-61	BSTAR drag term (decimal point assumed) [11]	-11606-4
BStar = '-11606-4'
line1[53:61] = BStar
#12	63-63	The number 0 (originally this should have been "Ephemeris type")	0
EphemerisT= '0'
line1[62] = EphemerisT
#13	65-68	Element set number. Incremented when a new TLE is generated for this object.[11]	292
ElementSetNo = '0292'
line1[64:68] = ElementSetNo
#14	69-69	Checksum (modulo 10)	7

line1 = ''.join(line1)
print line1
print len(line1)
###############################

line2 = list(line2)
print line2
print len(line2)

#1	01-01	Line number	2
#2	03-07	Satellite number	25544
SanNo2 = '25544'
line2[2:7] = SanNo2
#3	09-16	Inclination (degrees)	51.6416
Incl_deg = '051.6416'
line2[8:16] = Incl_deg
#4	18-25	Right ascension of the ascending node (degrees)	247.4627
RAAN_deg = '247.4627'
line2[17:25] = RAAN_deg
#5	27-33	Eccentricity (decimal point assumed)	0006703
Eccen = '0006703'
line2[26:33] = Eccen
#6	35-42	Argument of perigee (degrees)	130.5360
ArgP =  '130.5360'
line2[34:42] = ArgP
#7	44-51	Mean Anomaly (degrees)	325.0288
MeanAnamoly_deg = '325.0288'
line2[43:51] = MeanAnamoly_deg
#8	53-63	Mean Motion (revolutions per day)	15.72125391
MeanMo= '15.72125391'
line2[52:63] = MeanMo
#9	64-68	Revolution number at epoch (revolutions)	56353
RevNo = '56353'
line2[63:68] = RevNo
line2 = ''.join(line2)
print line2
print len(line2)
#10	69-69	Checksum (modulo 10)	7

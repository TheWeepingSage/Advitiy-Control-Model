import numpy as np
import constants_1U as C1U
import sgp 
import TLE2OrbitElements as TOE
import os


def filename(TT,MS,MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg,fname_load):
    os.chdir('data_files/')
    #This function give variable naming to the sgp output .csv file. The filename would contain major
    #orbit elements those was used in creating the sgp output.
    
    
    try:
        a_file = open(fname_load, 'rb')
        my_input = a_file
        a_file.close
        loaded = True
        print ('File found: ' + fname_load)
        return loaded
    except IOError as e:    #if file doesnot exist already it sets flag and calculates it so you don't have to manually check
        loaded = False
        print('No existing file could be opened.')
        return loaded
    '''
    if loaded == False:
        my_input = sgp_output
         np.savetxt(fname_load,my_input, delimiter=",")
    '''

#Function getOrbitdata_TLE calls sgp_fn and create postion and velocity of satellite at different time instants.
# First It takes TLE elements (line1 and line2) from constant file then using TLE2OE it gets relevent orbital parameters  
#and then call sgp_fn. 
def getOrbitData_TLE():
    line1 = C1U.LINE1
    line2 = C1U.LINE2
    MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg,DMeanMotion,DDMeanMotion,BStar = TOE.TLE2OE(line1,line2)


    dT = C1U.dT ## dT is in seconds.
    TT = C1U.TT ## total time in minutes
    MS = C1U.MODEL_STEP ## MS in seconds
    #filename(TT,MS,MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg)
    fname_load = "sgp_i_TT%g_MS%g_MMo%g_Ecc%g_Incl%g_MAnamoly%g_ArgP%g_Raan%g.csv" \
    %(TT,MS,MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg)    #load from this file
    
    if filename(TT,MS,MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg,fname_load) == False :
        sgp_output = np.zeros([ len(dT),7], dtype = 'float')
        sgp_output[:,0],sgp_output[:,1:4],sgp_output[:,4:7] = \
        sgp.sgp_fn(dT,MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg,DMeanMotion,DDMeanMotion,BStar)
        np.savetxt(fname_load,sgp_output, delimiter=",")
        print ('csv file is created by using TLE data')


#Function getOrbitData_OrbitELement calls sgp_fn and create postion and velocity of satellite at different time instants.
# First It takes orbitalelements from cosntant file  then call sgp_fn.
def getOrbitData_OrbitElement():
    MeanMo = C1U.MeanMo 
    Eccen = C1U.Eccen 
    Incl_deg  = C1U.Incl_deg
    MeanAnamoly_deg = C1U.MeanAnamoly_deg
    ArgP =C1U.ArgP 
    RAAN_deg = C1U.RAAN_deg
    DMeanMotion = C1U.DMeanMotion
    DDMeanMotion = C1U.DDMeanMotion
    BStar = C1U.BStar
    
    dT = C1U.dT ## dT is in seconds.
    TT = C1U.TT ## total time in minutes
    MS = C1U.MODEL_STEP ## MS in seconds
    #filename(TT,MS,MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg)
    fname_load = "sgp_i_TT%g_MS%g_MMo%g_Ecc%g_Incl%g_MAnamoly%g_ArgP%g_Raan%g.csv" \
    %(TT,MS,MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg)    #load from this file
    

    if filename(TT,MS,MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg,fname_load) == False :
        sgp_output = np.zeros([ len(dT),7], dtype = 'float')
        sgp_output[:,0],sgp_output[:,1:4],sgp_output[:,4:7] = \
        sgp.sgp_fn(dT,MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg,DMeanMotion,DDMeanMotion,BStar)
        np.savetxt(fname_load,sgp_output, delimiter=",")
        print ('csv file is created by using orbital elements')

### Call getOrbitData_TLE or getOrbitData_OrbitELement
# Uncomment whichever is required
#getOrbitData_TLE()
getOrbitData_OrbitElement()
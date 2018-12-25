import numpy as np
from datetime import *
import math
import constants_1U as C1U


def sgp_fn(dT,MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg,DMeanMotion,DDMeanMotion,BStar):
    pi = math.pi
    dT = dT/60.0 # the sgp require time in minutes. the dT imported from getorbitdata is in seconds.
    n0 = 2.0*pi*MeanMo/1440.0
    e0 = Eccen #   
    i0 = pi*Incl_deg/180.0 #inclination in rad
    M0 = pi*MeanAnamoly_deg/180.0 #Mean Anamoly in rad
    w0 = pi*ArgP/180.0 #Argument of perigee in rad
    Ohm0 = pi*RAAN_deg/180.0 #  Right ascension of the ascending node (rad)
    dn0 = 2.0*2.0*pi*DMeanMotion/(1440.0**2.0) # First time derivative of mean motion(rad/min^2)
    ddn0 = 6.0*2.0*pi*DDMeanMotion/(1440.0**3.0)
    Bstar=BStar
    M_EARTH = 5.972e24; #mass of earth, kg
    R_EARTH = 6378.135; #radius of earth,   ## km
    GM = 398603e9;
    ke = 0.0743669161 #converted to er/min ^3/2
    #aE = 6378160; % equatorial radius of the Earth
    aE = 1 #give result in Earth radii
    min_per_day = 1440.0
    sec_per_day = 86400.0
    J2 = 5.413080e-4 * 2.0; #second gravitational zonal harmonic of the Earth
    J3 = -0.253881e-5; #third gravitational zonal harmonic of the Earth
    J4 = -0.62098875e-6 * 8.0/3.0; #fourth gravitational zonal harmonic of the Earth
    ### Local COnstants
    a1 = (ke/n0)**(2.0/3.0)
    delta1 = 3.0/4.0 * J2 * (aE/a1)**2.0 * (3.0*((math.cos(i0))**2.0)-1.0)/((1-e0**2.0)**(3.0/2.0));
    a0 = a1 * (1.0 - (1.0/3.0)*delta1 - delta1**2.0 - (134.0/81.0)*delta1**3.0);
    p0 = a0 * (1.0 - e0**2.0);
    q0 = a0 * (1-e0);
    L0 = M0 + w0 + Ohm0;
    dOhm = - (3.0/2.0) * J2 * (aE/p0)**2.0 * n0 * math.cos(i0);
    dw = (3.0/4.0) * J2 * (aE/p0)**2.0 * n0 * (5.0*(math.cos(i0))**2.0-1.0);
    ###Secular effects of drag and gravitation
    a = a0 * np.power((np.divide( n0 , (n0 + 2*(dn0/2.0)*(dT) + 3.0*(ddn0/6.0)* np.power(dT,2.0)))), (2.0/3.0)) # vector
    e = np.zeros(len(dT),dtype = 'float') #vector
    
    for i in range (0, len(a)):
        if a[i] > q0 :
            e[i] = 1.0- q0/a[i]
        else:
            e[i] = 1e-6 ## 10^(-6)  
    
    p = np.multiply(a, (1-np.power(e,2.0)))
    OhmS0 = Ohm0 + dOhm * dT # vector
    wS0 = w0 + dw *  (dT) # vector
    Ls = (L0 + (n0 + dw + dOhm)*(dT) + dn0/2.0 * (np.power(dT,2.0)) + ddn0/6.0 * (np.power(dT,3.0))) % (2*math.pi) # vector
    
    
    ### Long Term Periodic Effects
    axNSL = np.multiply(e ,np.cos(wS0)) #vector
    ayNSL = np.multiply(e, np.sin(wS0)) - 1.0/2.0 * J3/J2 * np.divide(aE,p )* math.sin(i0) # % vector
    L = (Ls - 1.0/4.0 * J3/J2 * np.multiply(np.divide(aE,p) , axNSL) * math.sin(i0) * (3.0+5.0*math.cos(i0))/(1.0+math.cos(i0)))%(2.0*math.pi)  # vector
    ### Iteration for short period periodics below...
    tol = 1.0e-12 
    U =np.mod( (L - OhmS0) ,(2.0*math.pi)) ##vector
    Ew1 = U.copy()  ## vector
    Ew2 = Ew1.copy() ## vector
    dEw = np.divide((U - np.multiply(ayNSL,np.cos(Ew1)) + np.multiply( axNSL,np.sin(Ew1)) - Ew1),(np.multiply(-ayNSL,np.sin(Ew1)) - np.multiply( axNSL, np.cos(Ew1)) + 1.0)) # vector
    
    
    for i in range(0,len(dEw)):
        if np.abs(dEw[i]) >1 :
            Ew2[i] = Ew1[i]+np.sign(dEw[i])
        else :
            Ew2[i]=Ew1[i]+dEw[i]
    
              
    for i in range (0,len(Ew1)):   
        while np.abs(dEw[i])>tol :               
            Ew1[i]=Ew2[i]
            dEw[i]=  (U[i] -ayNSL[i]*np.cos(Ew1[i])+ axNSL[i] * np.sin(Ew1[i]) - Ew1[i])/(-ayNSL[i]*np.sin(Ew1[i]) - axNSL[i]*np.cos(Ew1[i]) + 1.0)
            if np.abs(dEw[i]) >1.0:
               Ew2[i]= Ew1[i] + np.sign(dEw[i])
            else:
               Ew2[i]= Ew1[i] + dEw[i]
    
    
    ecosE =   np.multiply(axNSL, np.cos(Ew2)) + np.multiply(ayNSL,np.sin(Ew2))
    esinE =np.multiply(axNSL,np.sin(Ew2)) - np.multiply(ayNSL,np.cos(Ew2)) # vector
    SQeL = np.power(axNSL,2.0) + np.power(ayNSL,2.0)#vector
    pL = np.multiply(a,(1.0 - SQeL))
    r = np.multiply(a,(1.0 - ecosE))
    dr = ke *  np.multiply(np.divide( np.sqrt(a),r) , esinE)#; % vector
    rdv = ke * np.divide(np.sqrt(pL),r) # vector
    sinu = np.multiply(np.divide(a,r) , (np.sin(Ew2) - ayNSL - np.divide(np.multiply( axNSL, esinE),(1.0+np.sqrt(1.0-SQeL))))) # vector
    cosu = np.multiply( np.divide(a,r),(np.cos(Ew2) - axNSL + np.divide(np.multiply(ayNSL,esinE),(1.0+np.sqrt(1.0-SQeL)))))#vectro
    
    u = np.zeros(len(sinu),dtype = 'float') #vector
    for i in range(0,len(sinu)):
        u[i] = (math.atan2( sinu[i],cosu[i] )) % (2.0*math.pi) # vector
    
    ### Short Term Perturbations
    rk = r + 1.0/4.0 * J2 * np.divide(aE**2.0,pL) * np.multiply((np.sin(i0))**2.0,np.cos(2.0*u))# vector
    uk = u - 1.0/8.0 * J2 * np.power(np.divide(aE,pL),2.0) * np.multiply((7.0 * (np.cos(i0))**2.0 - 1.0) , np.sin(2.0*u))# vector
    Ohmk = OhmS0 + 3.0/4.0 * J2 * np.power(np.divide(aE,pL),2.0) * np.multiply(np.cos(i0),np.sin(2.0*u))#vector
    ik = i0 + 3.0/4.0 * J2 *  np.power(np.divide(aE,pL),2.0) * np.sin(i0) * np.multiply( np.cos(i0), np.cos(2.0*u))# vector
    
    ### Unit orientation vectors
    R = np.zeros([len(uk),3], dtype ='float')# vector
    dR = np.zeros([len(uk),3], dtype ='float')# vector
    
    for i in range(0,len(uk)):
            M_vec = np.array([ -np.sin(Ohmk[i])*np.cos(ik[i]) , np.cos(Ohmk[i])*np.cos(ik[i]), np.sin(ik[i]) ])#vector
            N_vec = np.array([ np.cos(Ohmk[i]) ,np.sin(Ohmk[i]), 0 ])# vector
            U_vec = M_vec * np.sin(uk[i]) + N_vec * np.cos(uk[i]) #vector
            V_vec = M_vec * np.cos(uk[i]) - N_vec * np.sin(uk[i])# vector
             ##Position and velocity
            R[i,:] = rk[i] * U_vec #vector
            dR[i,:] = dr[i] * U_vec + rdv[i] * V_vec #vector
            
    #### Transforming position to Cartesian coordinates in meters and velocity to meters/sec and time in seconds
    R = R * R_EARTH*1000.0 /aE # in meters
    dR = dR * R_EARTH*1000.0 / aE * min_per_day / sec_per_day;# in meters per second
    dT = dT*60.0 # converting the time in seconds for storing    
    return dT,R,dR # time|x|y|z|xdot|ydot|zdot
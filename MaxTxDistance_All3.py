#!python3

#determining maximum distance a signal will transmit

#import necessary modules
import math

#obtain parameters from user
print('What is the radio power output in dBm?')
ptx=int(input())
print('What is the estimated line/connector loss in dBm?')
ltx=int(input())
print('What is the antenna gain in dBm?')
gtx=int(input())
print('What is the antenna gain at the receiver?')
rxg=int(input())
print('What is the line/adapter loss at the receiver?')
rxl=int(input())
print('What is the frequency in MHz?')
MHz=float(input())
##Set the minimum threshold
print('What is the minimum acceptable RSSI in dBm at the RX? ie. -110 or -47')
rx_min=int(input())
rx_minNeg=rx_min-(2*rx_min) #minimum rssi should will be a negative number
pwrTotal=rx_minNeg+ptx-ltx+gtx+rxg-rxl #radio link budget and minimum RSSI 

#Building the Path Loss Variables
dist1=10**(0.05*pwrTotal+1.3775-math.log(MHz,10))
dist2=10**(0.025*pwrTotal+0.68875-0.5*math.log(MHz,10))
dist3=10**(0.02*pwrTotal+0.551-0.4*math.log(MHz,10))
if dist1 < 1000:
    print('The Maximum achieveable distance in FREESPACE (Note, this does NOT exist on Earth): \n'+str(dist1)+'m')
else:
    dist1 = dist1/1000
    print('The Maximum achieveable distance in FREESPACE (Note, this does NOT exist on Earth): \n'+str(dist1)+'km')
if dist2 < 1000:
    print('The Maximum achieveable distance in NON-FREESPACE environments: \n'+str(dist2)+'m')
else:
    dist2 = dist2/1000
    print('The Maximum achieveable distance in NON-FREESPACE environments: \n'+str(dist2)+'km')
if dist3 < 1000:
    print('The Maximum achieveable distance in URBAN environments: \n'+str(dist3)+'m')
else:
    dist3 = dist3/1000
    print('The Maximum achieveable distance in URBAN environments: \n'+str(dist3)+'km')

print('press enter to close')
input()

#notes
##given equations
#Pathloss in dBm = 20*log(d) + 20*log(f) + 32.44 (d in km and f in MHz)
#Pathloss in dBm = 20*log(d) + 20*log(f) - 27.55 (din meters and f in MHz)
##wored equations
#0.05*rx_min+1.3775-log(MHz,10)=log(dist,10)
#10**(0.05*rx_min+1.3775-log(MHz,10)=dist #FreeSpace
#10**(0.025*rx_min+0.68875-0.5*math.log(MHz,10))=dist #NonFreeSpace
#10**(0.02*rx_min+0.551-0.4*math.log(MHz,10))=dist #Urban

'''
==============================================================================
    Author:
        Mahnoor Anjum
    Description:
        Digital Modulation Techniques:
            1- Amplitude Shift Keying
            2- On Off Keying
            3- M-ary Amplitude Shift Keying
            4- Frequency Shift Keying
            5- M-ary Frequency Shift Keying
            6- Phase Shift Keying
            7- Quadrature Phase Shift Keying 
    Contact:
        manomaq@gmail.com
==============================================================================
'''
import numpy as np
import matplotlib.pyplot as plt




on1 = 1000
off1 = 0
message1 = []
for w in range(2000):
    if(w<401):
        message1.append(off1)
    elif(w>400 and w<801):
        message1.append(on1)
    elif(w>800 and w<1201):
        message1.append(off1)
    elif(w>1200 and w<1601):
        message1.append(on1)
    elif(w>1600 and w<2001):
        message1.append(on1)
on2=980
off2=20
message2 = []
for w in range(2000):
    if(w<401):
        message2.append(on2)
    elif(w>400 and w<801):
        message2.append(off2)
    elif(w>800 and w<1201):
        message2.append(on2)
    elif(w>1200 and w<1601):
        message2.append(off2)
    elif(w>1600 and w<2001):
        message2.append(on2)



x = np.arange(-100, 100, 0.1);
s = np.arange(-200, 200, 0.1);
f = np.sin(s*.4)*1000


m = []

_11=130
_10=90
_01=60
_00=20

i=0
for w,v in zip(message1,message2):
    
    try:
        prevw
        prevv
    except NameError:
        prevw = w
        prevv = v
        m.append(f[i])
        i+=1
    else:

        if (w<prevw):
            if (v==on2):
                i+=_01
            else:
                i+=_00
            prevw = w
            prevv = v
            m.append(f[i])
            i+=1
        
        elif(w>prevw):
            if (v==on2):
                i+=_11
            else:
                i+=_10
            i+=_10
            prevw = w
            prevv = v
            m.append(f[i])
            i+=1
        elif (v<prevv):
            if (w==on1):
                i+=_10
            else:
                i+=_00
            i+=_01
            prevw = w
            prevv = v
            m.append(f[i])
            i+=1
        
        elif(v>prevv):
            if (w==on1):
                i+=_11
            else:
                i+=_01
            i+=_10
            prevw = w
            prevv = v
            m.append(f[i])
            i+=1
        else:
            m.append(f[i])
            prevw = w
            prevv = v
            i+=1
      
    
plt.scatter(x,message1, label = "message", color='r')
plt.scatter(x,message2, label = "message", color='b')

plt.plot(x,m, label = "modulated signal")
plt.legend()
plt.title('QPSK')
plt.xlabel('Time')
plt.ylabel('Modulated Signal')
plt.show()


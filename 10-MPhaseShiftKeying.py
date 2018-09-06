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
            8- M-ary Phase Shift Keying
    Contact:
        manomaq@gmail.com
==============================================================================
'''
import numpy as np
import matplotlib.pyplot as plt




level1 = 200
level2 = 0
level3 = 600
level4 = 1200
message = []
for w in range(2000):
    if(w<401):
        message.append(level1)
    elif(w>400 and w<801):
        message.append(level2)
    elif(w>800 and w<1201):
        message.append(level3)
    elif(w>1200 and w<1601):
        message.append(level1)
    elif(w>1600 and w<2001):
        message.append(level4)



x = np.arange(-100, 100, 0.1);
s = np.arange(-200, 200, 0.1);
f = np.sin(s*.4)*1200

m=[]
_1 = 30
_2 = 60
_3 = 90
_4 = 120


i=0
for w in message:
    
    try:
        prev
    except NameError:
        prev = w
        m.append(f[i])
        i+=1
    else:
        if (w==prev):
            m.append(f[i])
            i+=1
        else:
            if(w==level1):
                i+=_1
            elif(w==level2):
                i+=_2
            elif(w==level3):
                i+=_3
            else:
                i+=4
            m.append(f[i])
            prev=w
            i+=1
                  
    
    
plt.scatter(x,message, label = "message", color='r')
plt.plot(x,m, label = "modulated signal")
plt.legend()
plt.title('MPSK')
plt.xlabel('Time')
plt.ylabel('Modulated Signal')
plt.show()








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
    Contact:
        manomaq@gmail.com
==============================================================================
'''
import numpy as np
import matplotlib.pyplot as plt




on = 1000
off = 0
message = []
for w in range(2000):
    if(w<401):
        message.append(off)
    elif(w>400 and w<801):
        message.append(1200)
    elif(w>800 and w<1201):
        message.append(off)
    elif(w>1200 and w<1601):
        message.append(1200)
    elif(w>1600 and w<2001):
        message.append(off)


x = np.arange(-100, 100, 0.1);
s = np.arange(-200, 200, 0.1);
f = np.sin(s*.4)*1200


m = []

_t=90
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
        elif(w>prev):
            i+=_t
            m.append(f[i])
            prev=w
            i+=1
        else:
            i-=_t
            m.append(f[i])
            prev=w
            i+=1
        
              
    
    
plt.scatter(x,message, label = "message", color='r')
plt.plot(x,m, label = "modulated signal")
plt.legend()
plt.title('PSK')
plt.xlabel('Time')
plt.ylabel('Modulated Signal')
plt.show()




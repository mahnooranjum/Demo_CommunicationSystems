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

m = np.sin(x)
m = message*m


plt.scatter(x,message, label = "message", color='r')
plt.plot(x,m, label = "modulated signal")
plt.legend()
plt.title('MASK')
plt.xlabel('Time')
plt.ylabel('Modulated Signal')
plt.show()




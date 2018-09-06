'''
==============================================================================
    Author:
        Mahnoor Anjum
    Description:
        Digital Multiplexing Techniques:
            1- Frequency Division Multiplexing
            2- Time Division Multiplexing
    Contact:
        manomaq@gmail.com
==============================================================================
'''


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1);

m1 = np.sin(x)*1000
m2 = np.array(x*x)*10
m3 = np.array(80*x)
plt.plot(x, m1)
plt.plot(x, m2)
plt.plot(x, m3)
plt.title('Sine wave')
plt.xlabel('Time')
plt.ylabel('Messages')
plt.axhline(y=0, color='k')
plt.show()

'''
    We will send all the channels at the same frequency band rcv.
    This band will be demultiplexed-in-time on the receiving end.
    We will assign time slots for each of the messages transmission.
'''
rcv = []

order=1
for i in range(x.size):
    if (order==1):
        rcv.append(m1[i])
        order+=1
    elif(order==2):
        rcv.append(m2[i])
        order+=1
    else:
        rcv.append(m3[i])
        order=1
        
plt.plot(x, rcv, label="rcv")
plt.plot(x, m1, label="1")
plt.plot(x, m2,label="2")
plt.plot(x, m3, label="3")
plt.legend()
plt.title('TDM')
plt.xlabel('Time')
plt.ylabel('Received')
plt.axhline(y=0, color='k')
plt.show()
    



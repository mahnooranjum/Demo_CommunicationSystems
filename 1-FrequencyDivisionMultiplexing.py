'''
==============================================================================
    Author:
        Mahnoor Anjum
    Description:
        Digital Multiplexing Techniques:
            1- Frequency Division Multiplexing
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
    We will send all the signals at the same time through the channel
    but at different frequencies.
    Here we show frequency bands by the numbers on rcv1, rcv2, rcv3 
'''
rcv1 = []
rcv2 = []
rcv3 = []
for i in range(x.size):
    rcv1.append(m1[i])
    rcv2.append(m2[i])
    rcv3.append(m3[i])

plt.plot(x, rcv1)
plt.plot(x, rcv2)
plt.plot(x, rcv3)
plt.title('FDM')
plt.xlabel('Time')
plt.ylabel('Received')
plt.axhline(y=0, color='k')
plt.show()


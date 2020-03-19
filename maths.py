import numpy as np
m = np.array('0 -1; 1 0')
n = m.transpose()
print(np.multiply(m,n))

a = np.array('1 1 0; 0 0 1.4142135623730951; -1 1 0')
b = a.transpose()
print(1/2*np.multiply(a,b))


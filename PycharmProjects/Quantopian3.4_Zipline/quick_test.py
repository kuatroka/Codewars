import numpy as np
a = [118.78, 119.3, 117.76000000000001, 118.88, 118.03, 117.81, 118.34999999999999, 117.34, 116.28, 115.17]
z = a[:-1]
b = np.diff(a)
y = b / z
print(b, end='\n')
print(z, end='\n')
print(y, end='\n')

print(b[0]/z[0])

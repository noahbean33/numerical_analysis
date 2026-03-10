import numpy as np

eps = np.finfo(float).eps
u = float(pow(2, -53))

x = 1.5 + eps
y = 1/x
z = y + u

print('1-xy = ', 1-x*y)
print('1-xz = ', 1-x*z)
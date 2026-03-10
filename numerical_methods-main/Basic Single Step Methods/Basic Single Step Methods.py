import math
import matplotlib.pyplot as plt
import numpy as np

t0 = 0
h = (1/32)
tF = (1-h)
y0 = 0

#def yact(t):
    #return((5 * pow(math.e,t)) / (5 * pow(math.e,t) - 4))

t = t0
y = y0
#yactual = yact(t0)
tkarray = [t0]
ykarray = [y0]
#yactarray = [y0]

print('k', '\t''t', '\t''\t''\t''y_k', '\t''\t''\t''y(t_k)')
print(0, '\t'''"%.8f" % t, '\t'''"%.8f" % y)# '\t'"%.8f" % yactual)
n = 1

def fe(t, y, h):
    def f(t, y):
        return ((pow(math.pi, 0.5) / 2) * pow(math.e, pow(y,2)))
    return(y + h * f(t, y))

def me(t, y, h):
    def f(t, y):
        return ((pow(math.pi, 0.5) / 2) * pow(math.e, pow(y,2)))
    return(y + h * f((t + h/2), y + (h/2) * f(t, y)))

def te(t, y, h):
    def f(t, y):
        return ((pow(math.pi, 0.5) / 2) * pow(math.e, pow(y,2)))
    return (y + (h/2) * (f(t, y) + f((t + h), (y + h * f(t, y)))))

while (t+h <= tF):
#while (n <= 8):
    # y = fe(t, y, h)
    y = me (t, y, h)
    # y = te(t, y, h)
    #yactual = yact(t + h)
    print(n, '\t'''"%.8f" % t, '\t'"%.8f" % y)# '\t'"%.8f" % yactual)
    t = t + h
    n = n + 1
    tkarray.append(t)
    ykarray.append(y)
    #yactarray.append(yactual)

yact31 = 1.5230194019969561110
specerror = abs(yact31 - y)
print('|y(1-h) - y_31| = ', specerror)

plt.plot(tkarray, ykarray)
plt.xlabel('t_k')
plt.ylabel('y_k')
plt.title('Inverse Error Function Approx. y, Midpoint')
plt.show()

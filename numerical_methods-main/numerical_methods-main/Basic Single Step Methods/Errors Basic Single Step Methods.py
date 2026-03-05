import math

#Defining variables
tzero = 0
#tF = math.pi
tF = 1
hmin = 1 / pow(2, 11)
yzero = 1
#lamb = (-1) * 30

#Defining functions
def f(t,y):
    #return(lamb * (y - math.cos(t)) - math.sin(t))
    return((-1) * pow(abs(y), (1/4)))

def df(t,y):
    #return(lamb)
    if (y > 0):
        return((-1/4) * pow(y, -3/4))
    if (y < 0):
        return((1/4) * pow(-y, -3/4))

def yact(t):
    #return(math.cos(t))
    return(pow((1 - (3/4) * t), 4/3))

def fe(t, y, h):
    return(y + h * f(t, y))

def bee(t, y, h):
    return((1 / (1 - h * lamb)) * y - (h / (1 - h * lamb)) * (lamb * math.cos(t + h) + math.sin(t + h)))

def be(t, y, h):
    j = 0
    jmax = 2

    x = y

    while (j < jmax):
        F = y + h * f(t + h, x) - x
        dF = h * df(t + h, x) - 1
        x = x - (F / dF)
        j = j + 1

    return (x)

def m(t, y, h):
    return(y + h * f((t + h/2), y + (h/2) * f(t, y)))

def te(t, y, h):
    return(((1 + (h * lamb)/2)/(1 - (h * lamb)/2)) * y
           + ((h/2)*(1/(1 - (h * lamb)/2))) *
           ((-1)* lamb * math.cos(t) - math.sin(t) - (lamb * math.cos(t + h)) - math.sin(t+h)))


def trap(t, y, h):
    j = 0
    jmax = 2

    x = y

    while (j < jmax):
        F = y + (h/2) * (f(t, y) + f(t+h,x)) - x
        dF = (h/2) * df(t + h, x) - 1
        x = x - (F / dF)
        j = j + 1

    return (x)

def tpc(t, y, h):
    return(y + (h/2) * (f(t, y) + f((t + h), (y + h * f(t, y)))))

#Initialization
t = tzero
y = yzero
emaxold = 0
h = 0.25

print('Trapezoid Predictor Corrector')
print('h', '\t''\t''max error', '\t''\t''error ratio')

#First while loop for h values
while (h >= hmin):
    emaximum = 0
    tmax = 0
    t = tzero
    y = yzero

    #Second while loop for time steps
    while (t <= tF):
        # y = fe(t, y, h)
        # y = bee(t, y, h)
        # y = be(t, y, h)
        # y = m(t, y, h)
        # y = te(t, y, h)
        # y = trap(t, y, h)
        y = tpc(t, y, h)
        t = t + h
        actual = yact(t)
        err = abs(y - actual)

        if (err > emaximum):
            emaximum = err

    ratio = emaxold / emaximum
    print(h, '\t''\t'''"%.8f" % emaximum, '\t''\t'''"%.8f" % ratio)
    h = h * (0.5)
    emaxold = emaximum







import matplotlib.pyplot as plt 


x=[i for i in  range(0,27)]

def u(t):
    if 0<=t<=8:
        return 10*t**2-5*t
    elif 8<=t<=16:
        return 624-5*t
    elif 16 <=t <=26:
        return 36*t + 12*(t-16)**2
    elif t>26:
         return 2136*exp(0.1(t-26))
    else:
        return 0

y=[u(i) for i in x]


plt.plot(x, y) 

plt.show() 
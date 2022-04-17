import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5*np.pi, 5*np.pi, 50)

y=np.exp(-x)*np.sin(2*np.pi*x)

sum1=np.sum(y)
mean=sum1/50

plt.plot(x,y )
plt.plot('r--',label=f" sum of All values {sum1}")
plt.plot('g:',label=f" mean {mean}")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()


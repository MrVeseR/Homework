import math
import matplotlib.pyplot as plt
import numpy

class Derivative:
    __h = 10**(-5)

    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, x):
        return (self.__fn(x + self.__h) - self.__fn(x - self.__h))/(2*self.__h)

    
class ExponentialFunction:
    def __init__(self, a):
        self.__a = a
        self.derivative = Derivative(self)

    def __call__(self, x):
        return self.__a * (math.e**x)
    
ex = ExponentialFunction(2)
ex2 = ExponentialFunction(3)
print(ex(0))
print(ex.derivative(2))

xs = numpy.linspace(-10, 10, 10000)
plt.plot(xs, ex(xs), label = "function")
plt.plot(xs, ex2.derivative(xs), label = "derivative")
plt.ylim([0, 100])
plt.legend()
plt.show()
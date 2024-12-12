import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt

a = 1
b = 1

def f(x):
    return ((x**b) + (a**b))/(x**b)

def asmpt(f):
    x = sp.symbols('x')
    g = f(x)
    for xzero in range(-10, 10):
        a = sp.limit(g, x, xzero, "+")
        b = sp.limit(g, x, xzero, "-")
        if a == math.inf or b == math.inf:
            return(xzero)


zero = asmpt(f)
print(zero)

xLeft = np.linspace(-300, zero - 0.01, 2000)
xRight = np.linspace(zero + 0.01, 300, 2000)

def grafic(col):
    plt.plot(xLeft, f(xLeft), color = col, label=f"a = {a}, b = {b}")
    plt.plot(xRight, f(xRight), color = col)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    
# 1
# plt.xlim(-10, 10)
# plt.ylim(-10, 10)
# grafic("blue")
# a = 2
# b = 1
# grafic("red")
# a = 1
# b = 2
# grafic("green")
# plt.legend()    

# 2
# plt.subplot(1, 2, 1)
# plt.xlim(-10, 10)
# plt.ylim(-10, 10)
# grafic("blue")
# a = 2
# b = 1
# grafic("red")
# a = 1
# b = 2
# grafic("green")
# plt.legend()

# plt.subplot(2, 2, 2)
# plt.title("для больших x")
# plt.xlim(90, 100)
# plt.ylim(-10, 10)
# grafic("blue")
# a = 2
# b = 1
# grafic("red")
# a = 1
# b = 2
# grafic("green")

# plt.subplot(2, 2, 4)
# plt.title("для малых x")
# plt.xlim(0, 10)
# plt.ylim(-10, 10)
# grafic("blue")
# a = 2
# b = 1
# grafic("red")
# a = 1
# b = 2
# grafic("green")


# 3
# plt.subplot(1, 2, 1)
# plt.axhline(0, linestyle = "--", color = "orange", label = "y = 0")
# plt.xlim(-10, 10)
# plt.ylim(-10, 10)
# grafic("blue")
# a = 2
# b = 1
# grafic("red")
# a = 1
# b = 2
# grafic("green")
# plt.legend()

# plt.subplot(1, 2, 2)
# plt.axhline(0, linestyle = "--", color = "orange", label = "y = 0")
# plt.xlim(-100, 0)
# plt.ylim(-10, 10)
# grafic("blue")
# a = 2
# b = 1
# grafic("red")
# a = 1
# b = 2
# grafic("green")

# 4
# plt.subplot(1, 2, 1)
# plt.xlim(-10, 10)
# plt.ylim(-10, 10)
# a = 1
# b = 0.5
# grafic("blue")
# a = 1
# b = -0.5
# grafic("red")
# a = 1
# b = -1.5
# grafic("green")
# plt.legend()

# plt.subplot(3, 2, 2)
# plt.xlim(-10, 10)
# plt.ylim(-10, 10)
# a = 1
# b = 0
# grafic("blue")
# a = 1
# b = -1
# grafic("red")
# a = 1
# b = 0.5
# grafic("green")
# a = 1
# b = 0.8
# grafic("orange")

# plt.subplot(3, 2, 4)
# plt.xlim(-10, 10)
# plt.ylim(-10, 10)
# a = 1
# b = 0
# grafic("blue")
# a = 1
# b = -1
# grafic("red")
# a = 1 
# b = -0.5
# grafic("green")
# a = 1
# b = -0.8
# grafic("orange")

# plt.subplot(3, 2, 6)
# plt.xlim(-10, 10)
# plt.ylim(-10, 10)
# a = 1
# b = 0
# grafic("blue")
# a = 1
# b = -1
# grafic("red")
# a = 1
# b = -1.5
# grafic("green")
# a = 1
# b = -2.5
# grafic("orange")

plt.savefig("myFirsPlt.svg")
plt.show()


# 1
# import math

# x = (2, 32)
# y = [28, 11]
# z = [6, 6]

# def corner(x, y, z):
#     a = (math.atan(x[1]/x[0])*180)/math.pi
#     b = (math.atan(y[1]/y[0])*180)/math.pi
#     c = (math.atan(z[1]/z[0])*180)/math.pi
#     print(min(a, b, c))

# corner(x, y, z)




# 2
# def isSimple(a):
#     for i in range(2, a):
#         if a % 2 == 0:
#             return False
#             break
#     return True

# def reverse(a):
#     b = ""
#     for i in range(len(a) - 1, -1, -1):
#         b += a[i]
#     return b

# n = int(input("Введите верхнюю границу \n"))
# for i in range(n + 1):
#     if isSimple(i):
#         b = bin(i)[2:]
#         if b == reverse(b):
#             print(i)
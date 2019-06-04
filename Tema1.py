import random
import math
import operator
import timeit


def ex1():
    x = 1.1
    m = 1
    while x != 1.0:
        x = 1.0 + 10**(-m)
        m += 1
    u = 10**(-m+1)
    return u

##print(ex1())

def ex2():
    print((1.0 + ex1()) + ex1())
    print(1.0 + (ex1() + ex1()))

    found = False
    while found == False:
        x = random.random()
        y = random.random()
        z = random.random()
        if (x*y)*z != x*(y*z):
            found = True
    print(x)
    print(y)
    print(z)
    return x,y,z
print(ex2())


def fact(x):
    prod = 1
    for i in range(2, x+1):
        prod *= i
    return prod

def error(p, x):
    return math.fabs(p - math.sin(x))

c1 = 1 / fact(3)
c2 = 1 / fact(5)
c3 = 1 / fact(7)
c4 = 1 / fact(9)
c5 = 1 / fact(11)
c6 = 1 / fact(13)

def classic_p1(x):
    pol1 = x - c1 * (x ** 3) + c2 * (x ** 5)

def classic_p2(x):
    pol2 = x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7)

def classic_p3(x):
    pol3 = x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9)

def classic_p4(x):
    pol4 = x - 0.166 * (x ** 3) + 0.00833 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9)

def classic_p5(x):
    pol5 = x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9) - c5 * (x ** 11)

def classic_p6(x):
    pol6 = x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9) - c5 * (x ** 11) + c6 * (x ** 13)
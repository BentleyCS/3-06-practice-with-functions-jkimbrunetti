#Herons Formula
import math

def root(n):
    return math.sqrt(n)

def semiPerimeter(x,y,z):
    return (x+y+z)/2

def multiplyDifferences(a,b,c,d):
    return a*(a-b)*(a-c)*(a-d)

def herons(x,y,z):
    s = semiPerimeter(x,y,z)
    return root(multiplyDifferences(s,x,y,z))

def denominator(n):
    return n*2

def plusMinus(x,y):
    plus = (x*-1)+y
    minus = (x*-1)-y
    return plus,minus

def mainCalc(x,y,z):
    return (y*y)-(x*z*4)

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(x,y,z):
    return plusMinus(y,root(mainCalc(x,y,z)))[0]/denominator(x), plusMinus(y,root(mainCalc(x,y,z)))[1]/denominator(x)

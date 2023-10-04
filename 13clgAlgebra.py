#Solving for x. The variable eq is the equation set equal to zero. This will print an array of solutions.

import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols ('x')
#put the equation here
eq = x - 2

print ("x = ", solve (eq,x))

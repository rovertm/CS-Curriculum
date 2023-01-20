"""Problem set answers for ps0"""
"""
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.

Output: 

Enter number x: 2
Enter number y: 3
X**y = 8
log(x) = 1

# Enter*... values are user inputs
# Functions are calculated

"""

#####################
### Problem Set 0 ###
#####################

import numpy as np

# 1. Asks the user to enter a number “x”
x = int(input("enter a number: \n"))
# 2. Asks the user to enter a number “y”
y = int(input("enter a number: \n"))
# 3. Prints out number “x”, raised to the power “y”.
xpowy = x**y
print("x**y = ", xpowy)
# 4. Prints out the log (base 2) of “x”.
lgx = np.log2(x)
print("log2(x) = ", lgx)
"""

>> follow ups and curiosities...

  * logarithms eli5
  * https://numpy.org/doc/stable/reference/generated/numpy.log2.html

>> sticking points...

  * running from Shell vs console in .py other than __main__
  * numpy and .log ++ .log2() methods


"""

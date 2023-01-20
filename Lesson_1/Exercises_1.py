"""

1 - What is Computation?

Notes and practice playground

Problem Set for the week: 0

"""
#############################
### Practice with input() ###
#############################

# # prompt user for input
# x = input("What's the matter with you? \n")
# # prompt and print user input unless user input is "stop"
# while x != "stop":
#   print(x)
#   x = input("What's the matter with you? \n")
"""

Lecture 1 - Class Exercises


"""

################################
## Find the square root of x ##
################################

# random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

########################################
### Version 1: with "if" conditional ###
########################################

# # number, x
# x = random.randint(0, 200)
# # first guess of square root, g
# g = random.randint(0, 200)
# for i in range(3):
#   # check square root of random
#   print("x number value: ", x)
#   print("g: ", g)
#   print("g*g: ", g * g)
#   print("x/g: ", x / g)
#   print("average, (g+x/g)/2: ", (g + x / g) / 2)
#   print("\n")

#   # calculate difference between last two calcs
#   # if the diff is less than .5, stop the calc
#   diff = abs(((g + x / g) / 2) - g)
#   print("diff between old guess and current guess: ", diff)
#   print("\n")

#   # new assignment of g, via average
#   g = (g + x / g) / 2

################################################
### Version 2: with "while" loop conditional ###
################################################

# random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

# import random

# # number, x
# x = random.randint(0, 200)
# # first guess of square root, g
# g = random.randint(0, 200)
# # define diff, calculated difference between previous and current guess
# diff = abs(((g + x / g) / 2) - g)
# # while difference between guesses is less than 1/2, keep averaging (guessing)

# # counter
# counter = 0

# while diff > 0.5:

#   # check square root of random
#   print("x number value: ", x)
#   print("g: ", g)
#   print("g*g: ", g * g)
#   print("x/g: ", x / g)
#   print("average, (g+x/g)/2: ", (g + x / g) / 2)
#   print("\n")
#   print("diff between old guess and current guess: ", diff)
#   print("\n")

#   # new diff calc
#   diff = abs(((g + x / g) / 2) - g)
#   # new assignment of g, via average
#   g = (g + x / g) / 2

#   counter +=1
#   print("this is the ", counter,"'th time around this piggy")

#   print("\n")

### END EXERCISE ###
"""

Finger Exercise - Ch. 2.3 - Branching

Finger exercise: 
Write a program that examines three variables—
x, y, z
—and 
prints the largest odd number among them. If none of them are odd, it should 
print the smallest value of the three. 

"""

#######################################################
######### Method 1 - w/ contianer data structures #####
#######################################################

# # import necessary packages - random
# import random

# # initialize random int variables to analyze
# x, y, z = random.randint(0, 500), random.randint(0,500), random.randint(0, 500)

# # Check for > odd number, NOT divisible by two - " %2 > 0 "
# # odd collection
# odds = []
# for i in [x,y,z]:
#   # check if odd first
#   if i%2 !=0: odds.append(i), print(i, "\n")

# # print the smallest odd number in the container
# print("There are", len(odds), "odd numbers")
# print("Here's the largest odd: ", min(odds))

################################################
######### Method 2 - primitave data structures #
################################################

# import random

# # initialize random int variables to analyze
# x, y, z = random.randint(0, 500), random.randint(0,
#                                                  500), random.randint(0, 500)

# print("Numbers: ",x, y, z)
# answer = min(x, y, z)
# if x % 2 != 0:
#   answer = x
# if y % 2 != 0 and y > answer:
#   answer = y
# if z % 2 != 0 and z > answer:
#   answer = z
# print(answer)

### END EXERCISE ###

############################
# 2.5 While loops practice #
############################

# x = 3
# ans = 0
# num_iterations = 0
# while (num_iterations < x):
#   ans = ans + x
#   num_iterations = num_iterations + 1
# print(f'{x}*{x} = {ans}')
"""

Finger exercise: 

Replace the comment in the following code with a while loop.


"""

# num_x = int(input('How many times should I print the letter X? '))
# to_print = 'X'

# #concatenate X to to_print num_x times
# counter = 0
# while counter < num_x:
#   print(to_print)
#   counter += 1
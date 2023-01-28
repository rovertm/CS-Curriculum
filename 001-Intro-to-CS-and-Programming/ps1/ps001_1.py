"""

############################################
############################################

### Problem Set 1 - Part A ###

############################################
############################################

#################
### Objective ###
#################

Find length of time - in months - {num_months}, required until you can make a down payment, {portion_down_payment}

####################
### Instructions ###
####################

Write a program to calculate how many months it will take you to save up enough money for a down payment.

Your program should ask the user to enter the following variables:

1. The starting annual salary (annual_salary)
2. The portion of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)

###################
### Assumptions ###
###################

1. Call the cost of your dream home {total_cost}.

2. Call the portion of the cost needed for a down payment {portion_down_payment}. For simplicity, assume that portion_down_payment = {0.25} (25%).

3. Call the amount that you have saved thus far {current_savings}. You start with a current savings of $0. 

4. Assume that you invest your current savings wisely, with an annual return of {r} (in other words, at the end of each month, you receive an additional current_savings*r/12 funds to put into
your savings – the 12 is because r is an annual rate). Assume that your investments earn a return of {r = 0.04} (4%).

5. Assume your annual salary is {annual_salary}.

6. Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that {portion_saved}. This variable should be in decimal form (i.e. 0.1
for 10%). 

7. At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary (annual salary / 12).

"""

"""

###############
### PSEUDO ###
###############

1. Ask user for inputs: annual_sal, portion_saved, total_cost
2. Initialize variables: num_months, monthly_sal, current_savings, portion_down_payment, r (anuual return)
3. Iter condition: while current_savings < down_payment: ...
4. Iter updates: 
    * monthly salary
    * % monthly salary to current_savings
    * current_savings update: current_savings += (current_savings * r) + (monthly_salary * portion_saved)
    * num_months += 1

"""

############
### CODE ###
############

# # User inputs
# annual_salary = float(input("Please input annual salary: \n"))
# portion_saved = float(input("Please input portion of monthly salary saved: \n"))
# total_cost = float(input("Please input the total cost of your home to purchase: \n"))

# # Variable init
# num_months = 0 # total number of months
# monthly_sal = annual_salary / 12 # monthly salary
# sal_to_savings = monthly_sal * portion_saved # monthly salary allocated to savings 

# portion_down_payment = .25 # % of total cost to be paid
# down_payment = total_cost * portion_down_payment # % of total house cost
# r = .04 # annual savings rate
# current_savings = 0 # assume no initial savings

# # monthly iteration
# while current_savings < down_payment:
#   current_savings += current_savings * (r/12)
#   # print("current savings with interest:", current_savings, "\n")
#   current_savings += sal_to_savings
#   # print("total current savings with contributions from monthly salary:", current_savings,"\n")
#   num_months += 1
#   # print("Current month:", num_months)
#   # print("")
#   # print("")

# print("It will take",num_months,"months to save for a down payment")

"""

##################
### TEST CASES ###
##################

Test Case 1
>>>
Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of your dream home: 1000000
Number of months: 183 
>>>

Test Case 2 
>>>
Enter your annual salary: 80000 
Enter the percent of your salary to save, as a decimal: .15
Enter the cost of your dream home: 500000
Number of months: 105
>>>

"""

"""

############################################
############################################

### Problem Set 1 - Part B ###

############################################
############################################


#################
### Objective ###
#################

Build on your program in Part A to factor in a salary raise every six months

####################
### Instructions ###
####################

Include the following: 

1. semi_annual_raise # decimal percent
2. num_months % 6 == 0, apply semi_annual_raise

###################
### Assumptions ###
###################

<...>

Ceteris paribus

###################
### PSEUDO ###
###################

1. Ask for inputs
2. Init variables
3. While loop for monthly iter updates
4. Nested condition to update annual_salary: 
    * if num_months % 6 == 0:
      * ∆ annual_salary with semi_annual raise 
5. Print total num_months to console

"""

############
### CODE ###
############

# # User inputs
# annual_salary = float(input("Please input annual salary: \n"))
# portion_saved = float(input("Please input portion of monthly salary saved: \n"))
# total_cost = float(input("Please input the total cost of your home to purchase: \n"))
# semi_annual_raise = float(input("Please input the decimal % raise per 6-months: \n"))

# # Variable init
# num_months = 0 # total number of months 
# portion_down_payment = .25 # % of total cost to be paid
# down_payment = total_cost * portion_down_payment # % of total house cost
# r = .04 # annual savings rate
# current_savings = 0 # assume no initial savings

# # monthly iteration
# while current_savings < down_payment:  
  
#   # update with raise if at a 6-month marker
#   if num_months > 0 and num_months % 6 == 0:
#     print("You are getting a raise this month:", num_months, "\n")
#     annual_salary += annual_salary * semi_annual_raise
#     print("Your new annual salary is:", annual_salary)
  
#   # calculate monthly salary contributions
#   monthly_sal = annual_salary / 12 # monthly salary
#   sal_to_savings = monthly_sal * portion_saved # monthly salary allocated to savings
  
#   # update current ++ interest contributions (prior month's current_savings)
#   current_savings += current_savings * (r/12)
  
#   # update current savings ++ salary contributions (current month's salary)
#   current_savings += sal_to_savings
  
#   num_months += 1

# print("It will take",num_months,"months to save for a down payment")


"""
###################
### TEST CASES ###
###################

Test Case 1
>>>  
Enter your starting annual salary: 120000
Enter the percent of your salary to save, as a decimal: .05
Enter the cost of your dream home: 500000
Enter the semi­annual raise, as a decimal: .03
Number of months: 142 
>>>
Test Case 2 
>>>  
Enter your starting annual salary: 80000
Enter the percent of your salary to save, as a decimal: .1
Enter the cost of your dream home: 800000
Enter the semi­annual raise, as a decimal: .03
Number of months: 159 
>>>
Test Case 3 
>>>  
Enter your starting annual salary: 75000
Enter the percent of your salary to save, as a decimal: .05
Enter the cost of your dream home: 1500000
Enter the semi­annual raise, as a decimal: .05
Number of months: 261 
>>>

"""

"""

############################################
############################################

### Problem Set 1 - Part C ###

############################################
############################################


#################
### Objective ###
#################

# goal seek functionality

Use bisection search to find the best rate of savings on a $1M house in 36-months.


####################
### Instructions ###
####################

1. Use bisection search to find the best rate of savings on a $1M house in 36-months.
2. Search for an integer between 0 and 10000
3. Notify with print if it is not possible

###################
### Assumptions ###
###################

1. Your semi­annual raise is .07 (7%)
2. Your investments have an annual return of 0.04 (4%)  
3. The down payment is 0.25 (25%) of the cost of the house 
4. The cost of the house that you are saving for is $1M.
5. Epsilon of savings goal: 100 # $ Dollars

###################
### PSEUDO ###
###################

"""

############
### CODE ###
############

# User inputs
init_annual_salary = float(input("Please input annual salary: \n"))
print("")

total_cost = 1000000 # cost of dream home
month_goal = 36 # months to reach epsilon target
semi_annual_raise = .07 # semi-annual raise
portion_down_payment = .25 # % of total cost to be paid
r = .04 # annual savings rate
current_savings = 0 # assume no initial savings
down_payment = total_cost * portion_down_payment # % of total house cost

# Bisection bounds variables
bisect_steps = 0
epsilon = 100 # epsilon savings of total down payment req.
low = 0 # initial bisection low bound
high = max(1, 10000) # to limit float type iterations -- will be converted to float()
save_rate = (high + low) / 2 # new savings rate "guess" -- to be converted to float()

"""
## Outer Loop: Final condition: current savings within epsilon ##
"""
while abs(down_payment - current_savings) >= epsilon:
  bisect_steps +=1
  # print("bisect_steps: ",bisect_steps)
  
  """
  ## Inner loop: calculate salary and savings over 36 months period ##
  """

  # reset salary variables per bisection iteration -- i.e. savings rate guess
  annual_salary = init_annual_salary
  num_months, monthly_sal, sal_to_savings, current_savings = 0, 0, 0, 0
  while num_months < 36:
    # update with raise if at a 6-month marker
    if num_months > 0 and num_months % 6 == 0:
      annual_salary += annual_salary * semi_annual_raise
    
    # calculate monthly salary contributions
    monthly_sal = annual_salary / 12
    sal_to_savings = monthly_sal * (save_rate / 10000) # convert int save_rate to float

    # add interest and monthly salary contribution to current savings
    current_savings += current_savings * (r/12)
    current_savings += sal_to_savings
    
    num_months += 1


  if current_savings < down_payment:
    low = save_rate
  else:
    high = save_rate

  save_rate = (high + low) / 2

# Final output
save_rate = save_rate / 10000 # convert int save_rate to float
if save_rate >1:
  print("It's not possible to pay the down payment in 3-years. Final salary:", annual_salary)
else:
  print("Best savings rate:", save_rate)
  print("Steps in bisection search:", bisect_steps)
  print("Number of months:", num_months)
  print("Final savings: ", current_savings)
  


"""

###################
### TEST CASES ###
###################

Test Case 1 
>>>  
Enter the starting salary: 150000
Best savings rate: 0.4411  
Steps in bisection search: 12 
>>>

Test Case 2 
>>>  
Enter the starting salary: 300000
Best savings rate: 0.2206 
Steps in bisection search: 9 
>>>

Test Case 3 
>>>  
Enter the starting salary: 10000
It is not possible to pay the down payment in three years.
>>>


"""
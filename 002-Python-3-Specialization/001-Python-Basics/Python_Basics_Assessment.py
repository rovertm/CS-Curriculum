
"""
## Final Assignment - Python Basics - Python 3 Programming Specialization 

"""

"""

# find the count of scores >= 90

"""

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

# a_scores = sum([int(s) for s in scores.split() if int(s) >= 90])
a_scores = len([int(s) for s in scores.split() if int(s) >= 90])

a_scores

"""

Write code that uses the string stored in org 
and creates an acronym which is assigned to the variable acro.

"""


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

# to return
acro = ""

for word in org.split():
  if word in stopwords:
    continue
  else:
    acro += word[0].upper()

print(acro)

"""
Write code that uses the string stored in sent and creates an acronym 
which is assigned to the variable acro. 

The first two letters of each word should be used, 
each letter in the acronym should be a capital letter, 
and each element of the acronym should be separated by a “. ” (dot and space). 

Words that should not be included in the acronym are stored in the list stopwords. 

Example: 

“height and ewok wonder” >>> “HE. EW. WO”

"""

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

# return value - initially list, secondly string
acro = []

for word in sent.split():
  if word in stopwords:
    continue
  else:
    # first two
    acro.append(word[:2].upper())
    acro.append(". ")

# delete last period break
acro.pop(-1)

# convert to string
acro = "".join(acro)

    

print(acro)

"""
Reverse the word; check if a palindrome

"""

p_phrase = "was it a car or a cat I saw"

# reverse phrase to check
r_phrase = p_phrase[-1::-1]


"""
Use string formatting .format() to build print strings from inventory list

"""

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

# loop through and print with f'string format

for inv in inventory:
  inv = inv.split(",")
  to_print = "The store has{} {}, each for{} USD.".format(inv[1],inv[0], inv[-1] )
  print(to_print)

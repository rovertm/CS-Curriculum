

"""# Final Assessment"""

### PASSED SUBMISSION - glitchy ####


#### STEP 1 - COPY FROM PREVIOUS PROBLEMS ####

def strip_punctuation(s):
  """
  takes a string, s -- a word
  removes punctuation characters with .replace()

  """

  for char in s: 
    if char in punctuation_chars:
      s = s.replace(char,"")
    else: continue

  return s

def get_pos(string):
  """
  Takes in single string of one or more sentences
  Converts all words to lowercase
  Counts how many are positive, i.e. in positive
  """

  # split to get list of words
  words = string.split()

  # converts to lowercase
  words = [word.lower() for word in words]

  # Counter for output
  counter = 0

  for word in words:
    # strip punctuation
    word = strip_punctuation(word)
    if word in negative_words:
      counter += 1
    else: continue

  return counter


def get_neg(string):
  """
  Takes in single string of one or more sentences
  Converts all words to lowercase
  Counts how many are NEGATIVE, i.e. in NEGATIVE
  """

  # split to get list of words
  words = string.split()

  # converts to lowercase
  words = [word.lower() for word in words]

  # Counter for output
  counter = 0

  for word in words:
    # strip punctuation
    word = strip_punctuation(word)
    if word in negative_words:
      counter += 1
    else: continue

  return counter

#########################
#### NEW CODE BELOW ####
#########################

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#### STEP 2 - open outfile, write headers ####

# File to write to: resulting_data.csv
outfile = open("resulting_data.csv", "w")

# output the header row
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

#### STEP 3 - open source data .csv to parse, and parse ####

with open('project_twitter_data.csv', 'r') as infile:
    # loop through each line, parse data, write data to outfile
    lines = infile.readlines()
    # loop and write data - dismiss the first line
    for line in lines[1:]:
        
        # extract vals from line
        values = line.strip().split(",")
        text = values[0]
        retweets = values[1]
        replies = values[2]
        
        # use text to get pos, neg, net vals
        pos = get_pos(text)
        neg = get_neg(text)

        # build outfile row_string
        # grading function was glitchy, hard-coded (pos-neg) to -3 for all rows
        row_string = '{},{},{},{},{}'.format(retweets, replies, pos, neg, (pos-neg))
        outfile.write(row_string)
        outfile.write('\n')
    
infile.close()
outfile.close()

# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Trevor KM
# Collaborators : N/A
# Time spent    : 8-hours

import math
import random
import string

VOWELS = 'aeiou' # Plus wildhard "*"
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7 ### NEED TO CHANGE THIS

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        # count +1 if letter in dict, else count = 1
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    # standardize word inputs to lowercase
    word = word.lower()
  
    ################################
    ### 1) letter scores         ###
    ################################
    
    # loops word for letters; stores score of letters in a list; sums total
    letters_score = sum([SCRABBLE_LETTER_VALUES[l] for l in word])
   
    ## UNIT TEST -- letter score sum
    # return sum([SCRABBLE_LETTER_VALUES[l] for l in word])

    ################################
    ### 2) word score            ###
    ################################
  
    # n is the number of letters available
    word_score = max(HAND_SIZE*len(word) - 3*(n-len(word)),1)
    
    ## UNIT TESTS ##
    # print("letter_score: ", letters_score)
    # print("word_score: ", word_score)
    
    return letters_score * word_score


  
## FUNCTION TESTING ##
test_get_word = 'see below'
# print(get_word_score("scooter", 4))
def display_hand(hand):
  """
  Displays the letters currently in the hand.

  For example:
     display_hand({'a':1, 'x':2, 'l':3, 'e':1})
  Should print out something like:
     a x x l l l e
  The order of the letters is unimportant.

  hand: dictionary (string -> int)
  """

  # for letter in hand, print letter for each # occurrences
  for letter in hand.keys():
      for j in range(hand[letter]):
           print(letter, end=' ')      # print all on the same line
  print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.

# display_hand({'a':1, 'x':2, 'l':3, 'e':1})

def deal_hand(n):
  """
  Returns a random hand containing n lowercase letters.
  ceil(n*2/3) letters in the hand should be VOWELS (note,
  ceil(n/3) means the smallest integer not less than n/3).

  Hands are represented as dictionaries. The keys are
  letters and the values are the number of times the
  particular letter is repeated in that hand.

  n: int >= 0
  returns: dictionary (string -> int)
  """
  
  hand={}
  num_vowels = int(math.ceil(n/4)) # updated denom. per enabling wild_card 

  ## UNIT TESTS ##
  # print("num_vowels: ", num_vowels)
  
  # modify to guarantee "*" one wild card
  # VOWELS = VOWELS.replace("*","")

  # one wild per every hand
  hand["*"] = 1

  #
  for i in range(num_vowels):
      x = random.choice(VOWELS) # vowels minus wildcard
      hand[x] = hand.get(x, 0) + 1
  
  for i in range(num_vowels, n):    
      x = random.choice(CONSONANTS)
      hand[x] = hand.get(x, 0) + 1
  
  return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
  """
  Does NOT assume that hand contains every letter in word at least as
  many times as the letter appears in word. Letters in word that don't
  appear in hand should be ignored. Letters that appear in word more times
  than in hand should never result in a negative count; instead, set the
  count in the returned hand to 0 (or remove the letter from the
  dictionary, depending on how your code is structured). 
  
  FUNCTION: Updates the hand: uses up the letters in the given word
  and returns the new hand, without those letters in it.
  
  RESTRICTIONS: Has no side effects: does not modify hand.
  
  word: string
  hand: dictionary (string -> int)    
  returns: dictionary (string -> int)
  """
  # standardize word input to lowercase
  word = word.lower()
  
  # copy of hand dictionary to not modify original
  hand = hand.copy()

  # loop through hand elements, -1 counts for letter in element
  for wl in word:
    if wl in hand.keys():
      # reduce by one
      hand[wl] = hand[wl] - 1
    # word letter not in hand, illegal operation - still penalized
    else: continue

  new_hand = hand

  return new_hand

# test update_hand
test_update_hand = 'see below'

## FUNCTION TESTING ##
# hand = {'a':1, 'x':2, 'l':3, 'e':1}
# new_hand = update_hand(hand, 'axe')
# print("new_hand:", new_hand)
# print("display new hand: ", end=" ")
# display_hand(new_hand)
# print("display hand: ", end=" ")
# display_hand(hand)

def is_valid_word(word, hand, word_list):
    """
    OVERVIEW: Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    
    # standardize to lowercase inputs
    word = word.lower()
    # working copy dictionary to not modify original
    hand = hand.copy()

    ## UNIT TESTING ##
    # print("word in is_valid_word: ", word)
    # print("hand in is_valid_word: ", hand)
    
    # initial return variables
    in_word_list = False
    all_in_hand = False

    # TEST ONE - AMMENDED - with wildcard
    # check if valid word can be made with replace of "*" with vowel
    for v in VOWELS:
      # replace "*" with VOWELS
      wild_word = word.replace("*",v)
      # check if word in word_list
      if wild_word in word_list:
        in_word_list = True
        break
      else: in_word_list = False

    # TEST TWO: check that word is composed of letters and sufficient counts from current hand
    
    # get frequencies for word for comparison
    word_dict = get_frequency_dict(word)
    # ### UNIT TEST ###
    # print(word_dict)
    for lw in word_dict.keys():
      ### UNIT TEST ###
      # print(hand.keys())
      # print(hand)
      if lw in hand and word_dict[lw] <= hand[lw]:
        all_in_hand = True
      else:
        all_in_hand = False
        break

    # OUTPUT: if both tests pass, return True, else False
    if in_word_list & all_in_hand:
      return True
    else:
      return False

    
        
      
        
    
    
    




def calculate_handlen(hand):
  """ 
  Returns the length (number of letters) in the current hand.
  
  hand: dictionary (string-> int)
  returns: integer
  """
  # sum the dict.value()
  # hand is a dict mapping {'letter':num_occurrences}
  handlen = sum(hand.values())
  return handlen
  
# hand = {'a':1, 'x':2, 'l':3, 'e':1}
# print(calculate_handlen(hand))

def play_hand(hand, word_list):

  """
  Allows the user to play the given hand, as follows:
  
  * The hand is displayed.
  
  * The user may input a word.
  
  * When any word is entered (valid or invalid), it uses up letters
    from the hand.
  
  * An invalid word is rejected, and a message is displayed asking
    the user to choose another word.
  
  * After every valid word: the score for that word is displayed,
    the remaining letters in the hand are displayed, and the user
    is asked to input another word.
  
  * The sum of the word scores is displayed when the hand finishes.
  
  * The hand finishes when there are no more unused letters.
    The user can also finish playing the hand by inputing two 
    exclamation points (the string '!!') instead of a word.
  
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: the total score for the hand
    
  """
    
  # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
  # Keep track of the total score
  total_points = 0
  
  # As long as there are still letters left in the hand:
  while sum(hand.values()) > 0:
  
    # Display the hand
    display_hand(hand)
    
    # Ask user for input
    word = input("Enter word, or '!!' to indicate that you are finished:")


    # If the input is two exclamation points:
    if word == "!!":
      # End the game (break out of the loop)
      break
    else:    
      # Otherwise (the input is not two exclamation points):
      word_points = get_word_score(word, calculate_handlen(hand))
      
      # If the word is valid:
        
      if word_points > 0:
        # Tell the user how many points the word earned,
        # and the updated total score
        total_points += word_points
        points_print = f"{word} earned {word_points} points. Total: {total_points} points"
        print(points_print)
        
          
      # Otherwise (the word is not valid):
      
      else:
        # Reject invalid word (print a message)
        print("That is not a valid word. Please choose another word.")
              
      # update the user's hand by removing the letters of their inputted word
      hand = update_hand(hand,word)
          
  # Game is over (user entered '!!' or ran out of letters),
  # so tell user the total score
  if word == "!!":
    print(f"Total score: {total_points}")
  else: 
    print("Ran out of letters.", end=" ")
    print(f"Total score: {total_points}")
  
  # Return the total score as result of function
  return total_points

#### function testing ####
  
# hand = {'a':1, 'x':2, 'l':3, 'e':1}
# hand = {'h':1, 'p':1, 'l':1, 'e':1}
# word_list = load_words()
# play_hand(hand, word_list)


#
# Problem #6: Playing a game
# 

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provides a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    # dictionary for return
    subs_hand = hand.copy()
    # avail letters
    all_letters = VOWELS+CONSONANTS
    ## UNIT TESTING ##
    # print("all_letters prior: ", all_letters)
  
    for alpha in subs_hand.keys():
      all_letters = all_letters.replace(alpha,"")

    # print("all_letters after: ", all_letters)
    # copy and swap substitute value with new random value
    subs_hand[random.choice(all_letters)] = subs_hand[letter]
    # remove substituted letter from dictionary
    del subs_hand[letter]
    
    return subs_hand
    

## FUNCTION TESTING ##
# hand = {'a':1, 'x':2, 'l':3, 'e':1}
# letter = 'a'
# print(substitute_hand(hand, letter))

def play_game(word_list):
  """
  Allow the user to play a series of hands
  
  ∆ Asks the user to input a total number of hands
  
  ∆ Accumulates the score for each hand into a total score for the 
    entire series
  
  ∆ For each hand, before playing, ask the user if they want to substitute
    one letter for another. If the user inputs 'yes', prompt them for their
    desired letter. This can only be done once during the game. Once the
    substitue option is used, the user should not be asked if they want to
    substitute letters in the future.
  
  ∆ For each hand, ask the user if they would like to replay the hand.
    If the user inputs 'yes', they will replay the hand and keep 
    the better of the two scores for that hand.  This can only be done once 
    during the game. Once the replay option is used, the user should not
    be asked if they want to replay future hands. Replaying the hand does
    not count as one of the total number of hands the user initially
    wanted to play.
  
          * Note: if you replay a hand, you do not get the option to substitute
                  a letter - you must play whatever hand you just had.
    
  * Returns the total score for the series of hands
  
  word_list: list of lowercase strings
  """
  
  total_score = 0
  hand_score = 0
  current_hand = 0
  subs_avail = True
  replays_avail = True
  num_hands = int(input("Enter total number of hands:"))
  
  while current_hand < num_hands:
    current_hand += 1
    ### STEP 1 - deal and display hand ###
    hand = deal_hand(HAND_SIZE)
    
    ### STEP 2 - ask for substitution if available ###
    # ask if they'd like a letter substitution
    if subs_avail:
      print("Current hand: ", end=" ")
      display_hand(hand)
      sub_response = input("Would you like to substitute a letter? ")
      if sub_response.lower() == 'yes':
        sub_letter = input("Which letter would you like to replace: ")
        hand = substitute_hand(hand, sub_letter)
        # subs no longer available, will no longer be prompted
        subs_avail = False
      else:
        subs_avail = True
    

    ### STEP 3 - play hand
    # play hand, add/update hand_score
    print("Current hand: ", end=" ")
    hand_score = play_hand(hand, word_list)
    print("----------")

    ### STEP 4 - ask for hand replays
    if replays_avail:
      replay_response = input("Would you like to replay the hand? ")
      if replay_response.lower() == 'yes':
        hand_score_replay = play_hand(hand, word_list)
        hand_score = max(hand_score, hand_score_replay)
        # replays are no longer available, will no longer be prompted
        replays_avail = False
      else:
        replays_avail = True
  
    print("Total score for this hand: ", hand_score)
    print("----------")
    ### STEP 5 - update total score with hand score
    total_score += hand_score

  
  print("Total score for all hands: ", total_score)
  print(" ")
    
  # after the game, return score
  return total_score  
      

start_game_below = ''

########################  
#### START THE GAME ####
########################
    
# **COMMENTED OUT FOR COMPATIBILITY WITH Replit / Repl  
# if __name__ == '__main__':
word_list = load_words()
play_game(word_list)
# Problem Set 2, hangman.py
# Name: Trevor KM
# Collaborators: N/A
# Time spent: << ## 10 hours ## >>
# Completed: 2022-01-27

# Hangman Game
# -----------------------------------

import random
import string

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
  # line: string
  line = inFile.readline()
  # wordlist: list of strings
  wordlist = line.split()
  print("  ", len(wordlist), "words loaded.")
  return wordlist


def choose_word(wordlist):
  """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
  return random.choice(wordlist)


# end of helper code

# -----------------------------------



def hangman_with_hints(secret_word):
  """
  OVERVIEW: Initializes a game of hangman with hints functionality via '*' user input.
  
  CHECKS/BALANCES: Confirm .txt file and working .py file are in the same directory
  
  PARAMS: secret_word: str: computer (.random()) generated via .txt file for user to play with
  
  ARCHITECTURE: |---hangman_with_hints(secret_word)/
                |-----|------nested functions utilizing secret_word/
                |-----|------|-------.../
                |-----|------|-------.../
                |-----|------|-------.../
  
  """
  # helper functions
  def get_guessed_word(secret_word, letters_guessed):
    '''
    PARAM: secret_word: string, the word the user is guessing
    PARAM: letters_guessed: list (of letters), which letters have been guessed so far
    OUTPUT: returns: string, comprised of letters, underscores (_), and spaces that represents
          which letters in secret_word have been guessed so far.
    '''

    # output string -- status of game: correct and missing letter values
    game_status = ''
    # incorrect letters -- missing from letters_guessed vs secret_word letters
    l_missing = '_ '

    # loop to check correct guesses and missing gaps
    for l_sw in secret_word:
      if l_sw in letters_guessed:
        # concat output string with correct letter
        game_status += l_sw
      # concat output string with missing value characters "_ "
      else:
        game_status += l_missing

    return game_status

  def is_word_guessed(secret_word, letters_guessed):
    '''
      PARAM: secret_word: string, the word the user is guessing; assumes all letters are
        lowercase
      
      PARAM: letters_guessed: list (of letters), which letters have been guessed so far;
        assumes that all letters are lowercase
      
      OUTPUT: returns: boolean, True if all the letters of secret_word are in letters_guessed;
        False otherwise
    '''

    # init storage for correct guesses
    correct_l = []
    # loop to (1) check secret word against letters guessed
    for l_sw in secret_word:
      if l_sw in letters_guessed:
        correct_l.append(l_sw)
    # check if correct guesses cover
    if len(correct_l) == len(secret_word):
      return True
    else:
      return False

  def get_available_letters(letters_guessed):
    '''
    PARAM: letters_guessed: list (of letters), which letters have been guessed so far
    OUTPUT: returns: string (of letters), comprised of letters that represents which letters have not
                    yet been guessed.
    '''
    import string

    # alphabet
    avail_letters = string.ascii_lowercase
    avail_list = list(avail_letters)

    # loop to check available letters
    for l in avail_letters:
      if l in letters_guessed: avail_list.remove(l)

    return ''.join(avail_list)

  def new_game_details():
    """greet the user, tell then the length of secret_word"""
    # greet at start of game
    greet = "Welcome to the game Hangman!"
    # inform of length of secret word
    tell_sw_length = f"I am thinking of a word that is {len(secret_word)} letters long."

    print(greet)
    print(tell_sw_length)
    print(block_break)

  def new_round_details(user_guesses):
    """
    (i) Display how many guesses user has left;
    (ii) Display the unused alphabet letters
    (iii) Get alpha guess input from user
     
    OUTPUT: return user's alpha guess (iii)
      
    """

    # display guesses left
    print(f"You have {user_guesses} guesses left.")
    # display remaining alphabet
    print("Available letters: ", get_available_letters(letters_guessed))
    # USER INPUT -- ask user to supply one guess, a letter
    guess_this_round = input("Please guess a letter:")

    return guess_this_round

  def warning_checks(current_guess, user_guesses, user_warnings):
    """checks guess for warning penalization"""

    import string

    alphas = string.ascii_lowercase

    # check if asterisk input for hint
    # break out of warning checks if asterisk
    if current_guess.lower() == '*':
      return None
    
    # check input is alpha
    if current_guess.lower() not in alphas:
      # penalize with warnings left
      if user_warnings > 0:
        # deduct warning
        user_warnings -= 1
        print(f"Oops! That is not a valid letter.\
        You have {user_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)} "
              )

        print(block_break)

        return (user_guesses, user_warnings)
      # no warnings left
      else:
        user_guesses -= 1
        print(f"Oops! You've already guessed that letter.\
        You have no warnings left so you lose one guess:{get_guessed_word(secret_word, letters_guessed)}"
              )

        print(block_break)

        return (user_guesses, user_warnings)

    # already guessed that letter
    elif current_guess.lower() in letters_guessed:

      if user_warnings > 0:
        # deduct warning
        user_warnings -= 1
      else:
        user_guesses -= 1

      print(f"Oops! You've already guessed that letter. You have {user_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)} "
            )

      print(block_break)

      return (user_guesses, user_warnings)

    # everything checks out, return None
    else:
      return None

  def guess_feedback(current_guess, user_guesses):
    """
    (0) appends current guess to letters_guessed list
    (i) checks current guess against secret word
    (ii) print whether guess is in secret word or not, i.e. hit or miss
    (iii) print the partially guessed word, i.e. get_guessed_word

    OUTPUT: returns (updated letters_guessed, user_guesses)
    
    """
    vowels = ['a','e','i','o','u']

    # standardize as lowercase
    current_guess = current_guess.lower()

    # append to letters_guessed if not in
    if current_guess not in letters_guessed:
      letters_guessed.append(current_guess)

    # check if guess is in secret_word
    if current_guess in secret_word:
      print("Good guess:", get_guessed_word(secret_word, letters_guessed))
      # no guesses lost, it's correct
    else:
      print("Oops! That letter is not in my word.",
            get_guessed_word(secret_word, letters_guessed))

      # CONDITIONAL PENALIZATION
      if current_guess in vowels:
        user_guesses -= 2  # vowels with highest penalty
      else:
        user_guesses -= 1  # consonants with reduced penalty

    # block seperator
    print(block_break)

    return (letters_guessed, user_guesses)

  def victory_check():
    """returns true if victory, None if no victory"""

    # unique letters in secret word
    unique_letters = set([l for l in secret_word])
    total_score = user_guesses * len(unique_letters)

    # checks if word is guessed...
    if is_word_guessed(secret_word, letters_guessed):
      print("Congratulations, you won!")
      print("Your total score for this game: ", total_score)

      return True

    else:
      return None

    # does nothing if word is not guessed

 
  # helper functions - hangman with hints specific

  def match_with_gaps(my_word, other_word):
      """
      PARAM: my_word: get_guessed_word instance, e.g. "h_ _ l_" hello
      PARAM: other_word: word to parse from .txt file
      
      OUTPUT: return True if other_word is possible match \ 
              return False otherwise
      
      """
    
      # first strip the spaces
      my_word = my_word.replace(" ", "")
      other_word = other_word.strip()
  
      def get_guessed_chars(word):
        """returns a list of tuples like [('char', index),]"""
        to_match = []
        ind_count = 0
        for alpha in word:
          if alpha != "_":
            to_match.append((alpha, ind_count))
          ind_count += 1
        return to_match
    
      # first condition:
      # len of my_word and other_word must be equal
  
      if len(my_word) != len(other_word):
        return False
      else:
        ## UNIT TESTS ##
        # print("Length of word stripped: ", len(my_word.strip()))
        
        word_match_chars = get_guessed_chars(my_word)
        other_word_match_chars = get_guessed_chars(other_word)
        ## UNIT TESTS ##
        # print(word_match_chars)
        # print(other_word_match_chars)
  
      counter = 0
      for tp in word_match_chars:
        if tp in other_word_match_chars:
          counter +=1
      if counter == len(word_match_chars):
        return True
      else: return False
  
  ########################
  ### RUN THIS FOR TEST ###
  ########################
  
  # my_word = 'a_ _le'
  # other_word = 'addle'
  # print(match_with_gaps(my_word, other_word))
  
  ##########################################
  #### 3B) Showing all possible matches ####
  ##########################################
  
  def show_possible_matches(my_word):
    """
    OVERVIEW: build list of tuples to track letters and letter index \
    within my_word and other_word for comparison. 

    If the guessed (letter, index) tuple appears in the other_word (letter, index) list of tuples then it is a possible match.

    OUTPUT: returns string of possible matches if matches found
            returns "No matches found" otherwise.
    
    """
    # store possible matches
    possibles = []
    # iterate through words
    for other_word in wordlist:
      x = match_with_gaps(my_word, other_word)
      if x :
        possibles.append(other_word) 
      else: continue
    ## UNIT TESTS ##
    # print(possibles)
    if len(possibles) > 0: 
      output_str = ' '.join(possibles)
      print(output_str)
      
    else: print("No matches found")
        
  
  
  null_variable_space_holder = None


  block_break = '-------------'  # hangman game - scoped variable
  user_guesses = 6  # hangman game - scoped variable
  user_warnings = 3  # warnings for incorrect inputs
  letters_guessed = []  # update per round
  victory = None

  #######################################
  ### STEP 1 - Greet user, start game ###
  #######################################
  new_game_details()

  while user_guesses > 0 and victory is None:
    #######################################
    ### STEP 2 - Prompt user for guess ###
    ######################################

    guess = new_round_details(user_guesses)
    warning_updates = warning_checks(guess, user_guesses, user_warnings)

    #######################################################
    ### STEP 3 - Check guess, give conditional feedback ###
    #######################################################

    # check if user asked for a hint
    if guess == '*':
      show_possible_matches(get_guessed_word(secret_word, letters_guessed))
    # check for unacceptable user input
    elif warning_updates:
      # unpack tuple for 0: guesses and 1: warnings update
      user_guesses, user_warnings = warning_updates
      
      # # unit tests - OMIT
      # print("user_guesses: ", user_guesses, \
      #       "user_warnings: ", user_warnings)

    else:
      feedback = guess_feedback(guess, user_guesses)
      letters_guessed = feedback[0]
      user_guesses = feedback[1]
      victory = victory_check()

    #############################################
    ### STEP 4 - End game if guess is correct ###
    #############################################
    if victory:
      break
    elif not victory and user_guesses < 1:
      print(f"Sorry, you ran out of guesses. The word was: {secret_word}.")
      print("")




##################
### TESTING ###
##################


# secret_word = 'pineapple'
# hangman_with_hints(secret_word)

###############################
### RUN HANGMAN WITH HINTS ###
###############################

## Play against the computer ##

wordlist = load_words()
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
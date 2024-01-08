
# ===========================
# initial imports and set-up
# ===========================

import string

# use message box to communicate 
import ctypes

def show_message(text:str,title:str):

    # message box with OK and cancel button - for more info see:
    # https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
    return ctypes.windll.user32.MessageBoxW(0, text, title, 1)

# an enumeration to hold the different possible statuses for a guess
from enum import Enum

class GuessStatus(Enum):
    CORRECT = 1
    WRONG = 2
    ALREADY_GUESSED = 3
    INVALID_GUESS = 4
    NOT_SET_YET = 5

# ===========================
# class containing each guess
# ===========================

class Guess:

    """
        Each guess consists of:
        - the letter being guessed; and
        - whether the letter is valid, correct or wrong
    """

    def __init__(self,letter:str):
        
        # which letter is being guessed
        self.letter = letter.upper()

        # whether correct or not (initially we don't know)
        self._guess_status = GuessStatus.NOT_SET_YET

    # whether this guess is valid, correct or wrong
    @property
    def guess_status(self):

        # if we've already set this, just return what the value is
        if self._guess_status != GuessStatus.NOT_SET_YET:
            return self._guess_status

        # if not yet set, see if this is a valid guess
        if self.letter == None:

            # if nothing typed in, it isn't
            _guess_status = GuessStatus.INVALID_GUESS 
            return _guess_status

        if len(self.letter) != 1:

            # if more than one character, it isn't
            _guess_status = GuessStatus.INVALID_GUESS 
            return _guess_status

        if self.letter not in string.ascii_uppercase:

            # if not an upper case letter, it isn't
            _guess_status = GuessStatus.INVALID_GUESS
            return _guess_status 

        # if we reach this point, it's a valid letter - need to see if in word or not
        _guess_status = GuessStatus.NOT_SET_YET  
        return _guess_status
    
    @guess_status.setter
    def guess_status(self, value):

        # when setting the guess, just store its letter(s)
        self._guess_status = value

# ==========================
# class containing each game
# ==========================

class Game:

    """
        Each game consists of:
        - the word to be guessed
        - the number of guesses allowed
        - a list of the correct guesses
        - a list of the wrong guesses
        - which is the current guess being considered
    """

    def __init__(self,*,word:str,number_guesses_allowed:int):

        # when you start a game, store the word being guessed, and how many guesses allowed
        self.word = word.upper()
        self.number_guesses_allowed = number_guesses_allowed

        # initially there are no correctly and wrongly guessed letters
        self.correct_guesses = []   
        self.wrong_guesses = []   

        # there is no current guess yet
        self.current_guess = None

    def make_guess(self,guess:Guess):
        
        # called for each guessed letter

        # if this is one of the letters already guessed for this game, record this (we'll report 
        # on the error later)
        if guess.letter in (self.correct_guesses + self.wrong_guesses):
            guess.guess_status = GuessStatus.ALREADY_GUESSED
        else:
            
            # update status for this letter (depending on whether in word or not) and add it to the list of
            # correct or wrong guesses
            if (guess.letter in self.word):
                guess.guess_status = GuessStatus.CORRECT
                self.correct_guesses.append(guess.letter)
            else:
                guess.guess_status = GuessStatus.WRONG
                self.wrong_guesses.append(guess.letter)

        # this is the current guess for the game
        self.current_guess = guess
                   
    def show_status_message(self):

        # displays an update message on progress
        
        # determine message to be displayed according to whether guess was valid, correct or wrong
        if self.current_guess.guess_status == GuessStatus.ALREADY_GUESSED:
            letter_update_message = "You've already guessed {0}".format(guess.letter)
        elif self.current_guess.guess_status == GuessStatus.CORRECT:
            letter_update_message = "Congratulations: the letter " + self.current_guess.letter + " does appear."
        else:
            letter_update_message = "Sorry: the letter " + self.current_guess.letter + " does not appear."

        # show a suitable message after each guess (the current progress comes from another property)
        msg = \
            letter_update_message + "\n\n" + \
            self.current_progress + "\n\n" + \
            "Correct letters you have guessed so far: " + " ".join(self.correct_guesses) + "\n" + \
            "Wrong letters you have guessed so far: " + " ".join(self.wrong_guesses) + "\n\n" + \
            "You have {0} of {1} guesses left".format(self.number_guesses_left,self.number_guesses_allowed) + "\n\n" 

        show_message(msg,"Hangman")

    @property
    def number_guesses_left(self):
        
        # how many guesses user has left (correct guesses don't count)
        return self.number_guesses_allowed - len(self.wrong_guesses)

    @property
    def current_progress(self):
        
        # create a string of either underscores or letters
        current_state = ""

        for character in self.word:

            if len(current_state) > 0:
                current_state += " ";

            if character in (self.correct_guesses + self.wrong_guesses):
                current_state += character.upper()
            else:
                current_state += "_"

        return current_state

    @property 
    def if_lost(self):

        # if no guesses left
        return (self.number_guesses_left <= 0)
        
    @property 
    def if_won(self):

        # if word complete
        word_letters = set(self.word)
        guessed_letters = set(self.correct_guesses + self.wrong_guesses)
        
        # word is complete if there are no letters in word which aren't in guessed letters
        return (len(word_letters - guessed_letters) == 0)

# =================
# playing each game
# =================

# the code to play hangman
hangman = Game(word="Ladder",number_guesses_allowed=5)

# start game
show_message(
    "Guess this {0}-letter word.  You can have up to {1} wrong guesses.  Good luck!".format(len(hangman.word),hangman.number_guesses_allowed),
    "Wise Owl Hangman"
)

# keep trying letters until hung or guessed word
while True:

    # next guess
    next_letter = input("Guess next letter ==> ").upper()
    guess = Guess(next_letter)

    # decide what to do based on whether it's valid or not
    if guess.guess_status == GuessStatus.INVALID_GUESS:
        show_message("Each guess must be a single letter!","Error")
    else:

        # if it's a valid letter, see if it's already been guessed, and if not wehther correct or not
        hangman.make_guess(guess)
        
        # no point checking for won or lost if had already guessed
        if guess.guess_status != GuessStatus.ALREADY_GUESSED:

            # if word guessed, end game
            if hangman.if_won:
                show_message("Congratulations - you guessed the word {0}".format(hangman.word),"Well done!")
                break

            # if no more guesses, end game
            if hangman.if_lost:
                show_message("Sorry - you have used up all your guesses - the word was {0}".format(hangman.word),"Commiserations")
                break

        # display status message and continue (the status will say the letter has already been guessed, is 
        # correct or is wrong)
        hangman.show_status_message()
            
        # this command isn't needed (will continue anyway) but makes things clearer
        continue

# end thoughts!
show_message( 
    "You could obviously have written this game in many different ways - have a think about which classes, properties and methods you would have used!", 
    "Closing thought ..." 
)
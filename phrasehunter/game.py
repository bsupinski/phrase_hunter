from phrase import Phrase
from datetime import datetime
from dateutil import relativedelta
import random
class Game:
    time_format = "%H:%M:%S%p"
    
    
    def __init__(self):
        self.game_phrase = None
        self.warning = False
        self.guessed_letters = []
        
        self.max_tries = 2
        self.wrong_tries = 0
        self.start_time = None
        self.highscore = None
        self.phrases = ["The Way of the Kings", "Words of Radiance", "Oathbringer", "Rhythm of war", "Edgedancer", "Dawnshard", "The Final Empire", "Ther Well of Ascension", "The Hero of Ages", "Secret History", "The Alloy of Law", "Shadows of Self", "The Bands of Mourning", "The Lost Metal", "Tress of the Emerald Sea", "Yumi and The Nightmare Painter", "The Sunlit Man", "Elantris", "Warbreaker"]

   
    
    def set_phrase(self):
        self.game_phrase = Phrase("cat")
        # self.game_phrase = Phrase(random.choice(self.phrases))


    def welcome(self):
        print(f"""========================\nWelcome to Phrase Hunter\n========================\n\nPlease choose a single letter.\nYou will have {self.max_tries} wrong guesses till the game ends."""
        )
        input("Press enter to continue...")
        self.set_phrase()
        print("Here is your secret prhase")
        
        self.game_phrase.phrase_reveal(self.guessed_letters)


    def display_game_info(self):
        print(f"You have {self.max_tries - self.wrong_tries} remaining attemp(s).\n")
        print(f"Selected letters: {", ".join(self.guessed_letters)}")
        print(f"{self.game_phrase.phrase}")


    def check_guesses(self):
        #Show the user current game info
        self.display_game_info()
        #Reveal guessed letters
        self.game_phrase.phrase_reveal(self.guessed_letters)
        


    def user_guess(self):
        #Has the user guess a letter as game is not over.
        while self.game_phrase.hidden_phrase != self.game_phrase.phrase and self.wrong_tries < self.max_tries:
            user_guess = input("Select a letter to guess:  ")
            #Check valid guess
            if not user_guess.isalpha() or len(user_guess) != 1:
                #Gives one chance for a mistype
                if not self.warning:
                    self.warning = True
                    print("Please choose a single letter. You are allowed one mulligan. Next will deduct a guess")
                #Mesasage if guess is not a single letter
                else:
                    self.wrong_tries += 1
                continue
            
            #Check to see if letter already guessed
            if user_guess in self.guessed_letters:
                self.wrong_tries += 1
                print(f"You already guessed {user_guess}. A try has been deducted")
                continue
            
            #Append the guessed letter to all guesses
            self.guessed_letters.append(user_guess)
            
            if user_guess not in self.game_phrase.phrase:
                self.wrong_tries += 1
                self.set_score()
                print(f"{self.current_score}")
            
            self.check_guesses()
        


    def game_win(self):
        if self.game_phrase.hidden_phrase == self.game_phrase.phrase:
            print(f"Congrats you won with a time.")


    def game_loss(self):
        if self.game_phrase.phrase != self.game_phrase.hidden_phrase:
            total_right = 0
            for letter in self.game_phrase.hidden_phrase:
                if letter.isalpha():
                    total_right += 1
            print(f"You did not guess correct\nThe phrase was {self.game_phrase.phrase}\nYou got {total_right} letters right.")


    def play_again(self):
        choice = input("Enter '1' to play again\nEnter '2' to stop playing.\n")
        if choice == "1":
            print("Restarting")
            self.run_game()
        elif choice == "2":
           print("Thank you for playing")
           print("Exiting game")
           exit()


    def game_reset(self):
        self.game_phrase = None
        self.wrong_tries = 0
        self.warning = False
        self.guessed_letters = []


    def run_game(self):
        self.game_reset()
        self.welcome()
        self.user_guess()
        self.game_loss()
        self.game_win()
        self.play_again()





if __name__ == "__main__":
    # new_game = Game()
    # new_game.run_game()
    
    starttime = datetime.now()
    print(starttime)
    input("press enter...   ")
    timediff = datetime.now() - starttime
    print(timediff)
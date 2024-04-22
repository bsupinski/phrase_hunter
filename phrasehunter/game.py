from phrase import Phrase
import random
class Game:
    def __init__(self):
        self.game_phrase = None
        self.total_tries = 0
        self.warning = False
        self.guessed_letters = []
        self.phrases = ["The Way of the Kings", "Words of Radiance", "Oathbringer", "Rhythm of war", "Edgedance", "Dawnshard", "The Final Empire", "Ther Well of Ascension", "The Hero of Ages", "Secret History", "The Alloy of Law", "Shadows of Self", "The Bands of Mourning", "The Lost Metal", "Tress of the Emerald Sea", "Yumi and The Nightmare Painter", "The Sunlit Man", "Elantris", "Warbreaker"]

    def welcome(self):
        print("""
========================
Welcome to Phrase Hunter
========================

Please choose a single letter.
You will have 5 wrong guesses till the game ends.
    """
        )
        input("Press enter to continue...")
        self.set_phrase()
        
        print(" Here is your secret prhase")
        
        self.game_phrase.phrase_reveal(self.guessed_letters)


    def set_phrase(self):
        self.game_phrase = Phrase(random.choice(self.phrases))
        


    def guess(self):
        guess = input("Please guess a letter you think is in the phrase:  ")
        while not guess.isalpha() or  len(guess) != 1:
            if not self.warning:
                print("Sorry that is not a single letter.")
                print("You are allowed one mistype, next will cost a life\n")
                guess = input("Please guess a letter you think is in the phrase:  ")
                
                self.warning = True
            else:
                print("Sorry that is not a single letter.\n")
                guess = input("Please guess a letter you think is in the phrase:  ")
                self.total_tries += 1
        self.guessed_letters.append(guess.lower())


    def check_guess(self):
        while self.game_phrase.phrase != self.game_phrase.hidden_phrase:
            self.guess()
            self.game_phrase.phrase_reveal(self.guessed_letters)

    def run_game(self):
        self.welcome()
        self.check_guess()





if __name__ == "__main__":
    Game().run_game()
    

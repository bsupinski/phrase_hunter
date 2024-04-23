from phrase import Phrase
import random
class Game:
    def __init__(self):
        self.game_phrase = None
        self.wrong_tries = 0
        self.max_tries = 2
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


    def display_game_info(self):
        print(f"Your guesses so far: {" ".join(self.guessed_letters)}")
        print(f"You have {self.max_tries - self.wrong_tries} remaining attemp(s).\n")


    def guess(self):
        self.game_loss()
        self.display_game_info()
        guess = input("Please guess a letter you think is in the phrase:  ")
        while not guess.isalpha() or len(guess) != 1 or guess in self.guessed_letters:
            self.game_loss()
            if guess in self.guessed_letters:
                self.wrong_tries += 1
                self.display_game_info()
                print("You have already guessed that letter.\n")
                guess = input("Please guess a letter you think is in the phrase:  ")
            elif not self.warning:
                self.display_game_info()
                print("Sorry that is not a single letter.\n")
                print("You are allowed one mistype, next will cost an attempt\n")
                self.warning = True
                guess = input("Please guess a letter you think is in the phrase:  ")
            else:
                self.wrong_tries += 1
                self.display_game_info()
                print("Sorry that is not a single letter.\n")
                guess = input("Please guess a letter you think is in the phrase:  ")
        self.guessed_letters.append(guess.lower())
        if guess not in self.game_phrase.phrase:
            self.wrong_tries += 1


    def check_guess(self):
        while self.game_phrase.phrase != self.game_phrase.hidden_phrase:
            self.game_loss()
            self.guess()
            self.game_phrase.phrase_reveal(self.guessed_letters)


    def game_loss(self):
        if self.wrong_tries == self.max_tries:
            print(f"You ran out of attempts.")
            self.play_again()


    def play_again(self):
        user_input = input("Press '1' to playa gain\nPress '2' to quit.")
        if user_input == 1:
            self.run_game()
        elif user_input == 2:
            quit()
        
        print(user_input)    
        if user_input == 1:
            self.welcome()
        elif user_input == 2:
            quit()

    def run_game(self):
        self.welcome()
        self.check_guess()





if __name__ == "__main__":
    Game().run_game()
    

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


    def set_phrase(self):
        self.game_phrase = Phrase(random.choice(self.phrases))


    def welcome(self):
        print(f"""========================\nWelcome to Phrase Hunter\n========================\n\nPlease choose a single letter.\nYou will have {self.max_tries} wrong guesses till the game ends."""
        )
        input("Press enter to continue...")
        self.set_phrase()
        
        print(" Here is your secret prhase")
        
        self.game_phrase.phrase_reveal(self.guessed_letters)


    def display_game_info(self):
        print(f"You have {self.max_tries - self.wrong_tries} remaining attemp(s).\n")

    
    def check_guesses(self):
        self.game_phrase.phrase_reveal(self.guessed_letters)


    def user_guess(self):
        while self.game_phrase.hidden_phrase != self.game_phrase.phrase and self.wrong_tries != self.max_tries:
            print(self.game_phrase.hidden_phrase)
            print(self.game_phrase)
            user_guess = input("Please select a letter to guess:    ")
            if user_guess not in self.game_phrase.phrase:
                self.wrong_tries += 1
            self.guessed_letters.append(user_guess)
            self.check_guesses()


    def game_loss(self):
        if self.wrong_tries == self.max_tries:
            total_right = 0
            for letter in self.game_phrase.hidden_phrase:
                if letter.isalpha():
                    total_right += 1
            print(f"You did not guess correct\nThe phrase was {self.game_phrase.phrase}\nYou got {total_right} letters right.")


    def game_win(self):
        if self.game_phrase.hidden_phrase == self.game_phrase.phrase:
            print("Congrats you won")

        self.play_again()



    def play_again(self):
        choice = input("Enter '1' to play again\nEnter '2' to stop playing.")
        if choice == 1:
            self.run_game()
        elif choice == 2:
            exit()
            
        self.play_again()

    def run_game(self):
        self.welcome()
        self.user_guess()
        self.game_loss()
        self.game_win()





if __name__ == "__main__":
    Game().run_game()
    

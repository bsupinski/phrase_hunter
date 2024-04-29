from phrasehunter.phrase import Phrase
from datetime import datetime
import random
class Game:
    
    def __init__(self):
        self.game_phrase = None
        self.warning = False
        self.guessed_letters = []
        self.max_tries = 7
        self.wrong_tries = 0
        self.start_time = None
        self.current_score = None
        self.high_score = None
        self.phrases = [
            Phrase("The Way of the Kings"), 
            Phrase("Words of Radiance"), 
            Phrase("Oathbringer"), 
            Phrase("Rhytm of War"), 
            Phrase("Edgedance"),
            Phrase("Dawnshard"),
            Phrase("The Final Empire"),
            Phrase("The Well of Ascension"),
            Phrase("The Hero of Ages"),
            Phrase("Secret History"),
            Phrase("The ALloy of Law"),
            Phrase("Shadow of Self"),
            Phrase("The Bands of Mourning"),
            Phrase("The Lost Metal"),
            Phrase("Tress of the Emerald Sea"),
            Phrase("Yumi and the Nightmare Painter"),
            Phrase("The Sunlit Man"),
            Phrase("Elantris"),
            Phrase("Warbreaker")
        ]


    def set_start_time(self):
        self.start_time = datetime.now()


    def set_current_score(self):
        self.current_score = datetime.now() - self.start_time


    def format_score(self, score):
        return f"{str(score.seconds // 60).rjust(2, '0')}m:{str(score.seconds % 60).rjust(2, '0')}s:{str(score.microseconds)[:2]}ms"


    def set_phrase(self):
        self.game_phrase = Phrase(random.choice(self.phrases))
        self.game_phrase = self.game_phrase.phrase


    def welcome(self):
        print(f"""========================\nWelcome to Phrase Hunter\n========================\nPlease choose a single letter.\nYou will have {self.max_tries} wrong guesse(s) till the game ends."""
        )
        if self.high_score == None:
            print("There is no current high score")
        else:print(f"The current high score is {self.format_score(self.high_score)}")
        input("Press enter to continue...")
        self.set_phrase()
        self.set_start_time()
        print("Starting Time: 00m:00s:00ms")
        self.game_phrase.phrase_reveal(self.guessed_letters)


    def display_game_info(self):
        self.set_current_score()
        print(f"You have {self.max_tries - self.wrong_tries} remaining attemp(s).          Current Score: {self.format_score(self.current_score)}")
        print(f"Selected letters: {','.join(self.guessed_letters)}")


    def check_guesses(self):
        self.display_game_info()
        self.game_phrase.phrase_reveal(self.guessed_letters)


    def user_guess(self):
        while self.game_phrase.hidden_phrase != self.game_phrase.phrase and self.wrong_tries < self.max_tries:
            user_guess = input("Select a letter to guess:  ")
            print("")
            if not user_guess.isalpha() or len(user_guess) != 1:
                if not self.warning:
                    self.warning = True
                    print("Please choose a single letter. You are allowed one mulligan. Next will deduct a guess.")
                    self.display_game_info()
                    print(f'{self.game_phrase.hidden_phrase}')
                    print("")
                else:
                    self.wrong_tries += 1
                    print("Please choose a single letter.")
                    self.display_game_info()
                    print(f'{self.game_phrase.hidden_phrase}')
                    
                continue
            
            if user_guess in self.guessed_letters:
                self.wrong_tries += 1
                print(f"You already guessed {user_guess}. A try has been deducted")
                self.display_game_info()
                print(f'{self.game_phrase.hidden_phrase}')
                continue

            self.guessed_letters.append(user_guess)
            
            if user_guess not in self.game_phrase.phrase and len(user_guess) == 1:
                self.wrong_tries += 1
            
            self.check_guesses()


    def game_win(self):
        if self.game_phrase.hidden_phrase == self.game_phrase.phrase:
            if self.high_score == None:
                self.high_score = self.current_score
                print(f"\nCongrats you guessed correctly and have the new high score at {self.format_score(self.high_score)}\n")
            elif self.current_score < self.high_score:
                self.high_score = self.current_score
                print(f"\nCongrats you guessed correctly and have the new high score at {self.format_score(self.high_score)}\n")
            else:
                print(f"\nCongrats you guessed the phrase correct with a high score of {self.format_score(self.current_score)}\nThe current high score is {self.format_score(self.high_score)}\n")


    def game_loss(self):
        if self.game_phrase.phrase != self.game_phrase.hidden_phrase:
            total_right = 0
            for letter in self.game_phrase.hidden_phrase:
                if letter.isalpha():
                    total_right += 1
            print(f"You did not guess correctThe phrase was {self.game_phrase.phrase}You got {total_right} letters right.")


    def play_again(self):
        while True:
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
        self.warning = False
        self.guessed_letters = []
        
        self.wrong_tries = 0
        self.start_time = None
        self.current_score = None


    def run_game(self):
        self.game_reset()
        self.welcome()
        self.user_guess()
        self.game_loss()
        self.game_win()
        self.play_again()





if __name__ == "__main__":
    new_game = Game()
    new_game.run_game()
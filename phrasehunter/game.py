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
        print(self.wrong_tries, self.max_tries)
        print(f"You have {self.max_tries - self.wrong_tries} remaining attemp(s).\n")
        print(f"Selected letters: {", ".join(self.guessed_letters)}")


    def check_guesses(self):
        #Reveal guessed letters
        self.game_phrase.phrase_reveal(self.guessed_letters)
        #Show the user current game info
        self.display_game_info()


    def user_guess(self):
        #Has the user guess a letter as long as the game is not over
        while self.game_phrase.hidden_phrase != self.game_phrase.phrase and self.wrong_tries != self.max_tries:
            print(self.game_phrase.hidden_phrase)
            user_guess = input("Please select a letter to guess:   ")
            #Check for valid guess
            while not user_guess.isalpha() or len(user_guess) != 1 or user_guess in self.guessed_letters:
                #Check to see if letter already guessed
                if user_guess in self.guessed_letters:
                    print("You already guessed that letter.\n")
                #Gives one mistake for a mistype
                elif not self.warning:
                    self.warning = True
                    self.wrong_tries =- 1
                    print("Please choose a single letter. You are allowed one mulligan. Next will deduct a guess.")
                #Message if guess not a single letter.
                else:
                    print("Please choose a single letter")
                
                self.wrong_tries += 1
                if self.wrong_tries != self.max_tries:
                    user_guess = input("Please select a letter to guess:   ")

            #Deduct an attempt if letter not in phrase
            if user_guess not in self.game_phrase.phrase and self.wrong_tries != self.max_tries:
                self.wrong_tries += 1
            #Append the guess if legit guess
            self.guessed_letters.append(user_guess)
            #Check if user guess is in phrase.
            self.check_guesses()


    def game_loss(self):
        if self.wrong_tries == self.max_tries:
            total_right = 0
            for letter in self.game_phrase.hidden_phrase:
                if letter.isalpha():
                    total_right += 1
            print(f"\nYou did not guess correct\nThe phrase was {self.game_phrase.phrase}\nYou got {total_right} letters right.\n")


    def game_win(self):
        if self.game_phrase.hidden_phrase == self.game_phrase.phrase:
            print("Congrats you won")


    def play_again(self):
        choice = input("Enter '1' to play again\nEnter '2' to stop playing.")
        if choice == 1:
            self.run_game()
        elif choice == 2:
            exit()


    def run_game(self):
        self.welcome()
        self.user_guess()
        self.game_loss()
        self.game_win()
        self.play_again()





if __name__ == "__main__":
    Game().run_game()
    

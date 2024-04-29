class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
        self.hidden_phrase = ""


    def __str__(self):
        return self.phrase


    def phrase_reveal(self, guesses):
        self.hidden_phrase = ""
        for letter in self.phrase:
            if letter.lower() in guesses:
                    self.hidden_phrase += letter
            elif letter == " ":
                self.hidden_phrase += letter
            else:
                self.hidden_phrase += "-"
        print(f"You're Phrase:\n{self.hidden_phrase}")


if __name__ == "__main__":
    test = Phrase("The Way of the King")
    test.phrase_reveal(["k", "i", "o","a", "b", "c", "w"])

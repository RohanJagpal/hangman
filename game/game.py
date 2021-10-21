from random import choice
from os import system, name

def clear():
    if name =="nt":
        _ = system("cls")
    else:
        _=system("clear")

class Hangman:
    def __init__(self, minWordLength: int = 3, tries: int = 11) -> None:
        self.__minWordLength = minWordLength
        self.__state = ""
        self.__guesses = []
        self.__remaining = tries

    def __generateWord(self) -> str:
        with open('game/en', 'r') as f:
            word = ""
            while len(word) < self.__minWordLength and word.lower() != word:
                word = choice(f.read().splitlines())
            for letter in word:
                self.__state += "_"
            return word

    def __addIncorrectGuess(self, char: str) -> None:
        self.__remaining -= 1
        self.__guesses.append(char)

    def __addCorrectGuess(self, char: str) -> None:
        self.__guesses.append(char)
        newWord = ""
        for i in range(len(self.__word)):
            if self.__word[i] == char:
                newWord += char
            else:
                newWord += self.__state[i]
        self.__state = newWord

    def __guess(self) -> str:
        if not self.__remaining > 0:
            return self.__state
        print(f"\n\nYou have {self.__remaining} guesses remaining.\n\nSo far you have guessed {tuple(self.__guesses)}.\n")
        guess = input("Guess a letter: ")
        if len(guess) != 1:
            print("ERROR: Please enter a single letter.")
            return self.__state
        if guess not in self.__word:
            self.__addIncorrectGuess(guess)
        else:
            self.__addCorrectGuess(guess)
        return self.__state

    def run(self) -> None:
        self.__word = self.__generateWord()
        while self.__state != self.__word:
            clear()
            if self.__remaining > 0:
                print(self.__state)
                self.__state = self.__guess()
            else:
                print(f"You ran out of guesses!\nThe correct word was{self.__word}.")
        print("You guessed the word!")       
"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730529974"

WORD: str = input("Enter a 5-character word: ")
character: str = input("Enter a single character: ")

print("Searching for " + str(character) + " in " + str(WORD))
print(str(character) + " found at index " + WORD[0])
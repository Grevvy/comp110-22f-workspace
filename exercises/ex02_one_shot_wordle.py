"""EX02 - One Shot wordle."""

__author__ = "730529974"

secret: str = "python"
guess: str = (input("What is your 6-letter guess? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
a: str = ""
exists: bool = False
match: int = 0

while len(guess) != len(secret):
    guess = str(input("That was not six letters! Try again: "))
    
while i < 6:
    if guess[i] == secret[i]:
        a += GREEN_BOX
    else:
        a += WHITE_BOX
    i += 1

while exists == False and match > len(secret):
    if secret[match] == secret[match]:
        exists == True
    else: 
        match += 1

print(a)




if guess != (secret):
    print("Not quite. Play again soon!")
if guess == secret:
    print("Woo! You got it!")




    
        
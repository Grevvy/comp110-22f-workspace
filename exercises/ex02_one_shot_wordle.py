"""EX02 - One Shot wordle."""

__author__ = "730529974"

secret: str = "python"
guess: str = (input("What is your 6-letter guess? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
a: str = ""
exist: bool = False
b: int = 0


while len(guess) != len(secret):
    guess = str(input("That was not 6 letters! Try again: "))
    
while i < 6:
    if guess[i] == secret[i]:
        a += GREEN_BOX
    else:
        while exist is not True and b < len(secret):
            if secret[b] == guess[i]:
                exist = True
            else:
                b += 1
        if exist is True:
            a += YELLOW_BOX
        if exist is False:
            a += WHITE_BOX
    i += 1
    b = 0
    exist = False

print(a)

if guess != (secret):
    print("Not quite. Play again soon! ")
if guess == secret:
    print("Woo! You got it! ")        
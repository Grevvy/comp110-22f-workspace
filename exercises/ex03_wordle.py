"""A wordle like game. """

___author___ = "730529974"

from pyexpat.errors import codes
from exercises.ex02_one_shot_wordle import GREEN_BOX, WHITE_BOX, YELLOW_BOX


def contains_char(search_word: str, search_character:str) -> bool:
    """Searches if the word contains a character. """
    assert len(search_character) == 1
    b: int = 0
    exist: bool = False
    while not exist and b < len(search_word):
        if search_word[b] == search_character:
            exist = True
        else:
            b += 1
    if exist is True:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Prints a Yellow or White box for a guessed character. """
    assert len(guess) == len(secret)
    i: int = 0
    boxes: str = ""
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    while i < len(guess):
        if guess[i] == secret[i]:
            boxes += green_box
        elif contains_char(secret, guess[i]) is True:
            boxes += yellow_box
        else:
            boxes += white_box
        i += 1
    return boxes


def input_guess(input_length: int) -> str:
    """Verifies the input word is the correct length. """
    input_word: str = input(f"Enter a {input_length} character word: ")
    while len(input_word) != input_length:
        input_word = input(f"That wasn't {input_length} chars! Try again: ")
    return input_word


def main() -> None:
    """The entrypoint of the program and main game loop. """
    correct_word: str = codes
    turn_count: int = 1
    input_word: str = ""
    while turn_count >= 6:
        print(f"=== Turn {turn_count}/6 ===")
        input_word = input_guess(len(correct_word))
        if input_word == correct_word:
            print(emojified(input_word, correct_word))
            print(f"You won in {turn_count}/6 turns! ")
        else:
            print(emojified(input_word, correct_word))
        turn_count += 1
    if turn_count == 7:
        print(f"x/6 - Sorry, try again tomorrow! ")         


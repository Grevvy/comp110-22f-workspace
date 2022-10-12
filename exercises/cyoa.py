"""A quick cat adventure game."""


__author__ = "730529974"


points: int = 0
player: str = ""
NAMED_CONSTANT: str = "\U00000000"
CAT: str = "\U0001F63A"
CAT_DEATH: str = "\U0001F63F"
CAT_TREAT: str = "\U0001F638"
CAT_HEARTS: str = "\U0001F63B"
CAT_SLY: str = "\U0001F63C"


def main() -> None:
    global points
    greet()    
    while points < 3:
        keep_playing()
        path_select()
    if points == 3:
        eat_treats(3)
        print(f"Congratulations {player} you are now a chonky cat. {CAT_HEARTS} ")


def greet() -> None:
    global player
    print("Welcome to 'Cat Path' ")
    print("You will play as a cat choosing paths. ")
    print("If you choose the right path, you will receive a cat treat" )
    print("If you choose the wrong path nine times, you will be out of lives. ")
    player = input(f"What is your {CAT} name? ")


def eat_treats(a: int) -> int:
    global points
    print(input(f"Press enter to eat your {points} treats and win the game. "))
    points -= a
    return points


def path_select() -> None:
    from random import randint
    global points
    path: str = input(f"{player}, choose a path. left or right. ")
    correct_path: str = ""
    a: int = randint(0, 1)
    b: int = 9
    if a == 0:
        correct_path = "left"
    elif a == 1:
        correct_path = "right"
    if path == correct_path:
        print(f"{player}, Good job! You get a treat! {CAT_TREAT} ")
        points += 1
    else:
        print(f"{player}, You chose the wrong path and have lost a life. ")
        b -= 1
        print(f"You have {b} lives left")
    if b == 0:
        death()


def keep_playing() -> None:
    print(f"You have gathered {points} treats.")
    choice: str = input(f"{player} would you like to continue? y/n ")
    if choice == "n":
        exit_game()


def death() -> None:
    print(f"{player}, you have lost your ninth life.")
    print(f"Game over. {CAT_DEATH} ")
    print(f"Number of treats obtained: {points}")
    quit()  


def exit_game() -> None:
    print(f"{player}, you live to die another day. {CAT_SLY} ")
    print(f"Thanks for playing, {player}")
    print(f"your total score is: {points}")
    quit()


if __name__ == "__main__":
    main()

from random import randint

question: str = input("What is your yes/no question? ")
response: int = randint(0, 19)

if response == 0:
    print("It is certain. ")
elif response == 1:
    print("It is decidedly so. ")
elif response == 2:
    print("WIthout a doubt. ")
elif response == 3:
    print("Yes definitely. ")
elif response == 4:
    print("You may rely on it. ")
elif response == 5:
    print("As i see it yes. ")
elif response == 6:
    print("Most likely. ")
elif response == 7:
    print("Outlook good. ")
elif response == 8:
    print("Yes. ")
elif response == 9:
    print("Signs point to yes. ")
elif response == 10:
    print("Reply hazy, try again. ")
elif response == 11:
    print("Ask again later. ")
elif response == 12:
    print("Better not tell you now. ")
elif response == 13:
    print("Cannot predict now. ")
elif response == 14:
    print("Concentrate and ask again. ")
elif response == 15:
    print("Don't count on it. ")
elif response == 16:
    print("My reply is no. ")
elif response == 17:
    print("My sources say no. ")
elif response == 18:
    print("Outlook not so good. ")
else:
    print("Very doubtful. ")
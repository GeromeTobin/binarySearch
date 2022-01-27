import random
import math

rounds = int(100)
winRate = int(0)
maxInit = int(10000000000000)
minInit = int(1)
maxGuess = int(math.log2(maxInit - minInit + 1))

def Guess():
    correct = int(random.randint(minInit, maxInit))
    guess = int(maxInit)
    increment = int(maxInit/2)
    guess = int(guess - increment)
    increment = int(increment/2)
    i = 0
    end = 0
    while end != 1:
        i += 1
        if guess > correct:
            guess = int(guess - increment)
            increment = int(increment/2)
        elif guess < correct:
            guess = int(guess + increment)
            increment = int(increment/2)
        if guess - correct == 0:
            return 1
            break
        if i == math.log2(maxInit - minInit + 1):
            print(correct)
            print(guess)
            return 0
            end = 1
            break
        if increment < 1:
            increment = 1

for x in range(rounds):
    win = Guess()
    winRate += win

screen_width = 80
sentence = [str(winRate) + "/" + str(rounds), "guessed a number from 1-" + str(maxInit) + " in under " + str(maxGuess) + " tries",
 "this is the fastest you will get the number while using this program",
  "I am always here if you need a binary search algorithm!",
 "Thank you for your time."]
 
print("*"*screen_width)
for i in range(4):
    centered = sentence[i].center(screen_width - 4)
    output = "**{0}**".format(centered)
    print(output)
print("*"*screen_width)

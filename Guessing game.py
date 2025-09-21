import random

answer = random.randint(1, 100)
guess = 0

count = 0
while guess != answer:
    guess = int(input("Guess a number between 1 and 100: "))
    count += 1
    if guess < answer:
        print ("Too low! Try again")
    elif guess > answer:
            print ("Too high! Try again")
    elif guess == answer:
        print ("Hooray")

        print ("You guessed it in " + str(count) + " tries!")

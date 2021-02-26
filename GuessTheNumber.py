import random

def guess(x):
    random_number = random.randint(1,x) #random number between 1 and x
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} : "))
        if guess > random_number:
            print("Sorry! Too High.")
        elif guess < random_number:
            print("Sorry! Too Low.")
        
    print(f"Congrats You guessed the random number i.e {random_number}")


def ComputerGuess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low,high) #low = high , push errror
        feedback = input(f"Is {guess} too high(h), too low(l) or correct(c) : ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Computer has guessed the number {guess}")

guess(10)
ComputerGuess(10)
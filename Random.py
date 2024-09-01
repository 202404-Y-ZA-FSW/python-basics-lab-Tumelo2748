import random

def randomNumber():
    return random.randint(1, 100)

def playGame():
    secretNumber = randomNumber()
    attempts = 0

    while True:
        attempts += 1
        guess = int(input("Guess the number (between 1 and 100): "))
        if guess == secretNumber:
            print("Congratulations! You guessed the number correctly.")
            print(f"It took you {attempts} attempts to guess correctly.")
            break
        elif guess < secretNumber:
            print("Too low! Try again.")
            continue
        elif guess > secretNumber:
            print("Too high! Try again.")
            continue
    
    playAgain = input("Do you want to play again? (yes/no): ").lower()
    if playAgain == "yes":
        playGame()
print('Welcome to My Game of Inteligent people that can Guess numbers 😎')
playGame()
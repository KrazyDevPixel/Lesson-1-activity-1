import random

number_list = [3, 7, 15, 22, 31, 44, 50]
secret_number = random.choice(number_list)

print("Welcome to the Guessing Game!")
print("I'm thinking of a number from this list:")
print(number_list)

attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess not in number_list:
            print("That number is not in the list.")
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed it!")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

number = 7
guess = 0
print("puzzle game!")

if guess != number:
    guess = int(input("please input your guess number："))

if guess == number:
    print("Congratulations! You are so smart!")
if guess < number:
    print("Your guess is smaller than actual value!")
if guess > number:
    print("Your guess is bigger than actual value! Try again!")
import random

answer = random.randint(1, 10)
count = 0

while True:
    print("Your guess? ", end="")
    guess = int(input())
    count += 1

    if answer == guess:
        print("correct answer. your guess count is %i" %count)
        break
    elif answer > guess:
        print("Bigger")
    else:
        print("Smaller")
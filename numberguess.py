import random
number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
guess_history = []

while True:
    x = int(input("Guess the number between 1 and 30 "))

    if x > number:
        guess_history.append(x)
        print("Less")
    elif x < number:
        guess_history.append(x)
        print("Greater")
    else:
        print("Correct")
        print(guess_history)
        break
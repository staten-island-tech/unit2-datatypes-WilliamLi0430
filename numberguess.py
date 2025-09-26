import random
number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

while True:
    x = int(input("Guess the number between 1 and 10 "))

    if x > number:
        print("Less")
    elif x < number:
        print("Greater")
    else:
        print("Correct")
        break
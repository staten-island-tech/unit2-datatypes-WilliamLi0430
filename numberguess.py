import random
number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

while True:
    x = int(input("Guess the number between 1 and 30 "))

    if x > number:
        print("Less")
    elif x < number:
        print("Greater")
    else:
        print("Correct")
        break
import random
int(input("Guess the number" ))
list (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
number = random.choice(list)

while True:
    if input > number:
        print("Less")
    elif input == number:
        print("Equal")
    else:
        print("Greater")
import random
number = random.choice(list(range(1000000)))
guess_history = []

while True:
    x = int(input("Guess the number between 1 and 1000000 "))

    if x > number:
        guess_history.append(x)
        print("Less")
        print(f"You have guessed {guess_history}")
    elif x < number:
        guess_history.append(x)
        print("Greater")
        print(f"You have guessed {guess_history}")
    else:
        guess_history.append(x)
        print("Correct")
        print(f"Here are your guesses: {guess_history}")
        break
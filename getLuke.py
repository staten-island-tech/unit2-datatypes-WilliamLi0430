def get_Luke(number):
    Luke = []
    for i in range (1, number + 1):
        if number % i == 0:
            Luke.append (i)
    return Luke

Zheng = int(input("What is the number you would like factored? "))

print(get_Luke(Zheng))
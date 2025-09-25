first = int(input("What is your first number? "))
second = int(input("What is your second number? "))

def get_Luke(first):
    Luke = []
    for i in range (1, first + 1):
        if first % i == 0:
            Luke.append (i)
    return Luke

print(get_Luke(Zheng))
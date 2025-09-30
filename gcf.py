first = int(input("What is your first number? "))
second = int(input("What is your second number? "))

def wuergbo(first, second):
    gcf = 0
    for i in range(1, first):
        if first % i == 0 and second % i == 0:
            gcf = i
    return gcf
print(wuergbo(first, second))
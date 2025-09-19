bill = float(input("How much was the bill? "))

service = input("Was the service Bad, Okay, Good, or Great? ")
if service == ("Bad"):
    tip = 0
elif service == ("Okay"):
    tip = .15
elif service == ("Good"):
    tip = .2
elif service == ("Great"):
    tip = .25
print(f"You should tip ${tip * bill}")
print (f"Your total bill comes to ${(tip * bill)+ bill}")
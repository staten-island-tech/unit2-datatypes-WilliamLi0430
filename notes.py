#Splits a sentence and tells you how many words are in the sentence. 
""" sentence = input("Insert Sentence")
split = sentence.split()
print(len(split)) """

""" friend_comes = True
money = True
def and_movies(friend, money):
    if friend or money:
        print("Going to the movies")
    else:
        print("I am not going to the movies")
and_movies(friend_comes, money)
 """

#If I have homework, then I cannot go to the movies. 
#But if I change the "homework = True" to "homework = False", 
#I can go to the movies.
""" homework = True

def not_movies(homework):
    if not homework:
        print("Movie Time")
    else:
        print("Homework Time")
not_movies(homework) """

#remember to put int before input when comparing integers to strings.
""" temp = int(input("What is the temperature?"))
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """
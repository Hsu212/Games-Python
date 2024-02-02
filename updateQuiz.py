import random
print("Welcome to my Quizz.I hope you will enjoy!")

select_number = input("Please select one:" )

if select_number.isdigit():
    select_number = int(select_number)

    if select_number == 1:
        print("Let's Start!")

    elif select_number == 2:
        print("Quit!")
        quit()
    else:
        print("Please choose again")
        quit()

r = random.randrange(0,3)
score = 0

ans = input("What is OOP? ")

if ans.lower() == "object oriented programming":
    print("Correct!")
    score+=1

else:
    print("Incorrect!")

ans = input("What is RAM? ")

if ans.lower() == "random access memory":
    print("Correct!")
    score+=1

else:
    print("Incorrect!")

ans = input("What is JVM? ")

if ans.lower() == "java virtual machine":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("Congratulations! You got " + str(score) + " scores.")
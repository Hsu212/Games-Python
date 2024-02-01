print("Welcome To My DSA Quiz!")

playing = input("Do you want to start? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Start...")

score = 0

answer = input("What is the worst case time complexity of linear search algorithms? ")

if answer == "O(n)":
    print("Correct!")
    score += 1;
else:
    print("Incorrect!")

answer = input("What is the best case time complexity of bubble sort algorithm? ")

if answer == "O(n)":
    print("Correct!")
    score += 1;
else:
    print("Incorrect!")

answer = input("What is the difference between stack and queue? ")

if answer.lower() == "a stack is LIFO and a queue is FIFO":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the difference between binary tree and binary search tree? ")

if answer.lower() == "binary tree can have any value in any node and binary search tree has a specific order":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " correct questions")
print("You got " + str((score/4) * 100) + " %")
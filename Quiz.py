print('Welcome to my computer quiz')
playing = input('Do you want to play:')
if playing.lower() != "yes":
    quit()
print("Okay Lets play")
score = 0
answer = input("What is CPU stand for:")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("InCorrect")
answer = input("What is GPU stand for:")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("InCorrect")
answer = input("What is RAM stand for:")
if answer.lower() == "Random Access Memory":
    print("Correct")
    score += 1
else:
    print("InCorrect")
answer = input("What is PSU stand for:")
if answer.lower() == "Power Supply Unit":
    print("Correct")
    score += 1
else:
    print("InCorrect")

    print("You answered " + str(score) + " Questions Correct")
    print("You got " + str((score/4) * 100) + "%")

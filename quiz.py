print ("Welcome to the computer quiz game")
playing = input("Do want to play the game? ")
if playing != "yes" :
    quit()
print("Okay! lets play :) ")
score = 0
answer = input("What is the full form of CPU? ")
if answer.lower() == "Central processing Unit":
    print("correct! ")
    score += 1
else:
    print('incorrect! ')
answer = input("what is RAM? ")
if answer.lower() == "Random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect! ")
answer = input("where is burari? ")
if answer.lower() == "delhi":
    print("correct! ")
    score +=1
else:
    print("incorrect")
answer = input("where is delhi? ")
if answer.lower() == "India":
    print("correct! ")
    score += 1
else:
    print("incorrect! ")
print("you got " + str(score) + " question correct")
print("you got " + str((score/4)*100) + " %")

 
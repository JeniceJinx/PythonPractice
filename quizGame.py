from tkinter.messagebox import YES


print("Welcome to Quiz Game")

playing = input("Do you want play?  ")

if playing != "yes":
    quit()

print( "Ok! Lets Play!")

answer = input("BoyzIIMen is the brainchild of which group member?  ")
if answer == "Nathan Morris":
    print("This is correct!")
else:
    print("Sorry, this is not correct")    
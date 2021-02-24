# Design the WORD JUMBLE GAME

import random

# Banner
print("-"*60)
print("\t\tWELCOME TO THE WORD JUMBLE GAME")
print("The computer shows a jumbled word, You need to guess it")
print("One attempt per word")
print("-"*60)

# List of words
L = ["apples", "monkey", "laptop", "mobile", "python", "random"]

# Randomize the words
random.shuffle(L)

for word in L:

    # Select the word
    # Jumble the word
    temp = list(word)
    random.shuffle(temp)
    jword = ''.join(temp)

    # Show the jumbled word
    print("Word --> ", jword)

    # Input the word from the user
    uword = input("Enter you guess: ")

    # Comparison between selected word and user input
    # Updates the point
    if(uword == word):
        points += 1
        print("Correct guess!")
    else:
        print("Incorrect....")

# Print the results

print("-"*60)
print("SCORE : ", points)
if(points >= 5):
    print("Excellent Playing!")
elif(2 <= points < 5):
    print("Good")
else:
    print("Good luck next time....")
print("-"*60)



# The following the improvisations you could attempt

# 1. Get the words from a text file
# 2. Give two chances for every word
#    With out clue, with a clue
#    mobile -> a device used to make calls
# 3. Add difficulty level with a level manager logic with login details
# 4. Add GUI to this -> tkinter, kivy
# 5. Network gaming
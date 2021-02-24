import random

class wordjumblegame:

    nplayers = 0

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.words = self.initwords()
        wordjumblegame.nplayers += 1

    def showbanner(self):
        print("-"*60)
        print("\t\tWELCOME", self.name.upper(), "TO THE WORD JUMBLE GAME")
        print("The computer shows a jumbled word, You need to guess it")
        print("One attempt per word")
        print("-"*60)

    def initwords(self):
        words = ["apples", "monkey", "laptop", "mobile", "python", "random"]
        random.shuffle(words)
        return words

    def jumble(self, word):
        temp = list(word)
        random.shuffle(temp)
        return ''.join(temp)

    def run(self):

        self.showbanner()
        for word in self.words:

            # Select the word
            # Jumble the word
            jword = self.jumble(word)

            # Show the jumbled word
            print("Word --> ", jword)

            # Input the word from the user
            uword = input("Enter you guess: ")

            # Comparison between selected word and user input
            # Updates the point
            if(uword == word):
                self.points += 1
                print("Correct guess!")
            else:
                print("Incorrect....")
                

    def showresults(self):
        print("\n")
        print(self.name.upper())
        print("-"*60)
        print("SCORE : ", self.points)
        if(self.points >= 5):
            print("Excellent Playing!")
        elif(2 <= self.points < 5):
            print("Good")
        else:
            print("Good luck next time....")
        print("-"*60)
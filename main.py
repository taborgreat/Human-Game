import hangman
import random
running = 1
humanList = []
randomList = [1,2,3,4]

foodState = ["starving", "hungry", "fed", "full", "stuffed"]

class Human(object):
    def __init__(self, name, age, weight, strength=10, speed=6, hunger=foodState[2], intelligence=10, health=100):
        self.name = name.capitalize()
        self.age = age
        self.weight = weight
        self.strength = strength
        self.speed = speed
        self.hunger = hunger
        self.intelligence = intelligence
        self.health = health


    def printStats(self):
        print(f"You've created a {self.age} year old human has the name {self.name}, and weighs {self.weight} pounds.")


def introduction():
    print("Welcome to the Human Database.")
    print("Here you can create, and destroy humans.")
    print("You can also keep track of them.")
    print("In the next update, they will get hungry, and you'll have to feed them.")
    print("Type 'enter' to move on...")
    answer = input()
    while answer != 'enter':
        print("No...  T Y P E 'enter' silly.")
        answer = input()


def basicChoice():
    choice = input("0: Create Human   1: Kill Human   2: View Humans   3: Train Humans  \n >: ")
    while choice != '0' and choice != '1' and choice != '2' and choice != '3':
        choice = input("0: Create Human   1: Kill Human   2: View Humans   3: Train Humans \n >: ")

    if choice == '0':
        createHuman()
    if choice == '1':
        killHuman()
    if choice == '2':
        viewHumans()
    if choice == '3':
        trainHumans()


def createHuman():
    print("You have chose to create a human.")
    sameName = False
    n = input("What name would you like to give it: ")
    for x in range(len(humanList)):
        while humanList[x].name == n.capitalize():
            print("That name is already in use.")
            n = input("What name would you like to give it: ")
        sameName = False

    while len(n) > 14 and sameName == True:
        for x in range(len(humanList)):
            while humanList[x].name == n.capitalize():
                print("That name is already in use.")
                n = input("What name would you like to give it: ")
            sameName = False

    if sameName == False and len(n) > 14:
        print("Sorry. The name must be less than 15 characters.")
        n = input("What name would you like to give it: ")

    a = input("How old is this human: ")
    while not a.isnumeric():
        print("That is not a number.. try again.")
        a = input("How old is this human: ")

    w = input("How much does this human weigh (lbs): ")
    while not w.isnumeric():
        print("That is either not a number or weighs to much... try again.")
        a = input("How much does this human weight in pounds: ")

    n2 = n
    n2 = Human(n, a, w)
    humanList.append(n2)
    n2.printStats()

def killHuman():

    if len(humanList) == 0:
        print ("You have no humans to kill.")
        return()

    for x in range(len(humanList)):
        print(humanList[x].name)

    deathName = input("Type the name of the human you would like to kill:")

    for x in range(len(humanList)):
        if humanList[x].name != deathName.capitalize():
            print("This human does not exist.")
        else:
            print(f"{humanList[x].name} has been executed.")
            del humanList[x]
            break

def viewHumans():
    if len(humanList) == 0:
        print ("You have no humans to look at yet.")
        return()
    print("These are your humans:")
    for x in range(len(humanList)):
        print(f"Name: {humanList[x].name}")
        print(f"{humanList[x].age} years old")
        print(f"{humanList[x].weight} pounds")
        print(f"They are {humanList[x].hunger}")
        print(f"Health: {humanList[x].strength}")
        print(f"Strength: {humanList[x].strength}")
        print(f"Speed: {humanList[x].speed}")
        print(f"Intelligence: {humanList[x].intelligence}")
        print("-"*30)

def trainHumans():
    traineeHuman = None
    if len(humanList) == 0:
        print ("You have no humans to train.")
        return()

    for x in range(len(humanList)):
        print(f"Your Humans: {humanList[x].name}")
    choice = input("Enter the name of the Human you would like to train: ")


    for x in range(len(humanList)):
        if humanList[x].name != choice.capitalize():
            print("This human does not exist.")
            trainHumans()
        else:
            print(f"How would you like to train {humanList[x].name}?")
            traineeHuman = humanList[x]
            break

    choice = input("0: Train Strength   1: Train Speed   2: Train Intelligence \n >: ")
    while choice != '0' and choice != '1' and choice != '2':
        choice = input("0: Train Strength   1: Train Speed   2: Train Intelligence \n >: ")

    if choice == '0':
        trainStrength(traineeHuman)
    if choice == '1':
        trainSpeed(traineeHuman)
    if choice == '2':
        trainIntelligence(traineeHuman)



def trainStrength(trainee):
    print(trainee)

def trainSpeed(trainee):
    print(trainee)

def trainIntelligence(trainee):
    if hangman.game(trainee):
        increase = random.choice(randomList)
        trainee.intelligence += increase
        print(f"{trainee.name}'s intelligence increased from {trainee.intelligence - increase} to {trainee.intelligence}!\n")
    else:
        print(f"{trainee.name}'s training failed. Try again next time.")

introduction()

while running:

    basicChoice()



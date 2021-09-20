from adventurelib import *
from protagonist import Protagonist
from random import random
import sys
import time


# Pseudo-typing method, can use this instead of say(s) as desired
def type(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random()*0.05)
    print("")

# TODO replace the print statement with a function leading to your adventure
def adv_a():
    print("Adventure A")
    return 1

def adv_b():
    print("Adventure B")
    return 1

def adv_c():
    print("Adventure C")
    return 1

#The Different Advenetures and their names
ADVENTURES = {
    "A": "Adventure A",
    "B": "Adventure B",
    "C": "Adventure C"
    }

#The functions related to each adventure
ADVENTURE_FUNCTIONS = {
    "A": adv_a,
    "B": adv_b,
    "C": adv_c
}

#This is the primary function that you start at when you begin the game
def intro():
    adventures = 1 #we start with only 1 adventure availible
    say("""
    Welcome brave adventurer! You have 3 different adventures to depart on. 
    The adventures must be completed in order! To begin we need to know about you!
    """)
    # we create a character with a name and pronouns
    protag = character_creation()
    say("Let us begin!")
    # let our user pick their adventure
    success = pick_adventure(get_options(adventures))
    adventures += success #if the protag is successful they get another adventure
    while True:
        say("Would you like to go on an adventure?")
        choice = input("(y/n) ")
        if (choice == "y") or (choice == "Y"):
            success = pick_adventure(get_options(adventures))
            if adventures < len(ADVENTURE_FUNCTIONS):
                adventures += success
        else:
            break
    say("It has been great adventuring with you, " + protag.name)

#this function takes in a number of adventures avaible to the user
#returns a dictionary of different adventures they can go on
def get_options(adventures):
    available_adventures = {}
    all_adventures = list(ADVENTURES.keys())[0:adventures]
    for adventure in all_adventures:
        available_adventures[adventure] = ADVENTURES[adventure]
    available_adventures["E"] = "Exit"
    return available_adventures

# this function takes in the adventures our user can go on 
# this function returns 1 on a sucessful adventure and 0  on a failed adventure or exit
def pick_adventure(options):
    say("Pick an adventure below by entering the letter associated")
    # To Do Replace Adventure X with the correct name of the adventure
    print(options)
    while True:
        for key,adventure_name in options.items():
            say(key + ':' + adventure_name)
        choice = input()
        if choice in ADVENTURE_FUNCTIONS.keys():
            return ADVENTURE_FUNCTIONS[choice]()
        elif choice == "E":
            return 0
        else:
            say("That is not an option. Please enter only the letter for the adventure")

# this function take in no variables
# this returns a Protagonist object with a name and pronouns 
def character_creation():
    name = check_name()
    say("You say your name is " + name + " ?\n This is the name of the adventurer of legend!")
    pronouns = check_pronouns()
    protag = Protagonist(name, pronouns)
    return protag

# this function takes in no inputs
# this function returns a list of pronouns e.g.['he', 'him', 'his']
def check_pronouns():
    say("""
    Brave adventurer, what are your pronouns?
    """)
    while True:
        say("(Please format as follows: he/him/his)")
        try:
            pronouns = input("Pronouns: ")
            subject_pronoun, object_pronoun, possessive_pronoun = pronouns.split('/')
            say("Does this sound correct? \'" + subject_pronoun +" has " + possessive_pronoun + " sword with " + object_pronoun + "\'")
            correct = input("(y/n) ")
            if correct == "y":
                return [subject_pronoun, object_pronoun, possessive_pronoun]
            else:
                say("My mistake, let us try again\n")
        except ValueError:
            say("Please make sure your pronouns are seperated by / and that you provide all 3 versions.")

# this function takes in no inputs
# this fucntion returns the name of the protag
def check_name():
    while True:
        say("""
        Brave adventurer what is your name?
        """)
        name = input("Name: ")
        say("Is " + name + " correct? (y/n)")
        correct = input()
        if correct == "y":
            return name
        else:
            say("My mistake, let us try again\n")

if __name__ == '__main__':
    intro()
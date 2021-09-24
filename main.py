from adventurelib import *
from protagonist import Protagonist

from adv_a import adventure_a
from adv_b import start_adv_b
from adv_c import adventure_c


protag = None

# TODO replace the print statement with a function leading to your adventure
def adv_a(protag):
    #adventure_a(protag)
    return "Adventure A"
def adv_b(protag):
    start_adv_b(protag)
    return "Adventure B"
def adv_c(protag):
    #adventure_c(protag)
    return "Adventure C"

#The Different Adventures and their names
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
    adventures = 1 #we start with only 1 adventure available
    say("""
    Welcome brave adventurer! You have 3 different adventures to depart on. 
    The adventures must be completed in order! To begin we need to know about you!
    """)
    # we create a character with a name and pronouns
    global protag
    protag = character_creation()
    say("Let us begin!")
    # let our user pick their adventure
    success = pick_adventure(get_options(protag))

    #if protag is successful add the name of the adventure to your list
    protag.add_adventure(success)

    while True:
        say("Would you like to go on an adventure?")
        choice = input("(y/n) ")
        if (choice == "y") or (choice == "Y"):
            success = pick_adventure(get_options(protag))
            if len(protag.completed_adventures) < len(ADVENTURE_FUNCTIONS):

                #if protag is successful add the name of the adventure to your list
 
                protag.add_adventure(success)
        else:
            break
    say("It has been great adventuring with you, " + protag.name)

#this function takes in a number of adventures available to the user
#returns a dictionary of different adventures they can go on
def get_options(protag):

    #check how many adventures the protag has gone on
    adventures = len(protag.completed_adventures) + 1
    available_adventures = {}
    all_adventures = list(ADVENTURES.keys())[0:adventures]
    for adventure in all_adventures:
        available_adventures[adventure] = ADVENTURES[adventure]
    available_adventures["E"] = "Exit"
    return available_adventures

# this function takes in the adventures our user can go on 
# this function returns 1 on a successful adventure and 0  on a failed adventure or exit
def pick_adventure(options):
    say("Pick an adventure below by entering the letter associated")
    # To Do Replace Adventure X with the correct name of the adventure
    while True:
        for key,adventure_name in options.items():
            say(key + ':' + adventure_name)
        choice = input()
        if choice in ADVENTURE_FUNCTIONS.keys():
            return ADVENTURE_FUNCTIONS[choice](protag)
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
    global protag
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
# this function returns the name of the protag
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

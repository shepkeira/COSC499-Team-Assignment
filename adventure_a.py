from adventurelib import *
from protagonist import Protagonist
from random import random
import sys
import time

# Setup
inventory = Bag()
Room.items = Bag()
Room.locked = False
Item.desc = ""
    
# Rooms
current_room = laboratory = Room("""
    Several bright lights are on, revealing a clean but untidy living area. Its sparse and reminds you of a laboratory more than a bedroom.
    You are surrounded by white, metal walls on 7 of 8 sides. The bed is against the South side, and faces a table in the center with 2 chairs.
    A bulkhead is across the table from you on the North side of the room, containing what looks like an electronic door.
    The East wall contains a window. It"s pitch black outside, and you can see stars.
    On the West side is a closet.
""")
laboratory.how_fire = False # Event: fire
omelette = Item("omelette", "food") # Omolette does not start in laboratory, it only appears later
laboratory.items = Bag()

hallway = laboratory.north = Room("""
    Sirens are blazing, and lights are flashing. You know its only a matter of time before the person from earlier sees you.
    Taking a quick survey of your surroundings, you are first taken aback by the floor-to-ceiling windows along this hallway.
    They give a wide angle view of the entirely pitch-black sky. Such a wide angle in fact that you realize you can't see any ground.
    Just the black night sky. Black with the exception of the distant stars, and one other thing.
    You forget about your current circumstance for a minute as you approach the glass awestruck. A blue and green sphere sits prominently 
    at the left side of your field of view.
    You are in shock. You have no idea how any of what you are experiencing can be real or possible in any way.
    Shaken back into reality by the blaring sirens you realize there is somehow a more pressing matter.
    In front of you (North) lies the hallway which ends in a left-hand bend about 50 feet in from of you.
    Behind you is the room you came out of. You now notice a sign next to the door labelled "Laboratory"
    To your left is the wall-mounted computer you saw earlier.
""")
hallway.locked = True
hallway.stranger = False
hallway.event_see_stranger = False # Event: see stranger

closet = laboratory.west = Room("""
Hanging in the closet is a white jumpsuit, identical to the one you are wearing.
""")
coat_hanger = Item("coat hanger", "hanger")
coat_hanger.desc = "A hanger made out of a maleable, and electronically conductive piece of metal."
extra_suit = Item("extra jumpsuit", "jumpsuit", "suit", "white jumpsuit")
extra_suit.desc = "An extra jumpsuit, just like the one you are wearing"
closet.items = Bag({coat_hanger, extra_suit})

common_room = hallway.west = Room("""
        You round the corner carefully, tip-toeing despite the blaring sirens.
        Peaking around the corner, you find yourself in some sort of common area. There is a kitchen to your right, booth seating, a TV, and other amenities.
        You enter the room from the East, facing West. Southwardly, to your left, is another hallway. It is labelled 'Quarters.' To the North is another
        bulhead with many more warnings, labelled "Airlock". 
""")

quarters_hall = common_room.south = Room("This is a bad idea")

# Start of the game! This is the entrypoint from main.py
def adventure_a():
    say("Adventure A: Asunta II")
    
    # Commenting out sleeps to speed up debugging
    # time.sleep(1)
    print("You wake up in an unfamiliar room with a hazy mind, and no idea how you got here.")
    # time.sleep(1)

    look()
    start()
    # TODO Figure out how to return to menu
    return

# Main game functions, in mostly chronological order
@when("window")
@when("look out window")
@when("look at window")
@when("approach window")
def look_lab_window():
    global current_room
    if current_room == laboratory:
        say("Its pitch black out. You see stars all around.")
    else:
        say("There is no window")

@when("closet")
@when("look in closet")
@when("look at closet")
@when("open closet")
@when("enter closet")
@when("exit closet")
def enter_closet():
    global current_room
    if current_room == laboratory:
        room = current_room.exit("west")
        current_room = room
        look()

@when("leave closet")
@when("close closet")
def leave_closet():
    global current_room
    if current_room == closet:
        room = current_room.exit("east")
        current_room = room
        say("You are back in the laboratory.")
        if hallway.stranger is False:
            # Special event: see stranger
            see_stranger()
    else:
        say("You are not in the closet, you are in %s." % current_room)

def see_stranger():
    say("""
 In the corner of your eye you see a figure in the doorway. They're on the other side of door, but as soon as you turn they duck to the side.
 Your vision is still hazy so you don't get a good look. You can still see them through the window in the door.
    """)
    hallway.event_see_stranger = True
    hallway.stranger = True # Stranger is in hallway; user can go north or look at door to progress

@when("look at figure")
@when("look at door")
@when("look through door")
@when("approach door")
@when("move towards door")
@when("walk towards door")
@when("walk to door")
@when("go to door")
@when("look at door")
@when("look at figure")
@when("go to door")
def look_through_door():
    if current_room == laboratory and hallway.stranger is True:
        say("""
        Looking through the glass on the door you see the figure using a wall-mounted computer console in the hallway. They"re typing
        notes below a picture of what looks like your room. Their face is that of someone who is desparate, and nearly defeated.
        His gaze meets yours. He smiles slightly and presses a button on the keyboard. A voice echos in your room, taking you by shock.
        "So you"re still with us." The figure spoke rhetorically.
        He folds the keyboard into the wall and takes off at a stroll North down the hallway.
    
        You are startled by a whirring behind you. A machine is steaming and buzzing on the table in the middle of the room. Out pops 
        what looks to you like an omelette.
        """)
        laboratory.items.add(omelette)
        hallway.stranger = False
    else:
        say("There's nothing to see")

@when("eat omelette")
@when("eat food")
@when("eat")
def eat_omelette(): # Note that omelettes will be the only food in this adventure, so don't worry that this isn't generic
    obj = inventory.take("omelette")
    if not obj:
        say("You don't have any food in your inventory")
    else:
        say("""
        A taste brings back a memory of college, eating cartonned eggs on your illegal hotplate in your dorm room.
        "Why was it that we weren't supposed to have hotplates in our rooms in college?" You ponder, taking in the sensations on your senses.
        An idea sparks in your head. Fire!
        You look up and sure enough there is a little white dome on the ceiling. Blinking red once every 15 seconds.
        Surely they wouldn't keep you locked in here if a fire broke out right? Someone would at least have to come in to help put it out.
        You decide that if they wanted you dead, you probably would be already.
        Hastily moving on from that last thought, you think about what you could use to start a fire. Perhaps an electrical fire.
        """)
        laboratory.how_fire = True # Next progression is event: fire

@when("put clothes hanger in food machine")
@when("put hanger in food machine")
@when("put hanger in machine")
@when("use clothes hanger on food machine")
@when("use hanger on food machine")
@when("use hanger on machine")
@when("use coat hanger on food machine")
@when("start fire with clothes hanger and food machine")
def fire():
    # To start the fire, the coathanger needs to be in the player's inventory
    if inventory.find("coat hanger") and laboratory.how_fire is True:
        say("""
            Sparks fly in all directions. You cover your eyes and take a step back in recoil.
            Between the lights" flickering you see flames and a plume of smoke rise right underneath the blinking white dome on the ceiling.
            Barely a second later, alarms are blairing, and red lights are flashing in the hallway.
            Your heart sinks for a moment thinking that this was a failure, that you might die in this room.
            Just then, the door to the hallway robotically slides open.
        """)
        hallway.locked = False
        set_context("fire")
    elif inventory.find(coat_hanger):
        say("Come up with a reason to start a fire first.")
    elif laboratory.how_fire is True:
        say("You don't have a coat hanger in your inventory.")

@when("run", context="fire")
@when("north", context="fire")
@when("go through door", context="fire")
@when("run through door", context="fire")
def fire_door():
    global current_room
    if current_room == laboratory:
        say("Without hesitation you run out into the hallway")
        current_room = laboratory.exit("north")
        look()

@when("look", context="fire")
def fire_look():
    global current_room
    if current_room == hallway:
        say("""
            In front of you (North) lies the hallway which ends in a left-hand bend about 50 feet in from of you.
            Behind you is the room you came out of. You now notice a sign next to the door labelled "Laboratory"
            To your left is the wall-mounted computer you saw earlier.
            """)
    elif current_room == laboratory:
        say("Sirens are blaring and the door to the hallway is now open")

@when("go down hallway", context="fire")
@when("walk down hallway", context="fire")
@when("proceed down hallway")
@when("go north", context="fire")
@when("keep going", context="fire")
def round_corner():
    if current_room == hallway:
        go("west")
        say("Suddenly you hear footsteps pounding down the hallway from the South.")
        set_context("danger")

@when("go south", context="danger")
@when("run to quarters", context="danger")
@when("quarter", context="danger")
@when("south", context="danger")
def run_into_stranger():
    say("""
    In a confused panic, you run directly towards where you heard the footsteps coming from.
    You meet the stranger head-on, and for a second you both stop to stare at each-other. He is a tall, scraggly-bearded man 
    wearing a blue jumpsuit similar to the one that you woke up in. His panic turns to confusion, then quickly to focus.
    He walks towards you feigning confidence. You stand in shock as he pulls a black stick from behind his back.
    At this point you turn to try to run, but a tremendous shock fills your body and before you hit the ground you black out.
    """)
    end_game()

def end_game():
    say("""
    Again you awake, but this time even more than before it feels like a dream.
    You are floating, not able to move any part of your body, and your vision little more than a fuzzy haze.
    It can be discerned that you have been shoved into an extremely tight suit, but you aren't standing or laying down.
    Glass fogs in front of your face and as it clears your vision does too. Its the same scene as from the window in the hallway.
    Earth is sitting however many thousands of miles away, as magnificent as it is confusing.
    You're slowly spinning, and as you make a half rotation you begin to make out another figure. Its a space-station.
    The one you were just jettisoned from. Inscribed on the side in red paint is "Asunta II."
    """)
    return


# Common Functions
@when("north", direction="north")
@when("south", direction="south")
@when("east", direction="east")
@when("west", direction="west")
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room.locked:
        say("The door is locked")
    # Special event: See stranger
    if room == laboratory and current_room == closet and hallway.event_see_stranger is False:
        see_stranger()
    # Going North from lab after seeing stranger event
    elif room:
        current_room = room
        say("You go %s." % direction)
        look()


@when("take THING")
@when("pick up THING")
@when("grab THING")
def take(thing):
    obj = current_room.items.take(thing)
    if obj:
        say("You pick up the %s." % obj)
        inventory.add(obj)
    else:
        say("There is no %s here." % thing)


@when("drop THING")
@when("discard THING")
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say("You do not have a %s." % thing)
    else:
        say("You drop the %s." % obj)
        current_room.items.add(obj)

@when("inspect THING")
def inspect(thing):
    obj = inventory.find(thing)
    if not obj:
        say("You do not have a %s. Try taking it." % thing)
    elif obj.desc == "":
        say("It's a %s..." % thing)
    else:
        say(obj.desc)

@when("look")
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say("A %s is here." % i)


@when("inventory")
@when("show inventory")
@when("what am i carrying")
def show_inventory():
    say("You have:")
    for thing in inventory:
        say(thing)

# Comedic functions
@when("leave")
def leave():
    say("If only it were that easy")

# For debugging. Start adventure from this file without having to enter from main.py
# adventure_a()

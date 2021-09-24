from adventurelib import *
from dynamic_type import type, default_type
from colors import colors
import time


home = Room("""
You are in your townhouse.
""")

current_room = home
type_speed = 0.001


@when("exit")
def exit_game():
    raise Exception


# @when("location")
# def get_location():
#     say(current_room)


def start_adv_b(p):
    global protag
    protag = p
    type("Adventure B: Barren Wastes\n", 0.1)
    time.sleep(1)
    say("""You wake up on a chilly December morning. You don't bother getting out of bed for some time.\n""")
    print("\n")
    time.sleep(4)
    say("""It is your first day back on the job market after all.\n""")
    print("\n")
    time.sleep(4)
    say("""You shuffle down the stairs and into the kitchen.""")
    time.sleep(2)
    print("\n")
    type("‘Of course, the coffee maker has to need a water refill,’", 0.1)
    print("\n")
    say("""You grumble in your mind. Your mind wanders as you fill the carafe.\n""")
    print("\n")
    time.sleep(6)
    say("""How many years had to given to your work?\n""")
    print("\n")
    time.sleep(3)
    say("""How many promotions had you been passed over for?\n""")
    print("\n")
    time.sleep(3)
    say("""How many times had you helped others with their work and stayed late for no pay?\n""")
    print("\n")
    time.sleep(3)
    say("""All just for a pink slip.""")
    print("\n")
    time.sleep(5)
    say("""You are startled at the sound of the neighbor’s dog barking and spill water 
    down your front. Cursing and deciding the brisk air might knock some sense into your 
    foggy brain, you walk out your front door to get the morning paper off the porch. 
    It’s frigid out.\n""")
    print("\n")
    time.sleep(6)
    say("""As you grab it, a car pulls up, parks directly in front of your house, 
    and honks its horn once. You try to see if you can recognize the driver, 
    but you can’t see well enough from here.\n""")
    print("\n")
    say("""(Player options: “go back inside”(1A) “approach the car”(1B))""")
    try:
        start()
    except Exception:
        return
    return "Finished Adventure B"


@when("go back inside")
@when("go back")
@when("inside")
def ignore_car():
    say("""You scoff to yourself.""")
    print("\n")
    time.sleep(1)
    type("What a weirdo. Well I don’t care if he’s a missionary or a salesman or what, I’ve got better things to do.\n", 0.1)
    time.sleep(1)
    phone_call()


@when("approach the car")
@when("approach")
def investigate_car():
    say("""You decide it must be someone who knows you, perhaps a former college student who heard about your job falling through. 
    You approach the car with confidence at first, but, the closer you get to the passenger 
    side window, the more you realize that you… \n""")
    print("\n")
    time.sleep(7)
    type("Really can’t see who is in the driver’s seat…\n", 0.2)
    print("\n")
    time.sleep(3)
    say("""The shadow in the car is definitely watching you. You are so unnerved you turn and run back into your porch.\n""")
    print("\n")
    time.sleep(3)
    say("""You stop at your front door to look back one more time at the car.\n""")
    print("\n")
    time.sleep(3)
    say("""The driver hasn’t moved an inch.\n""")
    print("\n")
    time.sleep(3)
    phone_call()


def phone_call():
    say("""Ring ring ring ring banana phone""")

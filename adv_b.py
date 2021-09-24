from adventurelib import *
from dynamic_type import type, default_type
from colors import colors
import time


scene1 = Room("""""")
scene2 = Room("""""")
scene3 = Room("""""")
scene4 = Room("""""")
scene5 = Room("""""")
current_scene = scene1
type_speed = 0.001


@when("exit")
def exit_game():
    raise Exception


def bad_context():
    say("""You can't do that here.""")


# 1
def start_adv_b(p):
    global protag
    protag = p
    type("Adventure B: Barren Wastes\n", 0.1)
    # time.sleep(1)
    # say("""You wake up on a chilly December morning. You don't bother getting out of bed for some time.\n""")
    # print("\n")
    # time.sleep(4)
    # say("""It is your first day back on the job market after all.\n""")
    # print("\n")
    # time.sleep(4)
    # say("""You shuffle down the stairs and into the kitchen.""")
    # time.sleep(2)
    # print("\n")
    # type("‘Of course, the coffee maker has to need a water refill’", 0.1)
    # time.sleep(0.5)
    # print("\n")
    # say("""You grumble in your mind. Your mind wanders as you fill the carafe.\n""")
    # print("\n")
    # time.sleep(6)
    # say("""How many years had to be given to your work?\n""")
    # print("\n")
    # time.sleep(3)
    # say("""How many promotions had you been passed over for?\n""")
    # print("\n")
    # time.sleep(3)
    # say("""How many times had you helped others with their work and stayed late for no pay?\n""")
    # print("\n")
    # time.sleep(3)
    # say("""All just for a pink slip.""")
    # print("\n")
    # time.sleep(5)
    # say("""You are startled at the sound of the neighbor’s dog barking and spill water
    # down your front. Cursing and deciding the brisk air might knock some sense into your
    # foggy brain, you walk out your front door to get the morning paper off the porch.
    # It’s frigid out.\n""")
    # print("\n")
    # time.sleep(6)
    # say("""As you grab it, a car pulls up, parks directly in front of your house,
    # and honks its horn once. You try to see if you can recognize the driver,
    # but you can’t see well enough from here.\n""")
    # print("\n")
    print("1")
    # 1A & 1B
    say(colors.UNDERLINE +
        """(Player options: “go back inside” | “approach the car”)""" + colors.ENDC)
    try:
        start(help=False)
    except Exception:
        return
    return "Finished Adventure B"


# 1A
@when("go back inside")
def ignore_car():
    global current_scene
    if current_scene is not scene1:
        bad_context()
        return
    # say("""You scoff to yourself.""")
    # print("\n")
    # time.sleep(1)
    # type("‘What a weirdo. Well I don’t care if he’s a missionary or a salesman or what, I’ve got better things to do.’\n", 0.1)
    # time.sleep(1)
    print("1A")
    # 2
    phone_call()


# 1B
@when("approach the car")
def investigate_car():
    global current_scene
    if current_scene is not scene1:
        bad_context()
        return
    # say("""You decide it must be someone who knows you, perhaps a former college student who heard about your job falling through.
    # You approach the car with confidence at first, but, the closer you get to the passenger
    # side window, the more you realize that you… \n""")
    # print("\n")
    # time.sleep(7)
    # type("Really can’t see who is in the driver’s seat…\n", 0.2)
    # print("\n")
    # time.sleep(3)
    # say("""The shadow in the car is definitely watching you. You are so unnerved you turn and run back onto your porch.\n""")
    # print("\n")
    # time.sleep(3)
    # say("""You stop at your front door to look back one more time at the car.\n""")
    # print("\n")
    # time.sleep(3)
    # say("""The driver hasn’t moved an inch.\n""")
    # print("\n")
    # time.sleep(3)
    print("1B")
    # 2
    phone_call()


# 2
def phone_call():
    global current_scene
    current_scene = scene2
    # say("""With the driver’s eyes on you, you walk back inside his house, lock his front door, and shut all your first floor blinds.""")
    # print("\n")
    # time.sleep(5)
    # type("‘They’ll go away eventually if they haven't already. Hmph.’", 0.1)
    # print("\n")
    # time.sleep(3)
    # say("""You place the morning paper on you coffee table and suddenly-""")
    # print("\n")
    # time.sleep(2)
    # say("""The phone rings. There is no ID for the number.""")
    # print("\n")
    # time.sleep(3)
    # say("""You answer.""")
    # print("\n")
    # time.sleep(2)
    # type("‘Hello?’", 0.1)
    # print("\n")
    # time.sleep(5)
    # say("""Nothing but soft static replies. """)
    # print("\n")
    say("2")
    # 2A & #2B
    say(colors.UNDERLINE +
        """(Player options: “repeat the greeting” | “hang up”)""" + colors.ENDC)


# 2A
@when("repeat the greeting")
def repeat_greeting():
    global current_scene
    if current_scene is not scene2:
        bad_context()
        return
    say("2A")
    # 3A & #3B
    say(colors.UNDERLINE +
        """(Player options: “ask what they mean” | “end conversation”)""" + colors.ENDC)


# 2B
@when("hang up")
def hang_up():
    global current_scene
    if current_scene is not scene2:
        bad_context()
        return
    say("2B")
    # 3C & 3D
    say(colors.UNDERLINE +
        """(Player options: “investigate the package” | “call the police”)""" + colors.ENDC)


# 3A
@when("ask what they mean")
def ask_what_they_mean():
    global current_scene
    current_scene = scene3
    if current_scene is not scene3:
        bad_context()
        return
    say("3A")
    # 4A & 4B
    say(colors.UNDERLINE +
        """(Player options: “what kind of opportunity” | “is this paid”)""" + colors.ENDC)


# 3B
@when("end conversation")
def end_conversation():
    global current_scene
    current_scene = scene3
    if current_scene is not scene3:
        bad_context()
        return
    say("3B")
    # 4C & 4D
    say(colors.UNDERLINE +
        """(Player options: “investigate the noise” | “call the neighbors”)""" + colors.ENDC)


# 3C
@when("investigate the package")
def investigate_package():
    global current_scene
    current_scene = scene3
    if current_scene is not scene3:
        bad_context()
        return
    say("3C")
    # 4E & 4F
    say(colors.UNDERLINE +
        """(Player options: “call number” | “cook the meat”)""" + colors.ENDC)


# 3D
@when("call the police")
def call_police():
    global current_scene
    current_scene = scene3
    if current_scene is not scene3:
        bad_context()
        return
    say("3D")
    # 4G & 4H
    say(colors.UNDERLINE +
        """(Player options: “grab knife” | “do not grab knife”)""" + colors.ENDC)


# 4A
@when("what kind of opportunity")
def an_opportunity():
    global current_scene
    current_scene = scene4
    if current_scene is not scene4:
        bad_context()
        return
    say("4A")
    # 5A
    meeting_willingly()


# 4B
@when("is this paid")
def an_opportunity():
    global current_scene
    current_scene = scene4
    if current_scene is not scene4:
        bad_context()
        return
    say("4B")
    # 5A
    meeting_willingly()


# 4C
@when("investigate the noise")
def investigate_noise():
    global current_scene
    current_scene = scene4
    if current_scene is not scene4:
        bad_context()
        return
    say("4C")
    # 5B
    meeting_unwillingly()


# 4D
@when("call the neighbors")
def call_neighbors():
    global current_scene
    current_scene = scene4
    if current_scene is not scene4:
        bad_context()
        return
    say("4D")
    # 5B
    meeting_unwillingly()


# 4E
@when("call number")
def call_number():
    global current_scene
    current_scene = scene4
    if current_scene is not scene4:
        bad_context()
        return
    say("4E")
    # 5A
    meeting_willingly()


# 4F
@when("cook the meat")
def eat_meat():
    global current_scene
    current_scene = scene4
    if current_scene is not scene4:
        bad_context()
        return
    say("4F")
    # 5A
    meeting_willingly()


# 4G
@when("grab knife")
def grab_knife():
    global current_scene
    current_scene = scene4
    if current_scene is not scene4:
        bad_context()
        return
    say("4G")
    # 5B
    meeting_unwillingly()


# 4H
@when("do not grab knife")
def dont_grab_knife():
    global current_scene
    current_scene = scene4
    if current_scene is not scene4:
        bad_context()
        return
    say("4H")
    # 5B
    meeting_unwillingly()


# 5A
def meeting_willingly():
    global current_scene
    current_scene = scene5
    if current_scene is not scene5:
        bad_context()
        return
    say("5A")
    say(colors.UNDERLINE +
        """(Player options: “join” | “decline” | “redacted”)""" + colors.ENDC)


# 5B
def meeting_unwillingly():
    global current_scene
    current_scene = scene5
    if current_scene is not scene5:
        bad_context()
        return
    say("5B")
    say(colors.UNDERLINE +
        """(Player options: “join” | “decline” | “redacted”)""" + colors.ENDC)


# 6A
@when("join")
def red_ending():
    say("Red Ending")
    exit_game()


# 6B
@when("decline")
def black_ending():
    say("Black Ending")
    exit_game()


# 6C
@when("redacted")
def true_ending():
    say("True Ending")
    exit_game()

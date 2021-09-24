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
    type("‘Of course, the coffee maker has to need a water refill’", 0.1)
    time.sleep(0.5)
    print("\n")
    say("""You grumble in your mind. Your mind wanders as you fill the carafe.\n""")
    print("\n")
    time.sleep(6)
    say("""How many years had to be given to your work?\n""")
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
    say("""You scoff to yourself.""")
    print("\n")
    time.sleep(1)
    type("‘What a weirdo. Well I don’t care if he’s a missionary or a salesman or what, I’ve got better things to do.’\n", 0.1)
    time.sleep(1)
    # 2
    phone_call()


# 1B
@when("approach the car")
def investigate_car():
    global current_scene
    if current_scene is not scene1:
        bad_context()
        return
    say("""You decide it must be someone who knows you, perhaps a former college student who heard about your job falling through.
    You approach the car with confidence at first, but, the closer you get to the passenger
    side window, the more you realize that you… \n""")
    print("\n")
    time.sleep(7)
    type("Really can’t see who is in the driver’s seat…\n", 0.2)
    print("\n")
    time.sleep(3)
    say("""The shadow in the car is definitely watching you. You are so unnerved you turn and run back onto your porch.\n""")
    print("\n")
    time.sleep(3)
    say("""You stop at your front door to look back one more time at the car.\n""")
    print("\n")
    time.sleep(3)
    say("""The driver hasn’t moved an inch.\n""")
    print("\n")
    time.sleep(3)
    # 2
    phone_call()


# 2
def phone_call():
    global current_scene
    current_scene = scene2
    say("""With the driver’s eyes on you, you walk back inside his house, lock his front door, and shut all your first floor blinds.""")
    print("\n")
    time.sleep(5)
    type("‘They’ll go away eventually if they haven't already. Hmph.’", 0.1)
    print("\n")
    time.sleep(3)
    say("""You place the morning paper on you coffee table and suddenly-""")
    print("\n")
    time.sleep(2)
    say("""The phone rings. There is no ID for the number.""")
    print("\n")
    time.sleep(3)
    say("""You answer.""")
    print("\n")
    time.sleep(2)
    type("‘Hello?’", 0.1)
    print("\n")
    time.sleep(5)
    say("""Nothing but soft static replies. """)
    print("\n")
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
    say("""You repeat yourself, more uncertain.""")
    print("\n")
    time.sleep(2)
    type("‘. . . Hello?’", 0.1)
    print("\n")
    time.sleep(3)
    say("""Another moment of silence, then- """)
    print("\n")
    time.sleep(2)
    type(colors.YELLOW + "“Hello " + protag.name +
         ". I’m calling because I have a very important opportunity that I think you will be quite interested in.”" + colors.ENDC, 0.1)
    print("\n")
    time.sleep(2)
    say("""You can’t place what sort of person this voice is coming from. """)
    print("\n")
    time.sleep(3)
    type("‘This is odd, I haven’t even responded to any help wanted ads yet.’", 0.1)
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
    say("""You sigh.""")
    print("\n")
    time.sleep(1)
    type("‘These kids and their prank calls.’", 0.1)
    print("\n")
    time.sleep(2)
    say("""You hang up on the silent caller, and not a second later-""")
    print("\n")
    time.sleep(2)
    type(colors.BOLD + "THUMP" + colors.ENDC, 0.2)
    print("\n")
    time.sleep(0.5)
    type(colors.BOLD + "THUMP" + colors.ENDC, 0.2)
    print("\n")
    time.sleep(0.5)
    type(colors.BOLD + "THUMP" + colors.ENDC, 0.2)
    print("\n")
    time.sleep(2)
    type("‘That came from the back deck . . . ’", 0.1)
    print("\n")
    time.sleep(2)
    say("""You make your way through the kitchen to the backdoor. You open it a crack and look out into the backyard.""")
    print("\n")
    time.sleep(4)
    say("""No one is there, but - """)
    print("\n")
    time.sleep(2)
    type("‘What’s that?’", 0.1)
    print("\n")
    time.sleep(2)
    say("""A brown cardboard box with too much duct tape sealing it up sat in front of the door, with scrawling red marker on the top reading only: """)
    print("\n")
    time.sleep(6)
    say("‘To " + protag.name + "’ ")
    print("\n")
    time.sleep(4)
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
    type("“What do you mean? What kind of opportunity?”", 0.1)
    print("\n")
    time.sleep(1)
    say("""Better to not look a gift horse in the mouth. """)
    print("\n")
    time.sleep(2)
    type(colors.YELLOW + "“I’m terribly sorry to hear about your previous employers… not recognizing your talents, let’s say . . .”" + colors.ENDC, 0.1)
    print("\n")
    time.sleep(1)
    say("""The voice responds, smooth as silk. """)
    print("\n")
    time.sleep(2)
    type("“I-I’m sorry?”", 0.1)
    print("\n")
    time.sleep(1)
    say("""Your mind is racing.""")
    print("\n")
    time.sleep(2)
    type("‘How did they hear about-’", 0.05)
    print("\n")
    time.sleep(3)
    type(colors.YELLOW + "“Fortunately for you " + protag.name +
         ", we’ve been following some of your previous work. Personally I especially liked your article about the dangers of children being more and more exposed to technology. We’d love someone with your viewpoint on our team.”" + colors.ENDC, 0.1)
    print("\n")
    time.sleep(2)
    type("“Your team?”", 0.1)
    print("\n")
    time.sleep(2)
    type(colors.YELLOW + "“Trust me " + protag.name + ", this is an incredibly valuable opportunity. I’m sure when you’re given the full scope of it, you won’t be able to turn it down. If you’re interested, please meet with our group interviewers at 6 pm this evening at 333 Bedford Street.”" + colors.ENDC, 0.1)
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
    say("""You decides to hang up.""")
    print("\n")
    time.sleep(2)
    type("‘It must be a scam, has to be. I didn’t even give any businesses my resume yet. Speaking of which…’", 0.1)
    print("\n")
    time.sleep(1)
    say("""You glance at your laptop sitting on the couch and give a long-suffering sigh.""")
    print("\n")
    time.sleep(2)
    type(colors.YELLOW + "“Hello " + protag.name +
         ". I’m calling because I have a very important opportunity that I think you will be quite interested in.”" + colors.ENDC, 0.1)
    print("\n")
    time.sleep(2)
    say("""You can’t place what sort of person this voice is coming from. """)
    print("\n")
    time.sleep(3)
    type("‘This is odd, I haven’t even responded to any help wanted ads yet.’", 0.1)
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
    say("""You open the back door fully, scan the backyard one more time, then cautiously pick up the package. It feels heavy, and it sounded like something inside squished. """)
    print("\n")
    time.sleep(5)
    say("""You cringe but bring the package inside anyway. You set it on the kitchen counter. """)
    print("\n")
    time.sleep(3)
    say("""‘Should I call the police about this?.... Nah it’s definitely just another prank, it’s just like the phone call.’ With newfound determination, you grab a kitchen knife and work at cutting through the numerous layers of duct tape. You gingerly open the box and peer inside. """)
    print("\n")
    time.sleep(8)
    say("""The box contained a red-stained, newspaper-wrapped mass, with pamphlets thrown haphazardly on top like giant confetti. You take one from the box. It’s titled: “Humanity Versus Tech: We Will Not Be Slaves to AI!”. You take out another, this one titled: “The Devil is in the Details: How Tech Works to Brainwash Our Children!”. You open this one. Your article on the dangers of tech exposure on children, the one he wrote just before he was fired, is cited in it. There are multiple copies of each pamphlet. You fishe out the newspaper lump from the mess of paper. On the newspaper is written “For the winter”. You peel back the paper. """)
    print("\n")
    time.sleep(12)
    say("""It’s a hunk of meat. You can’t tell what animal it’s come from. """)
    print("\n")
    time.sleep(3)
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
    say("""You close the door and quickly lock it. ‘What the hell is going on? First the weirdo on the phone and now this? I bet some idiot dropped off drugs to the wrong " + protag.name + ". . .’ """)
    print("\n")
    time.sleep(5)
    say("""You pull out your phone and try to call the non-emergency line. Your phone won’t place the call. """)
    print("\n")
    time.sleep(3)
    type("‘What the hell?!", 0.06)
    print("\n")
    time.sleep(3)
    say("""You look at your screen- no internet, no signal. """)
    print("\n")
    time.sleep(3)
    type(colors.BOLD + "THUMP" + colors.ENDC, 0.2)
    print("\n")
    time.sleep(0.5)
    type(colors.BOLD + "THUMP" + colors.ENDC, 0.2)
    print("\n")
    time.sleep(0.5)
    type(colors.BOLD + "THUMP" + colors.ENDC, 0.2)
    print("\n")
    time.sleep(2)
    say("""Someone is knocking on the front door. """)
    print("\n")
    time.sleep(2)
    say("""You swallow, take a deep breath, and start walking through the kitchen as quietly as you can. You glance at the knife block on the counter. """)
    print("\n")
    time.sleep(5)
    say("""‘Maybe I should take one with me?’""")
    print("\n")
    time.sleep(5)
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
    type("“Wait, what kind of opportunity is this?”", 0.1)
    print("\n")
    time.sleep(2)
    type(colors.YELLOW + "“We are an organization who believes firmly that humanity is, to put it bluntly, taking technology and running with it before we fully understand the effects that such rapid tech growth cause on human minds, particularly the minds of the young and impressionable. We are dedicated to preventing a future where technology is valued above what humanity has to give, and we believe you’re someone who understands that.” " + colors.ENDC, 0.1)
    print("\n")
    time.sleep(2)
    type("“Oh, so you’re a civil rights organization? I’m sorry but I’m really only looking for paid-“", 0.1)
    print("\n")
    time.sleep(0.5)
    type(colors.YELLOW + "“This is a paid position. Not to mention it comes with, let’s just say, unimaginable benefits.”" + colors.ENDC, 0.1)
    print("\n")
    time.sleep(2)
    say("""You think about it for a moment. """)
    print("\n")
    time.sleep(2)
    type("“333 Bedford Street you said? I’ll be there.”", 0.1)
    print("\n")
    time.sleep(2)
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
    say("""You suddenly remember your sense of professionalism when you realize you’re being offered an interview. """)
    print("\n")
    time.sleep(2)
    type("“Is, um, is this a paid position?”", 0.1)
    print("\n")
    time.sleep(2)
    type(colors.YELLOW + "“Of course! If you accept the position you’ll be offered at least matching pay from your former place of employment, however . . . I’ve been told you to relay to you that money is no object here, if you catch my meaning.” " + colors.ENDC, 0.1)
    print("\n")
    time.sleep(2)
    say("""You grin - you certainly do.""")
    print("\n")
    time.sleep(2)
    type("“You said 6 pm right? At 333 Bedford Street?”", 0.1)
    print("\n")
    time.sleep(2)
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
    say("""You can smell the smoke before you’re even in the kitchen doorway. """)
    print("\n")
    time.sleep(2)
    say("""Half your kitchen is ablaze, the backdoor wide open. Someone had done this on purpose. """)
    print("\n")
    time.sleep(3)
    say("""You run back into the living room. Pulling out your phone you frantically dial 911. Your phone wont place the call-""")
    print("\n")
    time.sleep(3)
    say("""You feel something hit the back of his head and the world goes dark. """)
    print("\n")
    time.sleep(2)
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
    type("‘What if someone is in the kitchen?’", 0.1)
    print("\n")
    time.sleep(2)
    say("""Slowly, quietly, you get up from the couch and tiptoe into the opposite corner of the living room, towards your desk. You crouch behind it and try to call your next door neighbor Ms. Patty. """)
    print("\n")
    time.sleep(2)
    say("""Your phone won’t place the call. You examine the screen.""")
    print("\n")
    time.sleep(2)
    type("‘No wifi or data signal? What’s going on . . . ’ ", 0.1)
    print("\n")
    time.sleep(2)
    say("""You suddenly realize that something smells off. ‘Is that smoke?!’ """)
    print("\n")
    time.sleep(2)
    say("""You feel something heavy hit the back of his head, and everything fades away. """)
    print("\n")
    time.sleep(2)
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
    say("""You shudder and shift your gaze back to the dozens of pamphlets in the box. You realize they all have the same phone number on them. """)
    print("\n")
    time.sleep(4)
    type("‘Well, I guess I may as well at least find out who the hell is behind this… or maybe what the hell this meat is from . . .”", 0.1)
    print("\n")
    time.sleep(2)
    say("""You dial the number on his phone. It takes a bit, but someone picks up on the other end. You wait for them to say something, but they don’t. """)
    print("\n")
    time.sleep(4)
    type("“Um…. Hi? Look I’m calling about the box someone left on my back deck-“ ", 0.1)
    print("\n")
    time.sleep(0.5)
    type(colors.YELLOW + "“" + protag.name +
         ", we’ve been expecting your call.”" + colors.ENDC, 0.1)
    print("\n")
    time.sleep(2)
    type("“How do you know my name? Where did you get my address?” ", 0.1)
    print("\n")
    time.sleep(2)
    type(colors.YELLOW + "“The package is an invitation" +
         protag.name + "” " + colors.ENDC, 0.1)
    print("\n")
    time.sleep(2)
    type("“Invitation? But where did you get this meat-“", 0.1)
    print("\n")
    time.sleep(0.5)
    type(colors.YELLOW + "“It’s a custom of our organization. I apologize if it’s lead to any confusion. We like to symbolically provide for our people as much as we like to actually provide for them- like the old ways, before everything was emails and phone calls and zoom meetings.”" + colors.ENDC, 0.1)
    print("\n")
    time.sleep(2)
    say("""The voice talks over you, their tone turning terse at the mention of the technology. You sigh.""")
    print("\n")
    time.sleep(2)
    type("“I hear you- it’s like their pushing for everything we touch to be some kind of smart device. Where’s the peace supposed to be when your fridge can advertise to you?”", 0.1)
    print("\n")
    time.sleep(2)
    type(colors.YELLOW + "“I’m very glad to hear you seem to share our organization’s beliefs, Mr. Jones. Shall I give you the interview details?” " + colors.ENDC, 0.1)
    print("\n")
    time.sleep(2)
    type("“Yes, that will be fine, thank you.", 0.1)
    print("\n")
    time.sleep(2)
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

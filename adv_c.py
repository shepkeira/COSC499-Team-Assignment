from adventurelib import *
from protagonist import Protagonist
from pynput.keyboard import Key, Controller


Home = Room("""Welcome to the game of Three Identical Stranger. This game is based on the true story. 
     Hello brave worrior. You are getting adopted by your new adaptive family at 6 months. 
     You will pick your family from the following 3 choice (upper middle class, middle class or working class).""")

RoomDavid = Room("""Brave Worrior, Your name is David. 
      Although you have been adopted by a loving family who owns grocery store, 
      you have been in and out of pychiatric hospitals.
    Now you are 19 years old and here is a big news!! You are one of the triplets! 
    You have two other identical brothers.""")

RooomRobert = Room("""Brave Worrior, Your name is Robert.
  You have been apopted by upper middle class. Your father is a doctor but he was busy with his work while you growing up. 
  Now you are 19 years old. You have got some mental health issue and got into some troubles. 
  But here is the big news!. You are one of the triplests! You have two other identical brothers""")

RoomEdward = Room("""Brave Worrior, Your name is Edward.You got adopted by a middle class school teacher. You and your fathers's characteristics were not good match. You have been sturuggling with psychiatric problem and family conflict.
  Now you are 19 years old. You have got some mental health issue and got into troubles . 
  But here is the big news!. You are one of the triplests! You have two other identical brothers""")

RoomTriplets = Room("""You are having the best time of your life. You decided to open the resuaurant called Triplets with your brothers, Robert and Edward!
  The triplets are getting so much media attention it is like you are semi-celebs and you made a million in the first year!! As time goes on, they strugggled with their differences and Robert decided to leave the restauraurant several years after.""")

print("To start the game, please type begin")

@when("begin")
def begin():
# initial message to explain the game.
  current_room = Home
  print(current_room)
  say("""Please pick one of the following family  
  a: Working class or b: Middle class or c: Upper middle class)""")
  #return "End of Adventure C: Three Identical Triplets"

@when('a')
@when('working')
@when("working class")
    # if player typed "working class" or "A" lead him to David()
def David():
  current_room = RoomDavid
  say(current_room)
  option() 

@when('b')
@when('middle')
@when ("middle class") 
    # else if player typed "middle class" or "B" lead him to Edward()
def Edward():
  current_room = RoomEdward
  say(current_room)
  option()

@when('c')
@when ('upper')
@when('upper class')
    # else if player typed "upper middle class" or "C" lead him to Robert()
def Robert():
    current_room =RoomRobert
    say(current_room)
    option()  

def option():
    say( """Would like to go meet them ?\n 
    Option 1 : Type 'yes' to go meet them them right away.\n
    Option 2 : Type 'no' to stay all by yourself""")

@when ("no") 
    # the player chose the dead end, call game_over() function with the "reason"
def no():
    reason = """You choose NO, but here is unacceptalble truth for you. 
     You were used for the part of unethical human experimentation. 
     Evil research have separeted the high risk triplets on purpose and they were studying you while all of you were struggling with your metnal illness.
     Now your brothers and all the adaptive family want to get together and go talk to the researchers.
     There was no option for you to avoid meeting them."""
    game_over(reason)

@when("yes") 
def triplets():
    current_room = RoomTriplets
    print(current_room)
    say("""A couple years after, you got the worst news of your life, one of the triplets has commited suicide.\n 
    Who do you think it was?\n
    david, edward or robert""")
    
    @when("david")
    def david():
        #the player made wrong choice, call game_over() function with the "reason"
        reason = """Sorry brave warrior, your guess is wrong. David was adapted by working class family but with loving family he had developed the best way to cope with his mental illness out of the triplets. Since Rober left the restaurant and even more after Edwards death David and Robert drifted apart\n"""
        game_over(reason)
    
    @when("edward")
        # the player won the game by guessing correct
    def edward():
        reason = """Yes, it was Edward. Edward was adapted by the middle class family but he and his father was just not good match. 
        Edward sturuggle most growing up without necessary support. 
        He was exhibited increasing sigh of bipoar disorder This research was most cruel to him \n
        Bravo!! You made the correct guess and won the game\n"""
        game_over(reason)
    
    @when ("robert") 
    def robert():
     reason = """Sorry brave warrior, you did not win this time. 
     Rober was adapted by upper-middle class family whose father was doctor. 
     They has money but not quority time for him. , 
     but he has established carrie as a lawyer.\n"""
     game_over(reason)

def game_over(reason):
    #say("""Sorry brave warrior, your guess is wrong. David was adapted by working class family but with loving family he had developed the best way to cope with his mental illness out of the triplets.print Since Rober left the restaurant and even more after Edwards death David and Robert drifted apart""")
    say(reason)
    print("This game was based on the documetary field \'Three Identical Strangers\' \n \"Three Identical Strangers\". wikipedia, https://en.wikipedia.org/wiki/Three_Identical_Strangers. Accessed 17 Septempber 2021.")
    print("Study was never publised and all documents were placed with Yale University and restricted until 2065. \nThere were at least six sets of twin/ triplet who got separated in this study and at lease three of the separated sibling apparently committed suicide.")
    print("Type 'exit' to exit the game, Thank you!!!")

@when("exit")
def exit():
 say("exiting the game")
 keyboard = Controller()
 keyboard.press(Key.ctrl)
 keyboard.press('z')
 keyboard.release(Key.ctrl)
 keyboard.release('z')
 keyboard.press(Key.enter) 

start()

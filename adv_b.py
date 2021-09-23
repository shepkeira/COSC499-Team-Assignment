from adventurelib import *
from dynamic_type import type, default_type
from colors import colors
from pynput.keyboard import Key, Controller


home = Room("""
You are in your townhouse on Main Street, Anytown Canada. 
""")

current_room = home
protag = None
type_speed = 0.001


@when("exit")
def exit_game():
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('z')
    keyboard.release(Key.ctrl)
    keyboard.release('z')
    keyboard.press(Key.enter)


@when("location")
def get_location():
    say(current_room)


def start_adv_b(protag):
    protag = protag
    say("""You wake up, fix coffee, then
    go outside to get the paper on your porch. 
    While you're outside, a parked car you don't recognize 
    honks at you incessantly. Do you ignore it and leave, or do you investigate?""")
    start()
    return "Finished Adventure B"


@when("leave")
def ignore_car():
    say("""Not wanting any unwanted attention, you briskly
    go back inside.""")


@when("investigate")
def investigate_car():
    say("""Intrigued but unnerved, you make your way over to the 
    parked vehicle.""")

import time
import random


def print_pause(msg):
    print(msg)
    time.sleep(2)


def field(danger, items):
    print_pause("Enter 1 to Knock on the door of the house")
    print_pause("Enter 2 to peer into the cave")
    print_pause("What would you like to do?")
    choice(danger, items)


def door(danger, items):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the \n"
                "door opens and out steps a {danger}.")
    print_pause(f" Eep! This is the {danger}'s house!")
    print_pause(f"The {danger} attacks you!")
    if "the magical Sword of Ogoroth!" in items:
        fight_or_run = input("Would you like to (1) fight or (2) run away?")
        if fight_or_run == '1':
            print_pause(f"As the {danger} moves to attack, \n"
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in \n"
                        "your hand as you brace yourself for the attack.")
            print_pause(f"But the {danger} takes one look at \n"
                        "your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {danger}. /n"
                        "You are victorious!")
            play_again(danger, items)
        elif fight_or_run == '2':
            print_pause("You run back into the field. Luckily, \n"
                        "you don't seem to have been followed")
            field(danger, items)
        else:
            print_pause("You have made no choice")
    else:
        print_pause("You feel a bit under-prepared for this,\n"
                    " what with only having a tiny dagger.")
        fight_or_run = input("Would you like to (1) fight or (2) run away?")
        if fight_or_run == '1':
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {danger}.")
            print_pause("You have been defeated!")
            play_again(danger, items)
        elif fight_or_run == '2':
            print_pause("You run back into the field. Luckily, \n"
                        "you don't seem to have been followed")
            field(danger, items)
        else:
            print_pause("You have made no choice")


def play_again(danger, items):
    play_again_choice = input("Would you like to play again? (y/n)")
    if play_again_choice == 'y':
        print_pause("Excellent! Restarting the game . . .")
        items = []
        intro(danger, items)
    elif play_again_choice == 'n':
        print_pause("Thanks for playing, see you next time. Goodbye ...")
        exit()
    else:
        print_pause("You have made no choice")


def cave(danger, items):
    if "the magical Sword of Ogoroth!" in items:
        print_pause("you've been here before, and gotten \n"
                    "all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field(danger, items)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old \n"
                    "dagger and take the sword with you.")
        print_pause("You walk back out to the field.")
        items.append("the magical Sword of Ogoroth!")
        field(danger, items)


def choice(danger, items):
    choice = input("Please enter 1 or 2 \n")
    if choice == '1':
        door(danger, items)
    elif choice == '2':
        cave(danger, items)
    else:
        print_pause("Please enter a valid input")
        field(danger, items)


def intro(danger, items):
    print_pause("You find yourself standing in an open field, \n"
                "filled with grass and yellow wildflowers")
    print_pause(f"Rumor has it that a {danger} is somewhere \n"
                "around here, and has been terrifying the nearby village")
    print_pause("In your hand you hold your trusty \n"
                "(but not very effective) dagger.")
    print_pause("In front of you are two passageways")
    print_pause("Which way do you want to go?")
    field(danger, items)


def start_adventure():
    danger = random.choice(["wicked fairie", "dragon", "troll", "pirate"])
    items = []
    intro(danger, items)
    field(danger, items)
    choice(danger, items)


start_adventure()

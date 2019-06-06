import time
import random

bag = ['old_dagger']
weapon = ['Servel Sword', 'Machine Gun',
          'Golden Sword', 'Advance Alien Wappen']
creature = ['Gorggon', 'Out Law\'s', 'Dragon', 'Alien']
place = []
weapon = random.choice(weapon)
creature = random.choice(creature)


def print_pause(String):
    print(String)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.", )
    print_pause("Rumor has it that a " + creature + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your Right is a dark cave")
    print_pause("In your hand you hold your trusty "
                "(but not Very effective dagger)")
    print_pause("\n Enter 1 to knock on the door of House."
                "\n Enter 2 to peer into the cave."
                "\n What would you like to do?")


def house():
    # Things happen to the player in house are define here.
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock, "
                    "when the door opens and out steps a " + creature)
        print_pause("This is the  " + creature + " house!")
        if 'old_dagger' in bag:
            print_pause("you feel a bit under-prepared for this, "
                        "what with only having a tiny dagger.")
            ans = ''
            while ans != '1' and ans != '2':
                ans = input("Would you like to (1) Filght or (2) run away?")
                if ans == '1':
                    print_pause("You fought Bravely, But what could have "
                                "you done with just a tiny dagger.")
                    print_pause("Nasty " + creature + ", Killed you. :( ")
                    print_pause("\n \n \t YOU LOSS")
                    play_again()

                if ans == '2':
                    feild()
                    print_pause("\n \n \t YOU LOSS")
                    play_again()

        elif weapon in bag:
            print_pause("The " + creature + " attack you \n")
            ans = ''
            while ans != '1' and ans != '2':
                ans = input("Would you like to (1) Filght or (2) run away?\n")
                if ans == '1':
                    print_pause("As the " + creature + " moves to attack, "
                                "you unsheath your new" + weapon)
                    print_pause("The " + weapon + " of " + creature +
                                " shines brightly in your hand as you brace "
                                "yourself for the attack.")
                    print_pause("But the " + creature + " takes one look at "
                                "your shiny new toy and runs")
                    print_pause("You have rid the town of the " + creature +
                                ". YOU ARE VICTORIOUS!")
                    print_pause("\n \n \t YOU WON")
                    play_again()

                if ans == '2':
                    feild()
                    print_pause("\n \n \t YOU LOSS")
                    play_again()

        else:
            print_pause("\n \n \t YOU LOSS")
            play_again()


def cave():
    # Things happen to the player in cave are define here.
    if 'cave' not in place:
        print_pause("\n You Peer cautiously into the cave")
        print_pause("It truns out to be only a very small cave.")
        print_pause("You have found the " + weapon + " of " + creature)
        print_pause("You Discard your silly old dagger and "
                    "take the " + weapon + " with you")
        bag.remove('old_dagger')
        bag.append(weapon)
        print_pause("You walk Back out to the field")
        place.append('cave')
    else:
        print_pause("\n You Peer cautiously into the cave.")
        print_pause("You've been here befor, and gotton all the good stuff."
                    " it's just an empty cave now.")
        print_pause("You walk Back out to the feild.")


def feild():
    # Things happen to the player in feild are define here.
    print_pause("YOu run into the field. Luckily, "
                "you don't seem to have been followd")
    print_pause("You Run off cowardly to the feild. SHAAAMMM ")


def adventure_game():
    ans = ''
    if 'started' not in place:
        intro()
        place.append('started')
        while ans != '1' and ans != '2':
            ans = input("\n (Please enter 1 or 2.)\n")
            if ans == '1':
                house()
            if ans == '2':
                cave()
                adventure_game()
    else:

        while ans != '1' and ans != '2':
            ans = input("\n (Please enter 1 or 2.)\n")
            if ans == '1':
                house()
            if ans == '2':
                cave()
                adventure_game()


def play_again():
    ans = input("\nWOULD YOU LIKE TO PLAY AGAIN !!!\n"
                "If YESS Enter 1\n"
                "If NO Entert 2\n")
    if ans == '1':
        adventure_game()
    elif ans == '2':
        print_pause("It Was Really NICE :) to play with YOU\n"
                    "\n"
                    " SEE YOU SOON")
    else:
        print_pause("Please Enter 1 or 2")
        play_again()

adventure_game()

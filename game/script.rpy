# Declare characters used by this game.

define c = Character("Cheese") 

image cheese test = "cheese_test.png"
image bg mcdonalds kitchen = Transform("bg_mcdonalds_kitchen.jpg", zoom=2.0, xalign=0.5, yalign=0.5)

# The game starts here.

label start:

    scene bg mcdonalds kitchen

    show cheese test at truecenter

    c " lick my wrapper, peasant! "

    menu:

        " That's cheeseburher! ":
            jump ending
        
        " Oh hell yeah! ":
            jump ending


label ending:
    c " End of demo. "

    # This ends the game.

    return

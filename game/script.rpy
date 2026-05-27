# Declare characters used by this game.

define c = Character("Cheese") 


# The game starts here.

label start:

    scene bg room

    show cheese test at truecenter

    c " lick my wrapper, peasant! "

    menu:

        " What? ":
            jump ending
        
        " Oh hell yeah! ":
            jump ending


label ending:
    c " End of demo. "

    # This ends the game.

    return

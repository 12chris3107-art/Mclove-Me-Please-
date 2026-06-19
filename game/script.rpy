# Definitions for characters, images go here.

define c = Character("Cheese") 

image cheese test = "cheese_test.png"
image bg mcdonalds kitchen = Transform("bg_mcdonalds_kitchen.jpg", zoom=2.0, xalign=0.5, yalign=0.5)

# The game starts here.

label start:
    jump intro
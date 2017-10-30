#Start Screen
print("--------------------")
print("    Welcome to      ")
print("  Of Gods and Men   ")
print("--------------------")
print("                    ")

#Prologue
print("--------------------")
print("------Prologue------")
print("--------------------")

print("Your eyes open and you find yourself in the corner of a cold, damp cell.")
print("You look around and see a small mound of straw, and a ragged looking man in the cell next to you.")
str(input("Do you talk to him? [y/n]: "))

#Talk to Ragged Man
if ['y', 'Y', 'Yes', 'YES', 'yes']:
    print("You crawl over to the bars.")
    str(input("What do you say? [Who Are you?]: "))

    if ["Who are you?"]:
            print("I am the salt in the sea, the dirt on the ground, the leaves on the trees, the wind in the air.")
            str(input("What do you say? [Where am I?] : "))
            if ["Where am I?"]:
                print ("You're on board The Cape Wrath, headed for Brimstone Keep.")

def scene0():

    print("Scene 0: Imagination")

    print("Do you believe in magic?")

    print("1. Yes")

    print("2. No")



    choice = input("Choose 1 or 2: ")

    while choice != "1" and choice != "2":

        choice = input("Please choose 1 or 2: ")



    if choice == "1":

        return scene1()

    elif choice == "2":

        return ending0()
    


def scene1():

    print("Scene 1: The Wardrobe")

    print("You find a mysterious wardrobe. Do you:")

    print("1. Step inside.")

    print("2. Walk away.")



    choice = input("Choose 1 or 2: ")

    while choice != "1" and choice != "2":

        choice = input("Please choose 1 or 2: ")



    if choice == "1":

        return scene2()

    elif choice == "2":

        return ending1()



def scene2():

    print("Scene 2: Narnia")

    print("You’re in a snowy forest (the land of Narnia). A faun invites you to tea. Do you:")

    print("1. Go with him.")

    print("2. Say no and explore.")



    choice = input("Choose 1 or 2: ")

    while choice != "1" and choice != "2":

        choice = input("Please choose 1 or 2: ")



    if choice == "1":

        return scene3()

    elif choice == "2":

        return scene4()



def scene3():

    print("Scene 3: Mr. Tumnus’ House")

    print("He tells you about the White Witch, who makes Narnia always winter but never Christmas. Do you:")

    print("1. Go back and tell your siblings.")

    print("2. Stay and try to stop her.")



    choice = input("Choose 1 or 2: ")

    while choice != "1" and choice != "2":

        choice = input("Please choose 1 or 2: ")



    if choice == "1":

        return scene5()

    elif choice == "2":

        return ending2()



def scene4():

    print("Scene 4: The Witch")

    print("The White Witch offers you some delicious Turkish Delight. Do you:")

    print("1. Eat it.")

    print("2. Refuse and run.")



    choice = input("Choose 1 or 2: ")

    while choice != "1" and choice != "2":

        choice = input("Please choose 1 or 2: ")



    if choice == "1":

        return ending3()

    elif choice == "2":

        return scene6()



def scene5():

    print("Scene 5: Aslan’s Camp")

    print("You meet Aslan, the Great Lion and the leader of an army against the Witch. Do you:")

    print("1. Join the fight.")

    print("2. Stay back and let others fight.")



    choice = input("Choose 1 or 2: ")

    while choice != "1" and choice != "2":

        choice = input("Please choose 1 or 2: ")



    if choice == "1":

        return ending4()

    elif choice == "2":

        return ending5()



def scene6():

    print("Scene 6: Rescue Plan")

    print("You meet the Beavers who want to rescue Edmund, your brother. Do you:")

    print("1. Help them.")

    print("2. Say no, it's too risky.")



    choice = input("Choose 1 or 2: ")

    while choice != "1" and choice != "2":

        choice = input("Please choose 1 or 2: ")



    if choice == "1":

        return ending6()

    elif choice == "2":

        return ending7()



# Endings

def ending0():
    print("Ending: No Adventure")

    print("You do't believe in magic. You'll never know what Narnia was like.")



def ending1():

    print("Ending: No Adventure")

    print("You walk away. You'll never know what Narnia was like.")



def ending2():

    print("Ending: Frozen")

    print("The Witch turns you to stone. Game over.")



def ending3():

    print("Ending: Betrayed")

    print("The sweet was cursed. You fall under the Witch’s control.")



def ending4():

    print("Ending: Hero")

    print("You help defeat the Witch and become a ruler of Narnia.")



def ending5():

    print("Ending: Forgotten")

    print("Narnia is saved, but no one remembers you.")



def ending6():

    print("Ending: Edmund Saved")

    print("You helped save your brother and Narnia!")



def ending7():

    print("Ending: Witch Wins")

    print("Without your help, the Witch wins.")



# Story Starts

# Entry point: welcome the player and begin the story 

def story():

    print("Welcome to The Chronicles of Narnia Adventure Game!")

    scene0()


# Start the game by calling the story function

story()


# credit to C.S. Lewis, author of "The Chronicles of Narnia: the Lion, the Witch, and the Wardrobe"

 

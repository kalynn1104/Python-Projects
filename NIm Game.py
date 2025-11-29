# Introduction & Rules

print("Hello! Welcome to the Nim Game (2-Player & 3-Pile) !")

print("Please read the rules before you start:")

print("1. 3 piles each start with a random number of chips.")

print("2. You may only pick from ONE pile per turn.")

print("3. Take as many chips as you want. BUT you need to take at least one chip & you can't take more than what is on the pile.")

print("4. Take turns. The goal is to NOT pick up the last chip. Good luck!")



# Ask for players' names

playerOne = input("Enter Player 1's name: ")

playerTwo = input("Enter Player 2's name: ")



# Manage turns (player one starts)
turn = playerOne



# Randomize the number of chips in each pile

import random
pileOne = random.randint(3, 12)

import random
pileTwo = random.randint(3, 12)

import random
pileThree = random.randint(3, 12)



# Repeat while at least one pile has chips

while pileOne + pileTwo + pileThree > 0:



    # Display who's turn it is & the number of chips from each pile

    print("It is", turn, "'s turn.")

    print("Here are the number of chips from each pile:")

    print("Pile 1: ", pileOne)

    print("Pile 2: ", pileTwo)

    print("Pile 3: ", pileThree)



    # Ask to choose a pile

    selectedPile = 0     # Start with an invalid number

    while selectedPile != 1 and selectedPile != 2 and selectedPile != 3:

        selectedPile = int(input("Enter 1 to take chips from the first pile, 2 for the second, and 3 for the last: "))



        if selectedPile != 1 and selectedPile != 2 and selectedPile != 3:

            print("There is no such pile. Try again.")

            selectedPile = 0

        elif selectedPile == 1 and pileOne == 0:

            print("Pile 1 is empty. Choose another pile.")

            selectedPile = 0

        elif selectedPile == 2 and pileTwo == 0:

            print("Pile 2 is empty. Choose another pile.")

            selectedPile = 0

        elif selectedPile == 3 and pileThree == 0:

            print("Pile 3 is empty. Choose another pile.")

            selectedPile = 0



    # Ask for the number of chips they would like to take from the selected pile

    if selectedPile == 1:

        maxTake = pileOne

    elif selectedPile == 2:

        maxTake = pileTwo

    else:

        maxTake = pileThree


    # Keep asking until the player enters a number between 1 and maxTake 

    takenChips = 0     # Start with an invalid number

    while takenChips < 1 or takenChips > maxTake:

        takenChips = int(input("How many chips would you like to take from the pile? "))



        if takenChips < 1:

            print("You must take at least 1 chip.")

        elif takenChips > maxTake:

            print("You can't take more than", maxTake, "chip(s).")



    # Subtract the number of chips taken from the selected pile

    if selectedPile == 1:

        pileOne = pileOne - takenChips

    elif selectedPile == 2:

        pileTwo = pileTwo - takenChips

    else:

        pileThree = pileThree - takenChips



    # Check for a winner

    if pileOne + pileTwo + pileThree == 0:

        print("All piles are empty!")

        # The OTHER player wins

        if turn == playerOne:

            print("Congradulations,", playerTwo, ", you win the game!")

        elif turn == playerTwo:

            print("Congradulations,", playerOne, ", you win the game!")



    else:

        # Switch turns

        if turn == playerOne:

            turn = playerTwo

        else:

            turn = playerOne

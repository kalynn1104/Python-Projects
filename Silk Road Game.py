import random  

print("Welcome to 'Life as a Silk Road Merchant!'")
print("You're a merchant traveling the Silk Road from 900 to 1600 CE.")
print("Try to trade, stay alive, and learn some cool history along the way!\n")

# Starting stats
gold = 100
health = 100
inventory = {"Silk": 0, "Spices": 0, "Porcelain": 0}

# Trade goods with historical info: [buy cost, sell profit, historical fact]
goods = {
        "Silk": [10, 30, "Silk was super valuable in Europe for clothes and luxury items."],
        "Spices": [5, 20, "Spices like pepper and cinnamon were prized for cooking and preserving food."],
        "Porcelain": [8, 25, "Porcelain from China was beautiful, durable, and highly sought in Europe."]
        }

# Cities along the Silk Road with historical info
cities = [
        ["Chang'an (China)", "Chang'an was the eastern final stop of the Silk Road. Merchants from China started their journey here, trading silk, porcelain, and tea."],
        ["Samarkand (Central Asia)", "Samarkand was a major trade hub where East met West. Markets were full of goods from China, India, and Persia."],
        ["Baghdad (Middle East)", "Baghdad was a center of trade, learning, and technology. Merchants exchanged goods and ideas, helping spread Islam and science."],
        ["Constantinople (Europe)", "Constantinople was a key European trade city where goods from Asia were sold to Western merchants. It connected Asia and Europe economically and culturally."]
        ]

# Function to trade goods
def trade():
    global gold, inventory
    print("\nYou are in a market.")
    print("You have", gold, "gold coins.")
    print("Goods available to buy with historical info:")
    for item in goods:
        print(f"{item} - Cost: {goods[item][0]} gold/unit, Profit: {goods[item][1]} gold/unit")
        print("Historical fact:", goods[item][2])
    
    choice = input("Which good do you want to buy? (Silk/Spices/Porcelain/None) ")
    if choice in goods:
        amount = input("How many units do you want to buy? ")
        if amount.isdigit() and int(amount) > 0:
            amount = int(amount)
            cost = amount * goods[choice][0]
            if cost <= gold:
                inventory[choice] += amount
                gold -= cost
                print(f"You bought {amount} units of {choice}.")
            else:
                print("Not enough gold! Maybe next time.")
        else:
            print("Hmm, that's not a valid amount. You buy nothing.")
    else:
        print("You chose not to buy anything.")

# Function to simulate traveling
def travel(city):
    global health, gold
    print("\nTraveling to", city[0])
    print("Historical info:", city[1])
    
    # Ask if player wants to rest
    rest = input("Do you want to rest before traveling? (yes/no) ")
    if rest == "yes":
        health += 10
        print("You feel refreshed! Health +10.")

    # Random events
    event = random.randint(1,6)
    if event == 1:
        print("Uh-oh! Bandits attack! Merchants on the Silk Road often faced thieves.")
        loss = min(gold, random.randint(10, 30))
        gold -= loss
        health -= 10
        print(f"You lose {loss} gold and 10 health points. Ouch!")
    elif event == 2:
        print("Sandstorm! Desert and mountain routes were super dangerous.")
        health -= 15
        print("You lose 15 health points... stay hydrated next time!")
    elif event == 3:
        print("You feel sick from travel. Rest helps a bit.")
        health -= 10
        print("You lose 10 health points.")
    elif event == 4:
        print("You attend a local festival! Learn about religion, art, and tech. Cool!")
        # No health or gold lost
    elif event == 5:
        print("A helpful caravan shares food and advice. You feel better.")
        health += 5
        print("You gain 5 health points.")
    else:
        print("The journey is smooth. You safely continue your trade route.")

# Function to sell goods with optional partial selling
def sell():
    global gold, inventory
    print("\nArriving at the city market to sell goods.")
    for item in inventory:
        if inventory[item] > 0:
            print(f"You have {inventory[item]} units of {item}.")
            sell_choice = input(f"How many units of {item} do you want to sell? (0 to skip) ")
            if sell_choice.isdigit():
                sell_amount = int(sell_choice)
                if 0 <= sell_amount <= inventory[item]:

                    profit = sell_amount * goods[item][1]
                    gold += profit
                    inventory[item] -= sell_amount
                    print(f"You sold {sell_amount} units of {item} for {profit} gold.")
                else:
                    print(f"Invalid number. You sell none of your {item}.")
            else:
                print("Invalid input. You sell nothing.")
        else:
            print("You have no", item, "to sell.")
    print("Your total gold now:", gold)

def main():
    for city in cities:
        trade()
        travel(city)
        sell()
        print("Your health is:", health)
        if health <= 0:
            print("You did not survive the Silk Road journey. Game over!")
            break
        else:
            print("\nCongratulations! You completed your Silk Road journey!")
            print("Final gold:", gold)
            print("You learned about trade, cultural exchange, and dangers merchants faced along the Silk Road.")

    # Extra Historical Notes with personal touch
    print("\nExtra Historical Notes:")
    print("- Merchants traveled thousands of miles across deserts, mountains, and rivers.")
    print("- Trade goods included silk, spices, porcelain, precious metals, and even ideas.")
    print("- Merchants helped spread religions like Buddhism, Islam, and Christianity.")
    print("- Knowledge of technology, art, and science was exchanged along the Silk Road.")
    print("- Cities like Samarkand and Baghdad became famous centers of commerce and learning.")
    print("- The Silk Road connected East and West, shaping world history in the early modern era.")
    print("- Imagine risking bandits, sandstorms, and illness just to make a profit. Brave or crazy?")

main()

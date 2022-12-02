def shop(money: int, inventory: dict[str, int]):
    temp: str = ''
    while not temp == 'q':
        print(f"Welcome to the shop, you have {money} coins.")

        print("Your items:", end = ' ')
        for i in inventory:
            print(f"{inventory[i]} {i}", end = ' ')
        print()

        print("Shop items: Potions for 5$, Food for 3$, Keys for 10$")

        temp = input("Press p to buy a potion, f for food, k for keys, and q to quit (case sensitive)\n")

        if temp == 'p':
            if money >= 5:
                money -= 5
                try:
                    inventory["Potions"] += 1
                except:
                    inventory["Potions"] = 1
            else:
                print("You got a Potion!")
        elif temp == 'f':
            if money >= 3:
                money -= 3
                try:
                    inventory["Food"] += 1
                except:
                    inventory["Food"] = 1
            else:
                print("You got a Food!")
        elif temp == 'k':
            if money >= 10:
                money -= 10
                try:
                    inventory["Keys"] += 1
                except:
                    inventory["Keys"] = 1
            else:
                print("You got a Key!")
        elif temp == 'q':
            print("Goodbye!")
        else:
            print("Invalid Input!")
        
        print()

    return money

shop(100, {})
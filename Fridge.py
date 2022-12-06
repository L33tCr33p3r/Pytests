class Fridge:
    def __init__(self, number_of_items: int, door_open: bool, is_running: bool):
        self.number_of_items: int = number_of_items;
        self.door_open: bool = door_open
        self.is_running: bool = is_running
    
    def print(self):
        print(f"number of items: {self.number_of_items}, door is open: {self.door_open}, is running: {self.is_running}")
        if (self.is_running):
            print("go catch it, it'll get away")
    
    def open_door(self):
        self.door_open = True

    def close_door(self):
        self.door_open = False

    def fill(self, items: int):
        if self.door_open:
            self.number_of_items += items
        else:
            print("Open the door first!")
    
    def make_dinner(self):
        if self.number_of_items >= 10:
            self.number_of_items -= 10
        else:
            print("Restock your fridge!")

fridge = Fridge(0, False, False)

fridge.print()

fridge.make_dinner()

fridge.print()

fridge.fill(10)

fridge.print()

fridge.open_door()

fridge.print()

fridge.fill(10)

fridge.print()

fridge.close_door()

fridge.print()

fridge.make_dinner()

fridge.print()

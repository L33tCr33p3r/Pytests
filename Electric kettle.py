class electrickettle:
    def __init__(self):
        self.is_on = False
        self.is_hot = False
        self.water = 0.0
    def fill(self):
        self.water = 20.0
    def pour_cup(self):
        if self.water >= 5:
            self.water -= 5
            

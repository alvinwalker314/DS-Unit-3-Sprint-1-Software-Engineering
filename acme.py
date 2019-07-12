import random

class Product():
    
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
        
        
    def stealability(self):
        steal_ratio = self.price / self.weight
        if steal_ratio < 0.5:
            return "Not so stealable..."
        elif steal_ratio >= 0.5 & steal_ratio < 1:
            return "Kinda stealable"
        else:
            return "Very stealable!"
    
    def explode(self):
        explode_chance = self.flammability * self.weight
        if explode_chance < 10:
            return "...fizz"
        elif explode_chance > 10 & explode_chance < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

class BoxingGlove(Product):
    
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        super().__init__(name, price, weight, flammability, identifier)
    
    def explode(self):
        return "...it's a glove."
    
    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 & self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
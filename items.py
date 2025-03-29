# Super class for all foods
class Food:
    def __init__(self, can_chop, can_blend, location, name, image):
        self.can_chop = can_chop
        self.can_blend = can_blend
        self.location = location #1 is for Fridge, 2 is for pantry
        self.name = name
        self.image = image
        self.chopped = False
        self.blended = False

#Mixing items together
class Mixture:
    def __init__(self, items):
        self.items = items

# All types of food items
# Fruits
class Fruit(Food):
    def __init__(self, name, image):
        super().__init__(True, True, 1, name, image) #1 for fridge

# Vegetables
class Veggie(Food):
    def __init__(self, name, image):
        super().__init__(True, True, 1, name, image)  # 1 for fridge
        self.washed = False

    def wash(self):
        self.washed = True

# Oils, like avocado oil, olive oil, etc.
class Oils(Food):
    def __init__(self, name, image):
        super().__init__(False, True, 2, name, image)  # 2 for pantry
        self.heated = False

    def heat(self):
        self.heated = True

# Milk, juice, wine, etc.
class Liquid(Food):
    def __init__(self, name, image):
        super().__init__(False, True, 1, name, image)  # 1 for fridge
        self.heated = False

    def heat(self):
        self.heated = True

# Salt, pepper, spices
class Seasonings(Food):
    def __init__(self, name, image):
        super().__init__(False, True, 2, name, image)  # 2 for pantry

# Wheat, rice, oats, barley, Rye
class Grains(Food):
    def __init__(self, name, image):
        super().__init__(False, True, 2, name, image)  # 2 for pantry
        self.washed = False

    def wash(self):
        self.washed = True

# Please consider Milk to be a liquid. So this is Eggs, Butter, Yogurt, Cheese
class Dairy(Food):
    def __init__(self, name, image):
        super().__init__(True, True, 1, name, image)  # 1 for fridge

# Meats, like chicken, beef, pork, and mutton
class Meat(Food):
    def __init__(self):
        super().__init__(True, False, 1, name, image)  # 1 for fridge
        self.seasoned = False
        self.seasoning = []

    def seasoned(self, seasoning):
        self.seasoned = True
        self.seasoning = seasoning
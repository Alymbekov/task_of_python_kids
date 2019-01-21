class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print("Дышит")
    def move(self):
        print("Двигается")
    def eat_food(self):
        print("Ест")

class Mammals(Animals):
    def feed_young_with_milk(self):
        print("Кормит детенышей молоком")

class Giraffes(Mammals):
    
    #def __init__(self,spots):
        #self.giraffe_spots = spots
    
    def eat_leaves_from_trees(self):
        print("Ест листья")
    
    def left_foot_forward(self):
        print("Левая нога вперед")
    
    def right_foot_back(self):
        print("Правая нога назад")
    
    def right_foot_forward(self):
        print("Правая нога вперед")
    
    def left_foot_back(self):
        print("Левая нога назад")
    
    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
""" reginald = Giraffes()
harold = Giraffes()
reginald.move()
harold.eat_leaves_from_trees() """
""" ozwald = Giraffes(100)
print(ozwald.giraffe_spots) """

reginald = Giraffes()
reginald.dance()
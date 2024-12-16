import random

class Tiger:
    def __init__(self):
        self.state = 'hunt prey'
        self.lucky_attack = 0.5
        self.cord_x = 0
        self.cord_y = 0

    def random_stroll(self):
        self.cord_x += random.choice([-1, 0, 1])
        self.cord_y += random.choice([-1, 0, 1])
        self.cord_x = max(0, min(self.cord_x, 4))
        self.cord_y = max(0, min(self.cord_y, 4))

    def ubdate_state(self):
        if self.state == 'hunt prey':
            print('tiger is hunting')
            self.random_stroll()



class Rabbits:
    def __init__(self, x, y):
        self.is_find = False
        self.cord_x = x
        self.cord_y = y


    def to_find(self):
        self.is_find = True

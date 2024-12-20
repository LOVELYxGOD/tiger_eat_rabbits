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

    def is_near_rabbit(self, rabbit):
        return abs(self.cord_x - rabbit.cord_x) <= 1 and abs(self.cord_y - rabbit.cord_y) <= 1


class Rabbit:
    def __init__(self, x, y):
        self.is_find = False
        self.cord_x = x
        self.cord_y = y


    def to_find(self):
        self.is_find = True

def show_field(tiger, rabbits):
    field = []
    for i in range(5):
        row = []
        for i in range(5):
            row.append('.')
        field.append(row)

    field[tiger.cord_x][tiger.cord_y] = 'T'
    for rabbit in rabbits:
        if not rabbit.is_find:
            field[rabbit.cord_x][rabbit.cord_y] = 'R'

    for row in field:
        print(" ".join(row))
    print()
def init():
    tiger = Tiger()
    rabbit_1 = Rabbit(random.randint(1, 4), random.randint(1, 4))
    rabbit_2 = Rabbit(random.randint(1, 4), random.randint(1, 4))
    rabbits = [rabbit_1, rabbit_2]

    show_field(tiger, rabbits)

init()

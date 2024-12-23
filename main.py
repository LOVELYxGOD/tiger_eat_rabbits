import random
import os
import time

clear = lambda: os.system('cls')
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

    def update_state(self, rabbits):
        if self.state == 'hunt prey':
            print('tiger is hunting')
            self.random_stroll()
            if any(self.is_near_rabbit(rabbit) for rabbit in rabbits):
                self.state = 'attack'
        elif self.state == 'attack':
            if random.random() < self.lucky_attack:
                print('Tiger hunt rabbit😈')
                for rabbit in rabbits:
                    if self.is_near_rabbit(rabbit):
                        rabbit.to_find()
                self.state = 'Go home'
        elif self.state == 'Go home':
            self.cord_x = 0
            self.cord_y = 0

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

    while tiger.state != 'Go home':
        # os.system('cls' if os.name == 'nt' else 'clear')
        clear()
        print(tiger)

        for rabbit in rabbits:
            print(rabbit)

        show_field(tiger, rabbits)

        tiger.update_state(rabbits)

        time.sleep(1)

    print(tiger)

    for rabbit in rabbits:
        print(rabbit)
    # os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    tiger.update_state(rabbits)


    show_field(tiger, rabbits)

    if tiger.state == 'Go home':
        print('tiger in home')


init()



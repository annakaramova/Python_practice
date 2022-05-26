#
# Write a warships game with field 5x5
import random


class Ship:
    def __init__(self):
        self.is_sunk = False

    def hit(self):
        self.is_sunk = True


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_hit = False
        self.ship = None

    def hit(self):
        self.is_hit = True
        if self.ship:
            self.ship.hit()

    def __str__(self):
        if self.ship and self.ship.is_sunk:
            return '*'
        elif self.is_hit:
            return 'X'
        else:
            return '0'


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for x in range(width):
            self.cells.append([])
            for y in range(height):
                self.cells[x].append(Cell(x, y))

    def __str__(self):
        result = ''
        for row in self.cells:
            for cell in row:
                result += f"{cell} "
            result += '\n'
        return result

    def get_cell(self, x, y):
        return self.cells[x][y]

    def get_cell_by_coordinates(self, coordinates):
        return self.get_cell(coordinates[0], coordinates[1])


class Game:
    def __init__(self):
        self.field = Field(5, 5)
        self.ships = [Ship()]
        self.number_of_tries = 5

    def __str__(self):
        return str(self.field)

    def place_ship(self, ship, coordinates):
        cell = self.field.get_cell_by_coordinates(coordinates)
        if cell.ship:
            raise Exception('Cell is occupied')
        cell.ship = ship

    def shoot(self, coordinates):
        cell = self.field.get_cell_by_coordinates(coordinates)
        cell.hit()
        self.number_of_tries -= 1

    def is_game_over(self):
        if self.number_of_tries == 0:
            return True

        for ship in self.ships:
            if not ship.is_sunk:
                return False
        return True

    def is_win(self):
        for ship in self.ships:
            if not ship.is_sunk:
                return False
        return True

    @staticmethod
    def input_coordinates():
        while True:
            print('Enter coordinates: ', end='')
            coordinates = input().split(',')
            if len(coordinates) != 2:
                print('Wrong coordinates!')
                continue
            try:
                x = int(coordinates[0])
                y = int(coordinates[1])
            except ValueError:
                print('Wrong coordinates!')
                continue
            if x < 0 or x >= 5 or y < 0 or y >= 5:
                print('Wrong coordinates!')
                continue
            return [x, y]

    def play(self):
        self.place_ship(self.ships[0], (random.randint(0, self.field.width), random.randint(0, self.field.height)))

        while not self.is_game_over():
            print(self)
            coordinates = self.input_coordinates()
            try:
                self.shoot(coordinates)
            except Exception as e:
                print(e)

        if self.is_win():
            print('You win!')
        else:
            print('You lose!')


Game().play()

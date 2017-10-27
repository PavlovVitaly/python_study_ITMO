class Ship(object):
    """Корабль"""

    def __init__(self, tp, x=-1, y=-1, rotation=0):
        self.__x = None
        self.__y = None
        self.__rotation = None
        self.field = None

        self.__type = self.__health = tp

        self.update_pos(x, y, rotation)

    def __contains__(self, coord):
        """Перегрузка in"""

        x, y = coord
        x1, y1 = self.first_coord
        x2, y2 = self.last_coord
        return x1 <= x <= x2 and y1 <= y <= y2

    def in_halo(self, x, y):
        x1, y1 = self.first_halo_coord
        x2, y2 = self.last_halo_coord
        return x1 <= x <= x2 and y1 <= y <= y2

    def update_pos(self, x, y, rotation):
        self.__x = x
        self.__y = y
        self.__rotation = rotation

    def attack(self):
        if not self.is_killed():
            self.__health -= 1

    def is_killed(self):
        return not self.__health

    @property
    def type(self):
        return self.__type

    #
    # @type.setter
    # def type(self, tp):
    #     self.__type = tp
    #
    # @type.deleter
    # def type(self):     # del ship.type
    #     del self.__type

    @property
    def first_coord(self):
        return self.__x, self.__y

    @property
    def last_coord(self):
        x, y = self.first_coord
        r = self.__rotation
        i = self.__type - 1
        return x + i * r, y + i * (1 - r)

    @property
    def first_halo_coord(self):
        x, y = self.first_coord
        return x - 1, y - 1

    @property
    def last_halo_coord(self):
        x, y = self.last_coord
        return x + 1, y + 1

    def coords(self):
        """Координаты корабля"""
        x1, y1 = self.first_coord
        x2, y2 = self.last_coord
        return ((x, y)
                for x in range(x1, x2 + 1)
                for y in range(y1, y2 + 1))

    def halo(self):
        """Координаты ореола"""
        x1, y1 = self.first_halo_coord
        x2, y2 = self.last_halo_coord
        return ((x, y)
                for x in range(x1, x2 + 1)
                for y in range(y1, y2 + 1)
                if (x, y) not in self and (x, y) in self.field)


class Field(object):
    """Игровое поле"""

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__ships = []
        self.__shots = {}

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.rows and 0 <= y < self.cols

    @property
    def rows(self):
        return self.rpws

    @property
    def cols(self):
        return self.__cols

    def add_ship(self, ship):
        if not isinstance(ship, Ship):
            return False

        if not self.__check_pos(ship):
            return False

        ship.field = self
        self.__ships.append(ship)

        return True

    def __check_pos(self, ship):
        if ship.first_coord not in self or ship.last_coord not in self:
            return False
        for x, y in ship.coords():
            if self.get_ship_by_point(x, y, include_halo=True):
                return False

        return True

    def get_ship_by_point(self, x, y, include_halo=False):
        for ship in self.__ships:
            if (x, y) in ship:
                return ship
            if include_halo and ship.in_halo(x, y):
                return ship

    @property
    def ships_afloat(self):
        return sum(1 for ship in self.__ships if not ship.is_killed())

    SHOT_MISSED = 0
    SHOT_INJURED = 1
    SHOT_KILLED = 2
    SHOT_HALO = 3

    def attack(self, x, y):
        if (x, y) in self.__shots:
            return

        ship = self.get_ship_by_point(x, y)

        if ship:
            ship.attack()
            state = self.SHOT_KILLED if ship.is_killed() else self.SHOT_INJURED
        else:
            state = self.SHOT_MISSED

        points = {}

        if ship and ship.is_killed():
            for point in ship.coords():
                self.__shots[point] = points[point] = self.SHOT_KILLED

            for point in ship.halo():
                if point not in self.__shots:
                    self.__shots[point] = points[point] = self.SHOT_HALO
        self.__shots[x, y] = points[x, y] = state
        return state, points

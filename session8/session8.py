class Counter:
    def __init__(self, my_id):

        self._items = {}
        self._id = my_id

    def add(self, item_name, amount, price_of_unit):

        if item_name not in self._items:

            self._items[item_name] = {
                'quantity': amount, 'price per unit': price_of_unit}
        else:
            self._items[item_name]['quantity'] += amount

    def remove(self, item_name, amount):
        if item_name not in self._items:
            pass
        elif amount >= self._items[item_name]['quantity']:
            del self._items[item_name]
        else:
            self._items[item_name]['quantity'] -= amount

    def reset(self):

        self._items.clear()

    def get_total(self):
        total_price_of_items = 0
        for item in self._items:
            total_price_of_items += (self._items[item]['quantity']
                                     * self._items[item]['price per unit'])
        return round(total_price_of_items, 2)

    def status(self):

        total_amount_of_items = 0

        for item in self._items:
            total_amount_of_items += self._items[item]['quantity']

        return (f'{self._id} {total_amount_of_items} {self.get_total()}')


cart1 = Counter('C0001')

cart1.add('potato', 2, 3.65)
cart1.add('banana', 15, 1.54)
cart1.remove('banana', 2)


print(cart1.status())


class Sector:
    def __init__(self):
        self.fr = 0
        self.to = 0
        self.rad = 0

    def rotate(self, angle):
        if angle + self.to > 359:
            print('This action is not possible')
        else:
            self.fr += angle
            self.to += angle

    def intersect(self, other):

        if self.fr >= other.fr:
            new_fr = self.fr
        else:
            new_fr = other.fr
        if self.to <= other.to:
            new_to = self.to
        else:
            new_to = other.to
        if self.rad <= other.rad:
            new_rad = self.rad
        else:
            new_rad = other.rad
        new_sector = Sector()
        new_sector.fr = new_fr
        new_sector.to = new_to
        new_sector.rad = new_rad
        return new_sector

    def is_empty(self):
        if self.fr == self.to:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.rad == other.rad and self.fr == other.fr and self.to == other.to:
            return True
        else:
            return False

    def __str__(self):

        return (f'{self.fr} {self.to} {self.rad}')

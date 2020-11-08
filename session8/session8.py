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

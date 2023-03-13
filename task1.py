class Technic:
    PRICE_LIMIT = 10000

    __slots__ = ['title', 'price', 'available', 'price_cat']

    def __init__(self, title, price, available):
        self.title = title
        self.price = price
        self.available = available
        self.price_cat = 'budget' if self.price < self.PRICE_LIMIT else 'expensive'

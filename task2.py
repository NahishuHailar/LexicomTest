"""
Для сравнения строк  title по количеству символов:
- С помощью декоратора len_comparison переопределим методы:
__eq__, __lt__, __le__, __gt__, __ge__
Метод __ne__ не переопределен, интерпретатор инвертирует результат
метода __eq__.
"""
def len_comparison(cls):
    def verify_data(other):
        if not isinstance(other, Technic):
            raise TypeError('Объект для сравнения должен быть Technic')
        return other

    def eq(self, other):
        comparisons_obj = verify_data(other)
        return len(self.title) == len(comparisons_obj.title)

    def lt(self, other):
        comparisons_obj = verify_data(other)
        return len(self.title) < len(comparisons_obj.title)

    def gt(self, other):
        comparisons_obj = verify_data(other)
        return len(self.title) > len(comparisons_obj.title)

    def le(self, other):
        comparisons_obj = verify_data(other)
        return len(self.title) <= len(comparisons_obj.title)

    def ge(self, other):
        comparisons_obj = verify_data(other)
        return len(self.title) >= len(comparisons_obj.title)

    cls.__eq__, cls.__lt__, cls.__le__ = eq, lt, le
    cls.__gt__, cls.__ge__ = gt, ge

    return cls


@len_comparison
class Technic:
    PRICE_LIMIT = 10000

    __slots__ = ['title', 'price', 'available', 'price_cat']

    def __init__(self, title, price, available):
        self.title = title
        self.price = price
        self.available = available
        self.price_cat = 'budget' if self.price < self.PRICE_LIMIT else 'expensive'

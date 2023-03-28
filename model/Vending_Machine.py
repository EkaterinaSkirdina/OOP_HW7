from model.Product import Product


class Vending_Machine:

    def __init__(self):
        all_products = list()
        self._all_products = all_products

    @property
    def all_products(self):
        return self._all_products
    
    @all_products.setter
    def all_products(self, new_all_products):
        self._all_products = new_all_products

    def get_product(self, name, volume):
        for el in self.all_products:
            if el.name == name & el.volume == volume:
                return el
        else:
            return "Не найдено!"

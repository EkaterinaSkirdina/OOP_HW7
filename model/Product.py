class Product:
    
    def __init__(self, name, price, volume):
        self._name = name
        self._price = price
        self._volume = volume

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @name.setter
    def name(self, new_name):
        self._name = new_name
        return self._name

    @price.setter
    def price(self, new_price):
        self._name = new_price
        return self._price
    
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_volume):
        self._volume = new_volume
        return self._volume
    
    def __str__(self) -> str:
        return f"Название: {self.name}, цена: {self.price}, объем: {self.volume}"
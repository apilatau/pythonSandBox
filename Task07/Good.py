import uuid


class Good:

    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.name

    @property
    def price(self):
        return self.price

    @id.setter
    def id(self, value: uuid):
        self.id = value

    @name.setter
    def name(self, value: str):
        self.name = value

    @price.setter
    def price(self, value: float):
        self.price = value

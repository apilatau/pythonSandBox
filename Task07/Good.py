import uuid


class Good:

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @id.setter
    def id(self, value):
        self.__id = value

    @name.setter
    def name(self, value: str):
        self.__name = value

    @price.setter
    def price(self, value: float):
        self.__price = value

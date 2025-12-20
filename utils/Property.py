class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, plot, area, rooms: int, price, address):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Dom {self.rooms} pokojowy o powierzchni {self.area}m². Powierzchnia działki {self.plot}m².\nAdres: {self.address}\nCena: {self.price} zł"


class Flat(Property):
    def __init__(self, floor, area, rooms, price, address):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Mieszkanie {self.rooms} pokojowe na {self.floor} piętrze, o powierzchni {self.area}m².\nAdres: {self.address}\nCena: {self.price}zł."

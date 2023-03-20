class Tire:
    def __init__(self, size, brand):
        self.size = size
        self.brand = brand

    def is_compatible_with_car(self, car):
        return self.size == car.tire_size
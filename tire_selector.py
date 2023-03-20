class TireSelector:
    def __init__(self, tires, cars=None):
        self.tires = tires
        self.cars = cars or []

    def set_cars(self, cars):
        self.cars = cars

    def get_tire_sizes(self):
        return [car.get_tire_size() for car in self.cars]

    def select_tire(self, car):
        suitable_tires = []
        for tire in self.tires:
            if tire.is_compatible_with_car(car):
                suitable_tires.append(tire)
        return suitable_tires

    def select_all_tires(self):
        suitable_tires = {}
        for car in self.cars:
            suitable_tires[car] = self.select_tire(car)
        return suitable_tires
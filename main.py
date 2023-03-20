from car import Car
from tire import Tire
from tire_selector import TireSelector


car1 = Car("Toyota", "Camry", "205/55R16")
car2 = Car("Honda", "Accord", "215/55R17")
car3 = Car("BMW", "X5", "275/40R20")

tire1 = Tire("205/55R16", "Michelin")
tire2 = Tire("215/55R17", "Bridgestone")
tire3 = Tire("275/40R20", "Goodyear")

tires = [tire1, tire2, tire3]

tire_selector = TireSelector(tires)

# Пример выбора подходящих шин для автомобиля
print("Выбор шин для автомобиля", car1.make, car1.model, car1.tire_size)
suitable_tires = tire_selector.select_tire(car1)
for tire in suitable_tires:
    print(tire.brand, tire.size)

# Пример выбора подходящих шин для всех автомобилей
print("\nВыбор шин для всех автомобилей")
cars = [car1, car2, car3]
tire_selector.set_cars(cars)
suitable_tires = tire_selector.select_all_tires()
for car, tires in suitable_tires.items():
    print("Автомобиль", car.make, car.model, "использует шины:")
    for tire in tires:
        print(tire.brand, tire.size)

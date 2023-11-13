class Vehicle:
    def __init__(self):
        self.vehicle_type = ""

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""

    def set_car_details(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_car_details(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)


def main():
    automobile = Automobile()
    vehicle_type = "car"  

    automobile.set_vehicle_type(vehicle_type)
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    automobile.set_car_details(year, make, model, doors, roof)
    print("\nCar Details:")
    automobile.display_car_details()


if __name__ == "__main__":
    main()
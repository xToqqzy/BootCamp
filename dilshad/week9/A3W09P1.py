import datetime
import math


class CarParkingMachine:
    def __init__(self, capacity=10, hourly_rate=2.50):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}

    def check_in(self, license_plate: str, check_in=None):
        if len(self.parked_cars) >= self.capacity:
            return False  # Capacity reached

        if license_plate in self.parked_cars:
            return False  # License plate already inside

        check_in = check_in or datetime.datetime.now()
        self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
        return True  # Successfully registered

    def check_out(self, license_plate: str):
        if license_plate not in self.parked_cars:
            return None  # Not found

        parked_car = self.parked_cars.pop(license_plate)
        fee = self.get_parking_fee(parked_car.check_in)
        return fee  # Fee as a float

    def get_parking_fee(self, check_in_time):
        time_diff = datetime.datetime.now() - check_in_time
        hours_parked = math.ceil(time_diff.total_seconds() / 3600)
        hours_parked = min(hours_parked, 24)
        return self.hourly_rate * hours_parked

    def menu(self):
        while True:
            print("\n[I] Check-in car by license plate")
            print("[O] Check-out car by license plate")
            print("[Q] Quit program")
            choice = input("Please select an option: ").upper()

            if choice == 'I':
                license_plate = input(
                    "Enter the license plate of the car to check in: ")
                result = self.check_in(license_plate)
                if result:
                    print("License registered")
                else:
                    print("Capacity reached!")
            elif choice == 'O':
                license_plate = input(
                    "Enter the license plate of the car to check out: ")
                fee = self.check_out(license_plate)
                if isinstance(fee, float):
                    print(f"Parking fee: {fee:.2f} EUR")
                else:
                    print(f"License {license_plate} not found!")
            elif choice == 'Q':
                print("Exiting the program...")
                break
            else:
                print("Invalid option. Please try again.")


class ParkedCar:
    def __init__(self, license_plate: str, check_in: datetime.datetime):
        self.license_plate = license_plate
        self.check_in = check_in


if __name__ == "__main__":
    car_parking_machine = CarParkingMachine()
    car_parking_machine.menu()

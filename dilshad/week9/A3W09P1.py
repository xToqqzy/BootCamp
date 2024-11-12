class Car:
    def __init__(self, brand, model, color, price) -> None:
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold_to = None

    @property
    def sold(self):
        return self.sold_to is not None

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"color: {self.color}")
        print(f"price: {self.price}")

        if self.sold_to:
            print("Sold to Customer:")
            self.sold_to.print()
        else:
            print("not sold")

    def sell(self, customer):
        self.sold_to = customer


class Motorcycle:
    {}


class Customer:
    def __init__(self, name) -> None:
        self.name = name

    def print(self):
        print(f"Customer Name: {self.name}")


if __name__ == "__main__":
    car = Car("AUDI", "A3", "BLUE", 19.999)
    customer1 = Customer("John Doe")

    car.sell(customer1)

    car.print()

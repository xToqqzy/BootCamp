class Product:
    def __init__(self, name, amount, price) -> None:
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, number_of_items):
        if number_of_items < 10:
            discount = 1
        elif 10 <= number_of_items <= 99:
            discount = 0.90
        else:
            discount = 0.80

        totaalprijs = number_of_items * self.price * discount
        return totaalprijs

    def make_purchase(self, number_of_items):
        if number_of_items <= self.amount:
            self.amount -= number_of_items
            return True
        return False


if __name__ == "__main__":
    product_type = Product("product", 50, 20)
    print("Product name:", product_type.name)
    print("Amount:", product_type.amount)
    print("Price per item:", product_type.price)

    # Example usage
    number_of_items = 15
    total_price = product_type.get_price(number_of_items)
    print(f"Total price for {number_of_items} items:", total_price)

    purchase_successful = product_type.make_purchase(number_of_items)
    if purchase_successful:
        print(f"Purchase successful. Remaining amount: {product_type.amount}")
    else:
        print("Purchase failed. Not enough stock.")

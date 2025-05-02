from products import Product

class Store:
    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added.")
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        # Filtere alle aktiven Produkte
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        total_price = 0.0
        for product, quantity in shopping_list:
            if not product.is_active():
                raise Exception(f"The product {product.name} is not active.")
            total_price += product.buy(quantity)
        return total_price


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    products = best_buy.get_all_products()
    print(f"Total quantity in store: {best_buy.get_total_quantity()}")

    price = best_buy.order([(products[0], 1), (products[1], 2)])
    print(f"Order cost: {price} dollars.")

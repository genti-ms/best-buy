class Store:
    """
    Manages products and orders in the store.
    """

    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        """
        Add a new product to the store.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store.
        """
        self.products.remove(product)

    def get_total_quantity(self):
        """
        Get total quantity of all active products.
        """
        return sum(p.quantity for p in self.products if p.is_active())

    def get_all_products(self):
        """
        Get a list of all active products.
        """
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list):
        """
        Process an order consisting of (product, quantity) pairs.
        """
        total = 0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total
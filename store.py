from products import Product

class Store:
    """
    The Store class manages a collection of products and handles various operations
    like adding/removing products, calculating total quantities, and processing orders.

    Attributes:
        products (list): A list of products available in the store.
    """

    def __init__(self, products=None):
        """
        Initializes the Store instance with a list of products. If no products
        are provided, an empty list is used.

        Args:
            products (list, optional): A list of Product instances. Defaults to None.
        """
        if products is None:
            products = []
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a product to the store's inventory.

        Args:
            product (Product): The Product instance to add to the store.

        Raises:
            TypeError: If the argument is not a Product instance.
        """
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added.")
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store's inventory if it exists.

        Args:
            product (Product): The Product instance to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates and returns the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products in the store.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """
        Returns all active products in the store.

        Returns:
            list: A list of active Product instances.
        """
        # Filters and returns only the active products
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Processes an order consisting of a list of products and quantities,
        and returns the total price of the order.

        Args:
            shopping_list (list): A list of tuples where each tuple contains a Product instance
                                   and the quantity to order.

        Returns:
            float: The total price of the order.

        Raises:
            Exception: If a product in the shopping list is not active.
        """
        total_price = 0.0  # Initialize the total price to 0
        for product, quantity in shopping_list:
            if not product.is_active():
                raise Exception(f"The product {product.name} is not active.")
            total_price += product.buy(quantity)
        return total_price


if __name__ == "__main__":
    # Setup the initial inventory with some products
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    # Retrieve all active products in the store
    products = best_buy.get_all_products()
    print(f"Total quantity in store: {best_buy.get_total_quantity()}")

    # Create an order and calculate the total price
    price = best_buy.order([(products[0], 1), (products[1], 2)])
    print(f"Order cost: {price} dollars.")

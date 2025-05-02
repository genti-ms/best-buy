from products import Product

class Store:
    def __init__(self, products=None):
        """
        Initializes the store with an optional list of products.

        Args:
            products (list): A list of Product objects to initialize the store with.
        """
        if products is None:
            products = []
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a new product to the store.

        Args:
            product (Product): The product to add.

        Raises:
            TypeError: If the product is not an instance of the Product class.
        """
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added.")
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """
        Returns a list of all active products in the store.

        Returns:
            list: List of active Product objects.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Processes an order by reducing the stock of the purchased products and calculating the total price.

        Args:
            shopping_list (list): A list of tuples (product, quantity) to purchase.

        Returns:
            float: The total price of the order.

        Raises:
            Exception: If any product is not active.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if not product.is_active():
                raise Exception(f"The product {product.name} is not active.")
            total_price += product.buy(quantity)
        return total_price

class Product:
    """
    The Product class represents a specific product with attributes like name, price, and quantity.
    It includes methods for managing the product's stock and handling purchases.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The available quantity of the product in the store.
        active (bool): Whether the product is currently available for sale (True or False).
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize the Product instance with the specified name, price, and quantity.
        If any of the values are invalid, a ValueError is raised.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product available in stock.

        Raises:
            ValueError: If the name is empty or the price or quantity are negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid values for products")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Getter method for the product quantity.

        Returns:
            int: The current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Setter method for the product quantity. If the quantity is set to 0, the product is deactivated.

        Args:
            quantity (int): The new quantity to set for the product.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks if the product is active.

        Returns:
            bool: True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activates the product, making it available for purchase.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product, making it unavailable for purchase.
        """
        self.active = False

    def show(self) -> str:
        """
        Returns a string representation of the product.

        Returns:
            str: A string representing the product with its name, price, and quantity.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Purchases a certain quantity of the product, decreasing the stock and returning the total price.
        If there is not enough stock, an exception is raised.

        Args:
            quantity (int): The quantity of the product to purchase.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the purchase quantity is zero or negative.
            Exception: If the requested quantity exceeds the available stock.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if self.quantity < quantity:
            raise Exception("Not enough stock available.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity


# Test code - Example usage of the Product class
if __name__ == "__main__":
    # Create two product instances with specified names, prices, and quantities
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    # Purchase 50 Bose earbud products
    print(bose.buy(50))

    # Purchase 100 MacBook Air M2 products
    print(mac.buy(100))

    # Check if the MacBook Air M2 product is active after purchase
    print(mac.is_active())

    # Display product information for Bose earbud and MacBook Air M2
    bose.show()
    mac.show()

    # Set the quantity of Bose earbud products to 1000
    bose.set_quantity(1000)

    # Display updated information for the Bose earbud product
    bose.show()

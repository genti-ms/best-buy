class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a product with the specified name, price, and quantity.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid values for product")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Returns the quantity of the product in stock.

        Returns:
            int: The quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets a new quantity for the product and deactivates it if quantity is zero.

        Args:
            quantity (int): The new quantity to set.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Returns whether the product is active (i.e., in stock).

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """Activate the product (make it available for purchase)."""
        self.active = True

    def deactivate(self):
        """Deactivate the product (remove it from being available for purchase)."""
        self.active = False

    def show(self) -> str:
        """
        Returns a string representation of the product, including name, price, and quantity.

        Returns:
            str: Product details.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Simulates buying a certain quantity of the product, deducting from stock and returning the total price.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price for the purchased quantity.

        Raises:
            ValueError: If quantity is less than or equal to zero.
            Exception: If there is insufficient stock.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if self.quantity < quantity:
            raise Exception("Not enough stock available.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity

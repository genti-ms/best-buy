class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def show(self):
        """
        Return a string representation of the product.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def is_active(self):
        """
        Check if the product is active (quantity > 0).
        """
        return self.quantity > 0

    def activate(self):
        """
        Activate the product.
        """
        if self.quantity == 0:
            self.quantity = 1

    def deactivate(self):
        """
        Deactivate the product.
        """
        self.quantity = 0

    def buy(self, quantity):
        """
        Process the purchase of a quantity of this product.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")
        self.quantity -= quantity
        return self.price * quantity
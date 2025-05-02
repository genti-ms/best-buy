import products
import store


def start(best_buy: store.Store):
    """
    Starts the user interface for the store.
    Displays the main menu and processes user input.

    Args:
        best_buy (store.Store): The store object that contains all products.
    """
    while True:
        # Display the menu options
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        # Get the user's choice
        choice = input("Please choose a number: ")

        if choice == "1":
            # Option 1: List all products in the store
            all_products = best_buy.get_all_products()
            print("------")
            for idx, product in enumerate(all_products, 1):
                print(f"{idx}. {product.show()}")
            print("------")

        elif choice == "2":
            # Option 2: Show the total quantity of products in the store
            total_quantity = best_buy.get_total_quantity()
            print(f"\nTotal of {total_quantity} items in store")

        elif choice == "3":
            # Option 3: Make an order
            products_list = best_buy.get_all_products()
            print("------")
            for idx, product in enumerate(products_list, 1):
                print(f"{idx}. {product.show()}")
            print("------")
            print("When you want to finish the order, enter empty text.")

            shopping_list = []
            while True:
                # Get product number
                product_input = input("Which product # do you want? ").strip()
                if product_input == "":
                    break

                try:
                    # Convert product number to index
                    product_index = int(product_input) - 1
                    if product_index < 0 or product_index >= len(products_list):
                        print("Invalid product number.")
                        continue

                    # Get quantity for the product
                    quantity_input = input("What amount do you want? ").strip()
                    quantity = int(quantity_input)
                    if quantity <= 0:
                        print("Quantity must be positive.")
                        continue

                    # Add product and quantity to shopping list
                    shopping_list.append((products_list[product_index], quantity))
                    print("Product added to list!")

                except ValueError:
                    print("Invalid input, please enter numbers.")

            if shopping_list:
                try:
                    # Place the order and calculate the total price
                    total_price = best_buy.order(shopping_list)
                    print("********")
                    print(f"Order made! Total payment: ${int(total_price)}")
                except Exception as e:
                    print(f"Error: {e}")

        elif choice == "4":
            # Option 4: Quit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


# Initial product inventory setup
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)

if __name__ == "__main__":
    # Start the user interface with the store instance
    start(best_buy)

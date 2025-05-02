import products
import store

def start(best_buy: store.Store):
    """
    Function to start the user interface for the store.
    Displays a menu to the user and processes user input.

    Args:
        best_buy (store.Store): The store object that contains the products.
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
            shopping_list = []
            while True:
                print("------")
                print("When you want to finish order, enter empty text.")
                product_choice = input("Which product # do you want? ")
                if product_choice == "":
                    break

                try:
                    product_index = int(product_choice) - 1
                    product = best_buy.get_all_products()[product_index]
                except (ValueError, IndexError):
                    print("Invalid product number. Please try again.")
                    continue

                amount = input(f"What amount do you want? ")
                try:
                    quantity = int(amount)
                    if quantity <= 0:
                        print("Please enter a valid quantity.")
                        continue
                except ValueError:
                    print("Please enter a valid number for the quantity.")
                    continue

                shopping_list.append((product, quantity))

            # Calculate and display the total price for the order
            if shopping_list:
                try:
                    total_price = best_buy.order(shopping_list)
                    print(f"Order cost: {total_price} dollars.")
                except Exception as e:
                    print(f"Error: {e}")

        elif choice == "4":
            # Option 4: Quit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

# Initial inventory setup
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)

if __name__ == "__main__":
    start(best_buy)

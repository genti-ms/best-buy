import products
import store

def list_products(best_buy):
    """List all products in the store."""
    all_products = best_buy.get_all_products()
    print("------")
    for idx, product in enumerate(all_products, 1):
        print(f"{idx}. {product.show()}")
    print("------")


def show_total(best_buy):
    """Show total number of items in the store."""
    total_quantity = best_buy.get_total_quantity()
    print(f"\nTotal of {total_quantity} items in store")


def make_order(best_buy):
    """Handle making an order from the store."""
    products_list = best_buy.get_all_products()
    print("------")
    for idx, product in enumerate(products_list, 1):
        print(f"{idx}. {product.show()}")
    print("------")
    print("When you want to finish order, enter empty text.")

    shopping_list = []
    while True:
        product_input = input("Which product # do you want? ").strip()
        if product_input == "":
            break

        try:
            product_index = int(product_input) - 1
            if product_index < 0 or product_index >= len(products_list):
                print("Invalid product number.")
                continue

            quantity_input = input("What amount do you want? ").strip()
            quantity = int(quantity_input)
            if quantity <= 0:
                print("Quantity must be positive.")
                continue

            shopping_list.append((products_list[product_index], quantity))
            print("Product added to list!")

        except ValueError:
            print("Invalid input, please enter numbers.")

    if shopping_list:
        try:
            total_price = best_buy.order(shopping_list)
            print(f"********\nOrder made! Total payment: ${int(total_price)}")
        except ValueError as error:
            print(f"Error: {error}")


def start(best_buy):
    """Start the store user interface."""
    while True:
        print("\n    Store Menu")
        print("    ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(best_buy)
        elif choice == "2":
            show_total(best_buy)
        elif choice == "3":
            make_order(best_buy)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)

if __name__ == "__main__":
    start(best_buy)

import products
import store

def list_products(store_obj):
    """
    List all products in the store.
    """
    all_products = store_obj.get_all_products()
    print("------")
    for idx, product in enumerate(all_products, 1):
        print(f"{idx}. {product.show()}")
    print("------")


def make_order(store_obj):
    """
    Process an order from the user.
    """
    products_list = store_obj.get_all_products()
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
            total_price = store_obj.order(shopping_list)
            print(f"********\nOrder made! Total payment: ${int(total_price)}")
        except Exception as error:
            print(f"Error: {error}")


def start(store_obj: store.Store):
    """
    Start the store user interface.
    """
    while True:
        print("\n    Store Menu")
        print("    ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal of {total_quantity} items in store")
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# Set up the initial product inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy_store = store.Store(product_list)

if __name__ == "__main__":
    start(best_buy_store)
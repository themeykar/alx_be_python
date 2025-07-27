def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == "1":
            add_item = input(f"Enter the item to add: {shopping_list.append()}")
            pass
        elif choice == "2":
            remove_item = input(f"Enter the item to remove: {shopping_list.remove()}")
            pass

        elif choice == "3":
            for item in shopping_list:
                print(item)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")
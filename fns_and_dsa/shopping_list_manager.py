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
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item_added = input("Enter the item: ")
            shopping_list.append(item_added)
            print(shopping_list)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("What would you like to remove? ")
            if remove_item == shopping_list:
                shopping_list.remove(remove_item)
                print("Item removed", remove_item)
            else:
                print("Item not found on the list.")
                pass
        
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
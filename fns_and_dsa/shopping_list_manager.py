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
        choice = input("Enter your choice: ").strip()

        # Validate that the input is a number
        try:
            choice = int(choice)  # Convert input to integer
            if choice not in [1, 2, 3, 4]:  # Check if choice is valid
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:  # Use integer comparison
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"{item} added to the shopping list.")
            else:
                print("Item cannot be empty.")
        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")
        elif choice == 3:
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
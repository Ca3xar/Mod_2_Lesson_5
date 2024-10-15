def main():
    shopping_list = []
    while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. Print list")
        print("4. Quit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        ask_again = input("do you want to continue: yes or no: ")
        if ask_again != "yes":
            break

def add_item(shopping_list):
    item = input("Enter the item you want to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item you want to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in your shopping list.")

def print_list(shopping_list):
    if shopping_list:
        print("Your shopping list:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")


if __name__ == "__main__":
    main()
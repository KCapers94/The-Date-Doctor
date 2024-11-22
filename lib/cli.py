from helpers import (
    exit_program,
    list_categories,
    add_new_idea,
    delete_idea,
    idea_get_all_by_category_id,
    create_new_category,
    delete_category
)
from models.category import Category

def main():
    while True:
        menu()
        print("")
        print("")
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            categories_menu()
        else:
            print("Invalid choice")

def categories_menu():
    while True:
        print("")
        categories = list_categories()
        print("")
        print("")
        print("**Type s. to Select a category to view date_ideas **")
        print("**Type a. to Add Category **")
        print("**Type d. to Delete Category **")
        print("**Type b. to go Back to previous menu **")
        print("**Type 0. to Exit Program **")
        print("")
        print("")

        choice = input("> ")
        print("")
        if choice == "a":
            create_new_category()
        elif choice == "d":
            delete_category()
        elif choice == "s":
            selected_category = select_category_by_index(categories)
            if selected_category:
                extra_menu(selected_category)
        elif choice == "b":
            break
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice")

def select_category_by_index(categories):
    index_input = input("Enter the category number: ")
    try:
        index = int(index_input) - 1
        if 0 <= index < len(categories):
            return categories[index]
        else:
            print("Invalid category number.")
    except ValueError:
        print("Please enter a valid number.")
    return None

def extra_menu(selected_category):
    while True:
        print("")
        print(f"Selected Category: {selected_category.name}")
        print("")
        idea_get_all_by_category_id(selected_category)
        print("")
        print("")
        print("**Type a. to Add New Date **")
        print("**Type d. to Delete Date **")
        print("**Type b. to Back to categories menu **")
        print("**Type 0. to Exit program **")

        choice = input("> ")
        if choice == "a":
            add_new_idea(selected_category)
        elif choice == "d":
            delete_idea()
        elif choice == "b":
            break
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice")

def menu():
    print("**The Date Doctor!**")
    print("")
    print("**Time to Operate!**")
    print("")
    print("**Type 1. to see list of Categories**")
    print("**Type 0. to Exit program**")

if __name__ == "__main__":
    main()
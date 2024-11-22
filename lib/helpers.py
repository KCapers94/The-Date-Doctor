from models.category import Category
from models.idea import Idea

def create_new_category():
    name = input("Enter new category name: ")
    try:
        category = Category.create(name)
        print(f'Nice: {category}')
    except Exception as exc:
        print("Error creating category: ", exc)


def delete_category():
    name = input("Enter the category name: ")
    if category := Category.find_by_name(name):
        ideas = Idea.find_by_category_id(category.id)
        for idea in ideas:
            idea.delete()
        category.delete()
        
        print(f'Category {name} deleted')
    else:
        print(f'Category {name} not found')

def list_categories():
    categories = Category.get_all()
    for i, category in enumerate(categories, start=1):
        print(f"{i}: {category.name}")
    return categories

def idea_get_all_by_category_id(selected_category):
    try:
        ideas = Idea.find_by_category_id(selected_category.id)
        if ideas:
            for idea in ideas:
                print(f"{idea.date_idea}-{idea.date_details}")
        else:
            print(f"No ideas found for category {selected_category.name}.")
    except Exception as exc:
        print("Error retrieving ideas: ", exc)

def add_new_idea(selected_category):
    date_idea = input("Enter date idea: ")
    date_details = input("Enter type of restaurant/ or price of date: ")

    try:
        if date_details.strip() == "":
            date_details = None

        idea = Idea.create(date_idea, selected_category.id, date_details)
        print(f"{idea} has been added to {selected_category.name}!")

    except Exception as exc:
        print("Error: not valid ", exc)

def delete_idea():
    name = input("Enter the date name: ")
    if category := Idea.find_by_name(name):
        category.delete()
        print(f'{name} deleted')
    else:
        print(f'{name} not found')

def select_category():
    category_id = input("Enter the category number: ")
    try:
        category = Category.find_by_id(int(category_id))
        if category:
            return category
        else:
            print("Category not found. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return None

def exit_program():
    print("Goodbye!")
    exit()
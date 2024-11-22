from models.__init__ import CONN, CURSOR
from models.category import Category
from models.idea import Idea


def seed_database():
    Category.drop_table()
    Idea.drop_table()
    Category.create_table()
    Idea.create_table()


    restaurant = Category.create("Restaurants")
    activites = Category.create("Activites")
    gifts = Category.create("Gifts")

    Idea.create("The Brownstone Pancake House",restaurant.id, "Brunch")
    Idea.create("Tops Diner",restaurant.id, "Casual Dining",)
    Idea.create("Sky Diving",activites.id, "$350")
    Idea.create("Bowling",activites.id, "$75")
    Idea.create("Pool",activites.id, "$50")
    Idea.create("Flowers",gifts.id, "$50")
    Idea.create("Jewlery",gifts.id, "$500")

seed_database()
print("Seeded database")

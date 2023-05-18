from book import Book
from recipe import Recipe

if __name__=="__main__":
    try:
        book = Book("libro")
        print(book.creation_date)
        print(book.last_update)
        book.add_recipe(Recipe("burrito", 1, 45, ["tortilla", "queso", "carne"], "lunch", "tortilla con queso y carne"))
        book.add_recipe(Recipe("cake", 2, 30, ["flour", "milk", "eggs"], "dessert"))
        book.add_recipe(Recipe("salad", 4, 30, ["tomato", "lettuce", "eggs"], "lunch"))
        print(book.last_update)
        recipes = book.get_recipes_by_types("lunch")
        if recipes:
            for i in recipes: print(i)
        print(book.get_recipe_by_name("s"))
        book.get_recipe_by_name("cake")
    except Exception as e:
        print(e)
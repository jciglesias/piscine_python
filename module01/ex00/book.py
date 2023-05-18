import datetime
from recipe import Recipe

class Book:
    def __init__(self, name: str) -> None:
        if type(name) is not str:
            raise Exception("not a valid Book name")
        self.name = name
        time = datetime.datetime.now()
        self.last_update = time
        self.creation_date = time
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}
    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        self.last_update = datetime.datetime.now()
        self.recipes_list[recipe.recipe_type].append(recipe)
    def get_recipes_by_types(self, recipe_type: str):
        """Get all recipe names for a given recipe_type """
        return self.recipes_list.get(recipe_type)
    def get_recipe_by_name(self, name: str):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        recipes = []
        recipes.extend(self.recipes_list.get("starter"))
        recipes.extend(self.recipes_list.get("lunch"))
        recipes.extend(self.recipes_list.get("dessert"))
        for i in recipes:
            if name == i.name:
                print(i)
                return i
        return None
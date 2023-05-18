class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, recipe_type: str, description: str = None) -> None:
        #  only the description can be empty. In case of input errors, you should print what they are and exit properly.
        if type(name) is not str:
            raise Exception("not a valid name")
        self.name = name
        if cooking_lvl not in [1, 2, 3, 4, 5]:
            raise Exception("cooking lvl not in range")
        self.cooking_lvl = cooking_lvl
        if type(cooking_time) is not int or cooking_time < 0:
            raise Exception("not a valid cooking time")
        self.cooking_time = cooking_time
        if type(ingredients) is not list or ingredients == []:
            raise Exception("not a valid ingredients list")
        self.ingredients = ingredients
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise Exception("not a valid recipe type")
        self.recipe_type = recipe_type
        if description != None and type(description) is not str:
            raise Exception("not a valid description")
        self.description = description
    def __str__(self) -> str:
        """Return the string to print with the recipe info"""
        st = f"Recipe for {self.name}:\n"
        if self.description != None:
            st += self.description + "\n"
        st += f"\tlevel of difficulty: {self.cooking_lvl}\n"
        st += f"\ttakes {self.cooking_time} minutes of cooking\n"
        st += f"\tingredients: {self.ingredients}\n"
        st += f"\tto be eaten for {self.recipe_type}"
        return st

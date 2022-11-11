cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10,
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    },
}

def print_cookbook(val = None):
    global cookbook;
    for i in range(len(cookbook)):
        print(list(cookbook.keys())[i], end = ":\n");
        val = list(cookbook.values())[i];
        for j in range(len(val)):
            print("\t", list(val.keys())[j], ": ", list(val.values())[j]);

def print_recipe(name = None):
    global cookbook;
    print(f"Recipe for {name}", end = ":\n");
    recipe = cookbook.get(name)
    if recipe != None:
        print("\tIngredients list: ", list(recipe.values())[0]);
        print("\tTo be eaten for", list(recipe.values())[1]);
        print(f"\tTakes {list(recipe.values())[2]} minutes of cooking");
    else:
        print("\tRecipe does not exist.");

def delete_recipe(name = None):
    global cookbook;
    if cookbook.get(name) != None:
        cookbook.pop(name);
        print("\tRecipe deleted.");
    else:
        print("\tRecipe does not exist.");

def set_recipe(val = None):
    global cookbook;
    ingredients = [];
    name = input("Enter a name:\n")
    print("Enter ingredients");
    for i in range(3):
        ingredients.append(input());
    recipe = {
        "ingredients": ingredients,
        "meal": input("Enter a meal type:\n"),
        "prep_time": input("Enter a preparation time:\n"),
    };
    cookbook[name] = recipe; # cookbook.update({name: recipe});

if __name__=="__main__":
    run = True;
    select_opt = [set_recipe, delete_recipe, print_recipe, print_cookbook];
    print("Welcome to the Python Cookbook !");
    while(run):
        print("List of available options:\n  1: Add a recipe\n  2: Delete a recipe\n  3: Print a recipe\n  4: Print the cookbook\n  5: Quit");
        try:
            opt = int(input("Please select an option:\n"));
        except ValueError as ve:
            opt = 0;
        if opt == 5:
            run = False;
        elif opt < 5 and opt > 0:
            val = None;
            if opt == 2 or opt == 3:
                val = input("Please enter a recipe name:\n")
            select_opt[opt - 1](val);
        else:
            print("Sorry, this option does not exist.");
    print("Cookbook closed. Goodbye !");

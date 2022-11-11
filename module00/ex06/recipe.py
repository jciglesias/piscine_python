cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10,
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    },
}

def print_cookbook():
    global cookbook;
    for i in range(len(cookbook)):
        print(list(cookbook.keys())[i], end = ":\n");
        val = list(cookbook.values())[i];
        for j in range(len(val)):
            print("\t", list(val.keys())[j], ": ", list(val.values())[j]);

def print_recipe(name = None):
    global cookbook;
    print(name, end = ":\n");
    recipe = cookbook.get(name)
    if recipe != None:
        for j in range(len(recipe)):
            print("\t", list(recipe.keys())[j], ": ", list(recipe.values())[j]);

def delete_recipe(name = None):
    global cookbook;
    if cookbook.get(name) != None:
        cookbook.pop(name);

def set_recipe():
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

delete_recipe("Cake");
print_cookbook();
set_recipe();
print_recipe("Burrito");

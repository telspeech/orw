def create_cook_book(file_name):
    cook_book = {}
    with open(file_name, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            ingredient_count = int(lines[i + 1].strip())
            ingredients = []
            for j in range(i + 2, i + 2 + ingredient_count):
                ingredient_info = lines[j].strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            i += 2 + ingredient_count
    return cook_book

def print_cook_book(cook_book):
    for dish, ingredients in cook_book.items():
        print(f"{dish}:")
        for ingredient in ingredients:
            print(f"  {ingredient['ingredient_name']}: {ingredient['quantity']} {ingredient['measure']}")
        print()

file_name = 'recipes.txt'  # Название файла с рецептами
cook_book = create_cook_book(file_name)
print_cook_book(cook_book)
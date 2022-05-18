import os
from pprint import pprint
from collections import Counter

BASE_PATH = os.getcwd()
RECIPES_DIR_NAME = 'other_files'
RECIPES_FILE_NAME = 'recipes.txt'
full_path = os.path.join(BASE_PATH, RECIPES_DIR_NAME, RECIPES_FILE_NAME)


def cock_book_definition(name_file: str):
    with open(name_file, 'r') as file:
        dishes = []
        ingredients = []
        name = file.readline().strip()
        dishes.append(name)
        for line in file:
            count = int(line.strip())
            dish_ing = []
            for i in range(count):
                ingredient_dict = {}
                data = file.readline().strip()
                split_data = data.split('|')
                ingredient_dict['ingredient_name'] = split_data[0]
                ingredient_dict['quantity'] = int(split_data[1])
                ingredient_dict['mesure'] = split_data[2]
                dish_ing.append(ingredient_dict)
            file.readline()
            name = file.readline().strip()
            ingredients.append(dish_ing)
            dishes.append(name)
        cook_book = dict(zip(dishes, ingredients))
        return cook_book


# pprint(cock_book_definition(full_path))


def get_shop_list_by_dishes(dishes, person_count):
    result_dict = {}
    cook_book = cock_book_definition(full_path)
    menu = list(dict.keys(cook_book))
    counter = Counter(dishes)
    for dish in dishes:
        print(counter[dish])
        if dish not in menu:
            print(f'This dish: "{dish}" not in our menu, sorry!')
        else:
            order = cook_book[dish]
            for i in order:
                i['quantity'] *= int(person_count)
                ing_name = i['ingredient_name']
                ing_count = i['quantity'] * counter[dish]
                ing_measure = i['mesure']
                result_dict[ing_name] = {'quantity': ing_count, 'mesure': ing_measure}
    pprint(result_dict)


get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Фахитос', 'Омлет'], 1)

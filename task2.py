def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        ingredients = cook_book.get(dish)
        if ingredients:
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[name]['quantity'] += quantity

    return shop_list


# Пример использования
dishes_to_cook = ['Запеченный картофель', 'Омлет']
person_count = 2
result_shop_list = get_shop_list_by_dishes(dishes_to_cook, person_count)

# Вывод результата
print(result_shop_list)
def read_cook_book(filename):
    """
    Читает кулинарную книгу из файла и возвращает словарь с рецептами.
    """
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            # Читаем название блюда
            dish_name = file.readline().strip()
            if not dish_name:  # если достигнут конец файла
                break

            # Читаем количество ингредиентов
            ingredient_count = int(file.readline().strip())

            ingredients = []
            for _ in range(ingredient_count):
                # Читаем и парсим строку с ингредиентом
                ingredient_line = file.readline().strip()
                if not ingredient_line:
                    break

                name, quantity, unit = [part.strip() for part in ingredient_line.split('|')]
                ingredients.append({
                    'name': name,
                    'quantity': int(quantity),
                    'unit': unit
                })

            cook_book[dish_name] = ingredients
            file.readline()  # пропускаем пустую строку между рецептами

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """
    Формирует список покупок для заданных блюд и количества персон.

    :param dishes: список названий блюд
    :param person_count: количество персон
    :param cook_book: словарь с рецептами
    :return: словарь с ингредиентами и их количествами
    """
    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюдо '{dish}' не найдено в кулинарной книге!")
            continue

        for ingredient in cook_book[dish]:
            name = ingredient['name']
            measure = ingredient['unit']
            quantity = ingredient['quantity'] * person_count

            if name in shop_list:
                # Если ингредиент уже есть в списке, суммируем количество
                shop_list[name]['quantity'] += quantity
            else:
                # Добавляем новый ингредиент в список
                shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list


# Пример использования
if __name__ == "__main__":
    # Читаем кулинарную книгу из файла
    cook_book = read_cook_book('cook_book.txt')

    # Формируем список покупок
    shopping_list = get_shop_list_by_dishes(
        dishes=['Запеченный картофель', 'Омлет'],
        person_count=2,
        cook_book=cook_book
    )

    # Выводим результат
    print("Список покупок:")
    for ingredient, details in shopping_list.items():
        print(f"{ingredient}: {details['quantity']} {details['measure']}")
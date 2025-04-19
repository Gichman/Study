def read_recipes_from_file(filename):
    """
    Читает рецепты из файла и возвращает список словарей с рецептами.
    Каждый рецепт представлен в виде словаря с ключами:
    - 'name': название блюда
    - 'ingredients': список ингредиентов (каждый ингредиент - словарь с 'name', 'quantity', 'unit')
    """
    recipes = []
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            # Читаем название блюда
            name = file.readline().strip()
            if not name:  # если достигнут конец файла
                break

            # Читаем количество ингредиентов
            ingredient_count = int(file.readline().strip())

            ingredients = []
            for _ in range(ingredient_count):
                # Читаем строку с ингредиентом и разбиваем ее
                ingredient_line = file.readline().strip()
                if not ingredient_line:
                    break

                # Разделяем строку на части
                parts = [part.strip() for part in ingredient_line.split('|')]
                if len(parts) != 3:
                    continue

                ingredient = {
                    'name': parts[0],
                    'quantity': parts[1],
                    'unit': parts[2]
                }
                ingredients.append(ingredient)

            recipe = {
                'name': name,
                'ingredients': ingredients
            }
            recipes.append(recipe)

    return recipes


def write_recipe_to_file(filename, recipe):
    """
    Добавляет новый рецепт в конец файла.
    recipe - словарь с ключами 'name' и 'ingredients'
    """
    with open(filename, 'a', encoding='utf-8') as file:
        # Записываем название блюда
        file.write(f"{recipe['name']}\n")

        # Записываем количество ингредиентов
        file.write(f"{len(recipe['ingredients'])}\n")

        # Записываем каждый ингредиент
        for ingredient in recipe['ingredients']:
            file.write(f"{ingredient['name']} | {ingredient['quantity']} | {ingredient['unit']}\n")

        # Добавляем пустую строку для разделения рецептов
        file.write("\n")


def print_recipe(recipe):
    """Выводит рецепт в удобочитаемом формате."""
    print(f"\n{recipe['name']}")
    print("Ингредиенты:")
    for ing in recipe['ingredients']:
        print(f"- {ing['name']}: {ing['quantity']} {ing['unit']}")


def print_all_recipes(recipes):
    """Выводит все рецепты."""
    print("\nВсе рецепты:")
    for i, recipe in enumerate(recipes, 1):
        print(f"\nРецепт {i}:")
        print_recipe(recipe)


def input_recipe():
    """Запрашивает у пользователя данные для нового рецепта."""
    name = input("\nВведите название блюда: ")

    ingredients = []
    while True:
        try:
            count = int(input("Введите количество ингредиентов: "))
            if count <= 0:
                print("Количество должно быть положительным числом!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

    for i in range(count):
        print(f"\nИнгредиент {i + 1}:")
        ing_name = input("Название ингредиента: ")
        quantity = input("Количество: ")
        unit = input("Единица измерения: ")

        ingredients.append({
            'name': ing_name,
            'quantity': quantity,
            'unit': unit
        })

    return {
        'name': name,
        'ingredients': ingredients
    }


def main():
    filename = "recipes.txt"

    while True:
        print("\nМеню:")
        print("1. Просмотреть все рецепты")
        print("2. Добавить новый рецепт")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            try:
                recipes = read_recipes_from_file(filename)
                print_all_recipes(recipes)
            except FileNotFoundError:
                print("Файл с рецептами не найден. Сначала добавьте рецепт.")

        elif choice == '2':
            recipe = input_recipe()
            write_recipe_to_file(filename, recipe)
            print("Рецепт успешно добавлен!")

        elif choice == '3':
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")


if __name__ == "__main__":
    main()
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def find_person_by_document():
    doc_number = input("Введите номер документа: ")
    for document in documents:
        if document["number"] == doc_number:
            print(f"Владелец документа: {document['name']}")
            return
    print("Документ не найден.")

def find_shelf_by_document():
    doc_number = input("Введите номер документа: ")
    for shelf, docs in directories.items():
        if doc_number in docs:
            print(f"Документ находится на полке: {shelf}")
            return
    print("Документ не найден на полках.")

def list_all_documents():
    print("Список документов:")
    for document in documents:
        print(f"{document['type']} \"{document['number']}\" \"{document['name']}\"")

def add_new_document():
    doc_number = input("Введите номер документа: ")
    doc_type = input("Введите тип документа: ")
    doc_name = input("Введите имя владельца: ")
    shelf_number = input("Введите номер полки: ")

    if shelf_number in directories:
        documents.append({"type": doc_type, "number": doc_number, "name": doc_name})
        directories[shelf_number].append(doc_number)
        print("Документ успешно добавлен.")
    else:
        print("Такой полки не существует. Документ не добавлен.")

def delete_document():
    doc_number = input("Введите номер документа для удаления: ")

    
    for document in documents:
        if document["number"] == doc_number:
            documents.remove(document)
            break
    else:
        print("Документ не найден.")
        return


    for docs in directories.values():
        if doc_number in docs:
            docs.remove(doc_number)
            break

    print("Документ успешно удалён.")

def move_document():
    doc_number = input("Введите номер документа для перемещения: ")
    target_shelf = input("Введите номер полки, на которую переместить документ: ")


    found = False
    for docs in directories.values():
        if doc_number in docs:
            docs.remove(doc_number)
            found = True
            break
    if not found:
        print("Документ не найден.")
        return


    if target_shelf not in directories:
        print("Полка не существует. Перемещение невозможно.")
        return

    directories[target_shelf].append(doc_number)
    print(f"Документ перемещён на полку {target_shelf}.")

def add_shelf():
    new_shelf = input("Введите номер новой полки: ")
    if new_shelf in directories:
        print("Такая полка уже существует.")
    else:
        directories[new_shelf] = []
        print(f"Полка {new_shelf} добавлена.")


while True:
    command = input("\nВведите команду (p, s, l, a, d, m, as, q для выхода): ").lower()
    if command == 'p':
        find_person_by_document()
    elif command == 's':
        find_shelf_by_document()
    elif command == 'l':
        list_all_documents()
    elif command == 'a':
        add_new_document()
    elif command == 'd':
        delete_document()
    elif command == 'm':
        move_document()
    elif command == 'as':
        add_shelf()
    elif command == 'q':
        print("Выход из программы.")
        break
    else:
        print("Неизвестная команда. Попробуйте снова.")
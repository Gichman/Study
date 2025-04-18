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
        # Добавим документ в список документов
        documents.append({"type": doc_type, "number": doc_number, "name": doc_name})
        # Добавим номер на полку
        directories[shelf_number].append(doc_number)
        print("Документ успешно добавлен.")
    else:
        print("Такой полки не существует. Документ не добавлен.")

# Основной цикл
while True:
    command = input("\nВведите команду (p, s, l, a, q для выхода): ").lower()
    if command == 'p':
        find_person_by_document()
    elif command == 's':
        find_shelf_by_document()
    elif command == 'l':
        list_all_documents()
    elif command == 'a':
        add_new_document()
    elif command == 'q':
        print("Выход из программы.")
        break
    else:
        print("Неизвестная команда. Попробуйте снова.")
def count_lines_in_file(filename):
    """Подсчитывает количество строк в файле."""
    with open(filename, 'r', encoding='utf-8') as file:
        return len(file.readlines())


def merge_files(input_files, output_file):
    """
    Объединяет файлы в один с сортировкой по количеству строк.

    :param input_files: список файлов для объединения
    :param output_file: имя результирующего файла
    """
    # Создаем список кортежей (количество строк, имя файла, содержимое)
    files_data = []

    for filename in input_files:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.readlines()
            line_count = len(content)
            files_data.append((line_count, filename, content))

    # Сортируем файлы по количеству строк (от меньшего к большему)
    files_data.sort()

    # Записываем отсортированные файлы в результирующий файл
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for line_count, filename, content in files_data:
            # Записываем служебную информацию
            out_file.write(f"{filename}\n{line_count}\n")
            # Записываем содержимое файла
            out_file.writelines(content)
            # Добавляем перенос строки между файлами, если это не последний файл
            if (line_count, filename, content) != files_data[-1]:
                out_file.write("\n")


# Пример использования
if __name__ == "__main__":
    # Список файлов для объединения (должны существовать в папке с программой)
    files_to_merge = ['1.txt', '2.txt']
    # Имя результирующего файла
    result_file = 'result.txt'

    merge_files(files_to_merge, result_file)
    print(f"Файлы успешно объединены в {result_file}")
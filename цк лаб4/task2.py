import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Открываем CSV файл для чтения
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        # Читаем CSV файл
        reader = csv.DictReader(csv_file)

        # Преобразуем все строки в список словарей
        rows = [row for row in reader]

    # Записываем результат в JSON файл с отступами 4
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # Выполняем конвертацию CSV в JSON
    task()

    # Проверяем результат
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
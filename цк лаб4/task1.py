import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    total_sum = sum(item['score'] * item['weight'] for item in data)

    return round(total_sum, 3)

if __name__ == '__main__':
    print(task())
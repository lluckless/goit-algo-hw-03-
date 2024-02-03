from pathlib import Path

def get_cats_info(path):
    cats_data_list = [] 
    try:
        with open(path, 'r', encoding="UTF-8") as fh:                                                     # Відкриття файлу за допомогою менеджера
            for line in fh:
                cat_info = line.strip().split(',')                                                        # Очищення від пробілів і розділення рядка
                cats_data_list.append({'id': cat_info[0], 'name': cat_info[1], 'cats_age': cat_info[2]})  # Додавання у словник за індексами.
        return cats_data_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

path = Path("HomeworkM4") / "Cats.txt"                                                                    # Метод Path забезпечує стабільність отримування шляху на будь-яких системах
cats_info = get_cats_info(path)

print(cats_info)
# if cats_info:                     # Цю перевірку додав gpt, мені здається вона не потрібна для цього завдання
#     for cat in cats_info:         # Перевірка якщо повернуте значення True, то вивід в консоль
#         print(cat)

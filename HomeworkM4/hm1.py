from pathlib import Path

def total_salary(file_path):
    try:                                                                # Блок обробки можливих помилок
        with open(file_path, "r", encoding= "UTF-8") as file:           # Відкриття файла за допомогою менеджера
            lines = file.readlines()
            salaries = [int(line.split(',')[1]) for line in lines]      # Перебір значень за індексом, розділення по знаку, перетворення до int та запис у список
                                                                        
        total_sum = sum(salaries)
        average_salary = total_sum / len(salaries)

        print(f'Total sum: {total_sum}, Average: {average_salary}')
        return total_sum, average_salary
    
    except FileNotFoundError:
        print(f'Error: File is not found - {file_path}')
    
    except Exception as e:
        print(f'An error occured: {e}')

file_path = Path("HomeworkM4") / "salary_file.txt"                      # Метод Path забезпечує стабільність отримування шляху на будь-яких системах.
total_salary(file_path)

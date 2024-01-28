import random

def get_number_ticket(min, max, quantity):
    
    if 1 <= min < max <= 1000 and 1 <= quantity <= (max-min+1):   # Перевірка вводу корректних данних
        numbers = range(min, max+1)                               # Створення списку [1-1000]
        happyTicket = sorted(random.sample(numbers, quantity))    # Створення відсортованної вибірки
        return happyTicket
        
    else:
        print("\nValues can be [1-1000]")
        print("All ploho давай по новой")
        return []

while True: 
    try:                                                      # Блок перевірки з ймовірністю помилки
        min = int(input("Enter a min int number: "))          
        max = int(input("Enter a max int number: "))          
        quantity = int(input("Enter int quantity: "))
    
    except Exception:
        continue
    
    answer = get_number_ticket(min, max, quantity)            # Виклик функції
    if answer == []:
        continue
    else:
        print(answer)
        break

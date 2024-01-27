import random

def get_number_ticket(min,max,quantity):
        if 1 <= min < max <= 1000 and 1 <= quantity <= (max-min+1):
            numbers = range(min, max+1)
            happyTicket = random.sample(numbers, quantity)
            happyTicket.sort()
            return happyTicket
        
        else:
            print("\nValues can be [1-1000]")
            print("All ploho давай по новой")
            return []

while True: 
        try:
            min = int(input("Enter a min int number: "))
            max = int(input("Enter a max int number: "))
            quantity = int(input("Enter int quantity: "))
        except Exception:
             continue
        answer = get_number_ticket(min, max, quantity)
        if answer == []:
            continue
        else:
            print(answer)
            break

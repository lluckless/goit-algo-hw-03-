import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    phone_number=''.join(re.findall(r"[\d\+]",phone_number))           # Форматування номеру
    
    if not re.search(r"^\+", phone_number):                            # Перевірка на наявність префіксів
        if re.search(r"^3", phone_number):
            phone_number = "+" + phone_number
        else:
            phone_number = "+38" + phone_number
    return phone_number

for phone in raw_numbers:
    print(normalize_phone(phone))

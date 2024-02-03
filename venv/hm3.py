from pathlib import Path
import sys
from colorama import Fore

def main():
    if len(sys.argv) < 2:                             # Перевірка вводу. Чи ввів користувач шлях до директорії
        user_input = ""
    else:
        user_input = sys.argv[1]
    
    path = Path(user_input)

    if path.exists():                                 # Перевірка чи існує файл/директорія
        if path.is_dir():                             # Перевірка чи це директорія
            items = path.glob("**/*")                 # Метод який показує усе, що є у директорії
            for item in items:
                print(f'{Fore.YELLOW} {item} {Fore.RESET}')
        else:
            print(f'{path} {Fore.GREEN}is a file{Fore.RESET}') 
    else:
        print(f'{path.absolute()} {Fore.RED} is not exists {Fore.RESET}')

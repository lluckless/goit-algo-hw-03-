from pathlib import Path
import sys
from colorama import Fore

def list_directory_contents(directory_path):
    try:
        path = Path(directory_path)                           
        if path.exists():                                     # Перевірка чи існує файл/директорія
            if path.is_dir():                                 # Перевірка чи це директорія
                items = path.iterdir()                        # Метод який показує усе, що є у директорії
                for item in items:
                    print(f'{Fore.YELLOW} {item} {Fore.RESET}')
            else:
                print(f'{path} {Fore.GREEN}is a file{Fore.RESET}')
        else:
            print(f'{path.absolute()} {Fore.RED}does not exist{Fore.RESET}') 
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) < 2:                                      # Перевірка вводу. Чи ввів користувач шлях до директорії
        print(f"Usage:{Fore.LIGHTRED_EX} {sys.argv[0]} {Fore.RESET} <directory_path>") 
    else:
        user_input = sys.argv[1] 
        list_directory_contents(user_input)

if __name__ == "__main__":
    main()

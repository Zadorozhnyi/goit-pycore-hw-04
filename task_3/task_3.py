import sys
from pathlib import Path
from colorama import Fore, Style, init

# Initialize colorama library
init(autoreset=True)

def print_directory_structure(path, indent_level=0):
    try:
        p = Path(path)
        if not p.exists():
            print(f"{Fore.RED}Помилка: Шлях {path} не існує.")
            return
        if not p.is_dir():
            print(f"{Fore.RED}Помилка: Шлях {path} не є директорією.")
            return

        # Go through files and directories
        for item in p.iterdir():
            indent = "  " * indent_level
            if item.is_dir():
                # Display subdirectory in blue
                print(f"{indent}{Fore.BLUE}{item.name}/")
                # Recursively go through the subdirectory
                print_directory_structure(item, indent_level + 1) 
            else:
                # Display the files in green
                print(f"{indent}{Fore.GREEN}{item.name}")

    except Exception as e:
        print(f"{Fore.RED}Сталася помилка: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: не вказано шлях до директорії.")
    else:
        directory_path = sys.argv[1]
        print_directory_structure(directory_path)

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                # Receive developers salary from each line
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    # Skip lines with incorrect format
                    print (f"Рядок з неправильним форматом: [{line}]")
                    continue

            total = sum(salaries)
            average = total / len(salaries) if salaries else 0
            return int(total), int(average)

    except FileNotFoundError:
        print ("Файл не знайдено")
        return 0,0


total, average = total_salary("salary_file.txt")
print (f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

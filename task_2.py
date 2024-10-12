
def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Receive cat's id, name and age
                    cat_id, name, age = line.strip().split(',')
                    # Add dictionary with data about the cat
                    cats.append({"id": cat_id, "name": name.strip(), "age": int(age)})
                except ValueError:
                    # Skip lines with incorrect format
                    print (f"Рядок з неправильним форматом: [{line}]")
                    continue

        return cats

    except FileNotFoundError:
        print ("Файл не знайдено")
        return cats


cats_info = get_cats_info("cats_file.txt")
print (cats_info)

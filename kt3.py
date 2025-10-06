import csv
import os

# Функция для создания файла books.csv, если он не существует
def create_sample_books_file(filename):
    sample_data = """isbn|title|author|quantity|price
978-1-43545-500-9|Python Programming for the Absolute Beginner|Michael Dawson|10|18.90
978-0-59600-372-2|XSLT Cookbook|Sal Mangano|15|34.60
978-0-32168-056-3|Programming in Python 3|Mark Summerfield|8|27.28
978-1-44935-573-9|Learning Python|Mark Lutz|21|34.20
978-0-47178-597-2|Ajax For Dummies|Steve Holzner|32|11.80
978-1-78439-700-5|Mastering Python Networking|Eric Chou|23|31.49
978-8-59037-986-7|Programming in Lua|Roberto Ierusalimschy|12|37.10
978-1-78439-658-9|Machine Learning in Java|Bostjan Kaluza|45|34.99"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(sample_data)

# Задание 1: Чтение CSV файла и преобразование в список списков
def get_books(filename):
    if not os.path.exists(filename):
        create_sample_books_file(filename)
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)  # Пропускаем заголовок
        return list(map(lambda row: [
            row[0], 
            row[1], 
            row[2], 
            int(row[3]), 
            float(row[4])
        ], reader))

# Задание 2: Фильтрация книг по подстроке в названии и объединение title и author
def filtered_books(books, keyword):
    keyword_lower = keyword.lower()
    filtered = filter(lambda book: keyword_lower in book[1].lower(), books)
    return list(map(lambda book: [
        book[0], 
        f"{book[1]}, {book[2]}", 
        book[3], 
        book[4]
    ], filtered))

# Задание 3: Создание кортежей (isbn, quantity*price)
def calculate_totals(books):
    return list(map(lambda book: (book[0], book[2] * book[3]), books))

# Пример использования
if __name__ == "__main__":
    # Задание 1
    books = get_books("books.csv")
    print("Все книги:")
    print(*books, sep='\n')
    
    # Задание 2
    python_books = filtered_books(books, "python")
    print("\nКниги с 'python' в названии:")
    print(*python_books, sep='\n')
    
    # Задание 3
    totals = calculate_totals(python_books)
    print("\nСуммарная стоимость (количество * цена):")
    print(*totals, sep='\n')

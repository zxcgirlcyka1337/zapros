### Импорт модулей и класс Library
import sqlite3

class Library:
    ###происходит импорт модуля sqlite3, который используется для работы с базой данных sqlite и определение класса library
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()
        self.create_books_table()
        self.genres = ['Фантастика', 'Детектив', 'Роман']

        ### Метод create_books_table
    def create_books_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                description TEXT,
                genre TEXT
            )
        """)
        self.conn.commit()
### Метод add_book
    def add_book(self, title, author, description, genre):
        self.cursor.execute("""
            INSERT INTO books (title, author, description, genre)
            VALUES (?, ?, ?, ?)
        """, (title, author, description, genre))
        self.conn.commit()
        print(f'Книга "{title}" успешно добавлена в библиотеку!')
### Метод view_books
    def view_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()

        if len(books) == 0:
            print('В библиотеке нет книг.')
        else:
            print('Список книг в библиотеке:')
            for book in books:
                print(f'Название: {book[1]}, Автор: {book[2]}, Жанр: {book[4]}')

    def search_books(self, keyword):
        self.cursor.execute("""
            SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR description LIKE ?
        """, (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
        books = self.cursor.fetchall()

        if len(books) == 0:
            print(f'По запросу "{keyword}" ничего не найдено.')
        else:
            print(f'Результаты поиска по запросу "{keyword}":')
            for book in books:
                print(f'Название: {book[1]}, Автор: {book[2]}, Жанр: {book[4]}')

    def remove_book(self, title):
        self.cursor.execute("DELETE FROM books WHERE title = ?", (title,))
        self.conn.commit()
        print(f'Книга "{title}" успешно удалена из библиотеки!')

    def close_connection(self):
        self.conn.close()

def main():
    library = Library()

    while True:
        print('Меню:')
        print('1. Добавить новую книгу')
        print('2. Просмотреть список книг')
        print('3. Поиск книги по ключевому слову')
        print('4. Удалить книгу')
        print('0. Выход из программы')

        choice = input('Сделайте выбор: ')

        if choice == '1':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            description = input('Введите описание книги: ')
            genre = input('Введите жанр книги: ')
            library.add_book(title, author, description, genre)

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            keyword = input('Введите ключевое слово для поиска: ')
            library.search_books(keyword)
        
        elif choice == '4':
            title = input('Введите название книги для удаления: ')
            library.remove_book(title)

        elif choice == '0':
            print('Выход из программы.')
            library.close_connection()
            break

        else:
            print('Некорректный ввод. Попробуйте снова.')


if __name__ == '__main__':
    main()

# Определяем класс Book для представления отдельной книги
class Book:
    def __init__(self, title, author, description, genre):
        self.title = title
        self.author = author
        self.description = description
        self.genre = genre

# Определяем класс Library для управления книгами в библиотеке
class Library:
    def __init__(self):
        self.books = []  # Инициализируем пустой список книг
        self.genres = ['Фантастика', 'Детектив', 'Роман']  # Заранее заданные жанры

    # Метод для добавления новой книги
    def add_book(self, title, author, description, genre):
        new_book = Book(title, author, description, genre)  # Создаем новый экземпляр Book
        self.books.append(new_book)  # Добавляем книгу в список книг
        print(f'Книга "{title}" успешно добавлена!')

    # Метод для просмотра всех книг
    def view_books(self):
        if len(self.books) == 0:
            print('В библиотеке нет книг.')
        else:
            print('Список книг в библиотеке:')
            for book in self.books:
                print(f'Название: {book.title}, Автор: {book.author}')

    # Метод для просмотра подробной информации о книге
    def view_book_details(self, title):
        for book in self.books:
            if book.title == title:
                print('Подробная информация о книге:')
                print(f'Название: {book.title}')
                print(f'Автор: {book.author}')
                print(f'Описание: {book.description}')
                print(f'Жанр: {book.genre}')
                return
        print(f'Книга с названием "{title}" не найдена.')

    # Метод для вывода книг определенного жанра
    def view_books_by_genre(self, genre):
        print(f'Список книг в жанре "{genre}":')
        found_books = []
        for book in self.books:
            if book.genre == genre:
                found_books.append(book)
                print(f'Название: {book.title}, Автор: {book.author}')
        if len(found_books) == 0:
            print(f'Книги в жанре "{genre}" не найдены.')

    # Метод для поиска книги по ключевому слову
    def search_books(self, keyword):
        print(f'Результаты поиска по ключевому слову "{keyword}":')
        found_books = []
        for book in self.books:
            if keyword in book.title or keyword in book.author:
                found_books.append(book)
                print(f'Название: {book.title}, Автор: {book.author}')
        if len(found_books) == 0:
            print('Книги с данным ключевым словом не найдены.')

    # Метод для удаления книги
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Книга "{title}" успешно удалена!')
                return
        print(f'Книга с названием "{title}" не найдена.')


# Функция для запуска программы
def main():
    library = Library()
    choice = ''
    while choice != '0':
        print('Выберите действие:')
        print('1. Добавить новую книгу')
        print('2. Просмотреть список книг')
        print('3. Просмотреть подробную информацию о книге')
        print('4. Вывести книги определенного жанра')
        print('5. Поиск книги по ключевому слову')
        print('6. Удалить книгу')
        print('0. Выйти')

        choice = input('Введите номер действия: ')

        if choice == '1':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            description = input('Введите описание книги: ')
            print('Доступные жанры:', library.genres)
            genre = input('Введите жанр книги или введите новый жанр: ')
            library.add_book(title, author, description, genre)

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            title = input('Введите название книги для просмотра подробной информации: ')
            library.view_book_details(title)

        elif choice == '4':
            genre = input('Введите жанр книги: ')
            library.view_books_by_genre(genre)

        elif choice == '5':
            keyword = input('Введите ключевое слово для поиска: ')
            library.search_books(keyword)

        elif choice == '6':
            title = input('Введите название книги для удаления: ')
            library.remove_book(title)

        elif choice == '0':
            print('Выход из программы.')
            break

        else:
            print('Некорректный ввод. Попробуйте снова.')


if __name__ == '__main__':
    main()

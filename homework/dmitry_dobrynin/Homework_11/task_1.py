# Первая часть задания


class Book:
    material = "бумага"
    is_text = True

    def __init__(self, title, author, count_page, ISBN, is_reserved=False):
        self.title = title
        self.author = author
        self.count_page = count_page
        self.ISBN = ISBN
        self.is_reserved = is_reserved


first = Book("Идиот", "Достоевский", 500, 9781234567897)
second = Book("Мастер и Маргарита", "Булгаков", 480, 9780451525022)
third = Book("Гарри Поттер и философский камень", "Роулинг", 352, 9780747532743)
fourth = Book("1984", "Оруэлл", 328, 9780451524935, True)
fifth = Book("Война и мир", "Толстой", 1225, 9780192833983)
books = [first, second, third, fourth, fifth]


for book in books:
    text = (
        f"Название: {book.title}, "
        f"Автор: {book.author}, "
        f"страниц: {book.count_page}, "
        f"материал: {book.material}"
    )

    if book.is_reserved:
        text += ", зарезервирована"

    print(text)


#  Вторая часть задания


class SchoolBook(Book):
    def __init__(
        self, title, author, count_page, ISBN, item, group, is_task, is_reserved=False
    ):
        super().__init__(title, author, count_page, ISBN, is_reserved)
        self.item = item
        self.group = group
        self.is_task = is_task


matan = SchoolBook(
    "Алгебра", "Иванов", 97812342567897, 200, "Математика", 9, True, True
)
fizika = SchoolBook("Физика", "Петров", 250, 97812334567897, "Физика", 8, False, False)
geometry = SchoolBook(
    "Геометрия", "Иванов", 97812234567897, 220, "Математика", 9, True, False
)
items_books = [matan, fizika, geometry]

for book in items_books:
    text = (
        f"Название: {book.title}, "
        f"Автор: {book.author}, "
        f"страниц: {book.count_page}, "
        f"предмет: {book.item}, "
        f"класс: {book.group}"
    )

    if book.is_reserved:
        text += ", зарезервирована"

    print(text)

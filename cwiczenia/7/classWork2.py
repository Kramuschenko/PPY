import tkinter as tk
from tkinter import ttk
import mysql.connector

root = tk.Tk()
root.title("Book Store")
root.iconbitmap("./bookshelf.ico")
#Pobranie danych z tabeli
def fetch_data():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="kramushchanka",
        password="123rh456",
        database="s24124_python_7")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM books")
    result = mycursor.fetchall()
    mycursor.close()  # Zamknięcie kursora
    mydb.close()  # Zamknięcie połączenia
    return result


# Utworzenie widżetu Treeview
treeview = ttk.Treeview(root)
treeview["columns"] = ("id", "title", "author", "price", "category")
treeview.column("#0", width=0)
treeview.heading("id", text="ID")
treeview.heading("title", text="Tytuł")
treeview.heading("author", text="Autor")
treeview.heading("price", text="Cena")
treeview.heading("category", text="Kategoria")
# Wyświetlenie widżetu Treeview
treeview.pack()


def load_data():
    data = fetch_data()
    # Usunięcie poprzednich danych
    treeview.delete(*treeview.get_children())
    # Dodanie nowych danych
    for row in data:
        treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))


def open_new_book_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj nową książkę")
    title_label = ttk.Label(new_window, text="Tytuł:")
    title_label.pack()
    title_entry = ttk.Entry(new_window)
    title_entry.pack()
    author_label = ttk.Label(new_window, text="Autor:")
    author_label.pack()
    author_entry = ttk.Entry(new_window)
    author_entry.pack()
    price_label = ttk.Label(new_window, text="Cena:")
    price_label.pack()
    price_entry = ttk.Entry(new_window)
    price_entry.pack()
    category_label = ttk.Label(new_window, text="Kategoria:")
    category_label.pack()
    category_entry = ttk.Entry(new_window)
    category_entry.pack()

    def add_new():
        new_title = title_entry.get()
        new_author = author_entry.get()
        new_price = price_entry.get()
        new_category = category_entry.get()
        mydb = mysql.connector.connect(
            host="db4free.net",
            user="kramushchanka",
            password="123rh456",
            database="s24124_python_7"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO books (title, author, price, category) VALUES (%s, %s, %s, %s)"
        params = (new_title, new_author, new_price, new_category)
        mycursor.execute(sql, params)
        mydb.commit()
        # Zapisanie zmian w bazie
        mycursor.close()
        # Zamknięcie kursora
        mydb.close()
        # Zamknięcie połączenia
        load_data()
        # Zamknięcie okna po zapisaniu zmian
        new_window.destroy()

    add_button = ttk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()


add_new_book_button = tk.Button(root, text="Dodaj nową książkę", command=open_new_book_window)
add_new_book_button.pack(side="left")

# Wywołanie funkcji wczytującej dane
load_data()
root.mainloop()


if __name__ == "__main__":
    print("Start app")

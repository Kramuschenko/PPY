import sqlite3
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Students")
root.iconbitmap("./bookshelf.ico")


#Pobranie danych z tabeli
def fetch_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student")
    result = cursor.fetchall()
    cursor.close()  # Zamknięcie kursora
    cursor.close()  # Zamknięcie połączenia
    return result


# Utworzenie widżetu Treeview
treeview = ttk.Treeview(root)
treeview["columns"] = ("id", "mail", "imie", "nazwisko",
                       "project", "lista1", "lista2", "lista3",
                       "hw1", "hw2", "hw3", "hw4", "hw5", "hw6", "hw7", "hw8", "hw9", "hw10",
                       "grade", "status")
treeview.column("#0", width=0)
treeview.heading("id", text="ID")
treeview.heading("mail", text="Mail")
treeview.heading("imie", text="Imie")
treeview.heading("nazwisko", text="Nazwisko")
treeview.heading("project", text="Projekt")
treeview.heading("lista1", text="Lista 1")
treeview.heading("lista2", text="Lista 2")
treeview.heading("lista3", text="Lista 3")
treeview.heading("hw1", text="Zad 1")
treeview.heading("hw2", text="Zad 2")
treeview.heading("hw3", text="Zad 3")
treeview.heading("hw4", text="Zad 4")
treeview.heading("hw5", text="Zad 5")
treeview.heading("hw6", text="Zad 6")
treeview.heading("hw7", text="Zad 7")
treeview.heading("hw8", text="Zad 8")
treeview.heading("hw9", text="Zad 9")
treeview.heading("hw10", text="Zad 10")
treeview.heading("grade", text="Ocena końcowa")
treeview.heading("status", text="Status")
# Wyświetlenie widżetu Treeview
treeview.pack()


def load_data():
    data = fetch_data()
    # Usunięcie poprzednich danych
    treeview.delete(*treeview.get_children())
    # Dodanie nowych danych
    for row in data:
        treeview.insert("", "end", values=(row[0], row[1], row[2], row[3]
                                           , row[4], row[5], row[6]
                                           , row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16]
                                           , row[17], row[18], row[19]))


def create_student(mail, imie, nazwisko, project, lista1, lista2, lista3, hw1, hw2, hw3, hw4, hw5, hw6, hw7, hw8, hw9, hw10, grade, status):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Student (mail, imie, nazwisko, project, lista1, lista2, lista3, hw1, hw2, hw3, hw4, hw5, hw6, hw7, hw8, hw9, hw10, grade, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                       , (mail, imie, nazwisko, project, lista1, lista2, lista3, hw1, hw2, hw3, hw4, hw5, hw6, hw7, hw8, hw9, hw10, grade, status))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def open_new_student_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj nowego studenta")
    mail_label = ttk.Label(new_window, text="Mail:")
    mail_label.pack()
    mail_entry = ttk.Entry(new_window)
    mail_entry.pack()
    name_label = ttk.Label(new_window, text="Imie:")
    name_label.pack()
    name_entry = ttk.Entry(new_window)
    name_entry.pack()
    surname_label = ttk.Label(new_window, text="Nazwisko:")
    surname_label.pack()
    surname_entry = ttk.Entry(new_window)
    surname_entry.pack()
    project_label = ttk.Label(new_window, text="Ocena projektu:")
    project_label.pack()
    project_entry = ttk.Entry(new_window)
    project_entry.pack()
    list_label = ttk.Label(new_window, text="Ocena list:")
    list_label.pack()
    list_entry = ttk.Entry(new_window)
    list_entry.pack()
    hw_label = ttk.Label(new_window, text="Ocena zadań domowych:")
    hw_label.pack()
    hw_entry = ttk.Entry(new_window)
    hw_entry.pack()
    final_grade_label = ttk.Label(new_window, text="Ocena końcowa:")
    final_grade_label.pack()
    final_grade_entry = ttk.Entry(new_window)
    final_grade_entry.pack()
    status_label = ttk.Label(new_window, text="Status:")
    status_label.pack()
    status_entry = ttk.Entry(new_window)
    status_entry.pack()

    def add_new():
        new_mail = mail_entry.get()
        new_name = name_entry.get()
        new_surname = surname_entry.get()
        new_project = project_entry.get()
        new_list_grades = list_entry.get().split(",")
        new_hw_grades = hw_entry.get().split(",")
        new_final_grade = final_grade_entry.get()
        new_status = status_entry.get()
        create_student(new_mail, new_name, new_surname, new_project
                       , new_list_grades[0], new_list_grades[1], new_list_grades[2],
                       new_hw_grades[0], new_hw_grades[1], new_hw_grades[2], new_hw_grades[3], new_hw_grades[4],
                       new_hw_grades[5], new_hw_grades[6], new_hw_grades[7], new_hw_grades[8], new_hw_grades[9],
                       new_final_grade, new_status)

        # Zamknięcie połączenia
        load_data()
        # Zamknięcie okna po zapisaniu zmian
        new_window.destroy()

    add_button = ttk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()


add_student_button = tk.Button(root, text="Dodaj nowego studenta", command=open_new_student_window)
add_student_button.pack(side="left")


def update_student(id, mail, imie, nazwisko, project, lista1, lista2, lista3, hw1, hw2, hw3, hw4, hw5, hw6, hw7, hw8, hw9, hw10, grade, status):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE STUDENT SET mail = ?, imie = ?, nazwisko = ?, project = ?, lista1 = ?, lista2 = ?, lista3 = ?, hw1 = ?, hw2 = ?, hw3 = ?, hw4 = ?, hw5 = ?, hw6 = ?, hw7 = ?, hw8 = ?, hw9 = ?, hw10 = ?, grade = ?, status = ?  WHERE id = ? "
                       , (mail, imie, nazwisko, project, lista1, lista2, lista3, hw1, hw2, hw3, hw4, hw5, hw6, hw7, hw8, hw9, hw10, grade, status, id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def update_student_window():
    new_window = tk.Toplevel(root)
    new_window.title("Zmień studenta")
    id_label = ttk.Label(new_window, text="ID:")
    id_label.pack()
    id_entry = ttk.Entry(new_window)
    id_entry.pack()
    mail_label = ttk.Label(new_window, text="Mail:")
    mail_label.pack()
    mail_entry = ttk.Entry(new_window)
    mail_entry.pack()
    name_label = ttk.Label(new_window, text="Imie:")
    name_label.pack()
    name_entry = ttk.Entry(new_window)
    name_entry.pack()
    surname_label = ttk.Label(new_window, text="Nazwisko:")
    surname_label.pack()
    surname_entry = ttk.Entry(new_window)
    surname_entry.pack()
    project_label = ttk.Label(new_window, text="Ocena projektu:")
    project_label.pack()
    project_entry = ttk.Entry(new_window)
    project_entry.pack()
    list_label = ttk.Label(new_window, text="Ocena list:")
    list_label.pack()
    list_entry = ttk.Entry(new_window)
    list_entry.pack()
    hw_label = ttk.Label(new_window, text="Ocena zadań domowych:")
    hw_label.pack()
    hw_entry = ttk.Entry(new_window)
    hw_entry.pack()
    final_grade_label = ttk.Label(new_window, text="Ocena końcowa:")
    final_grade_label.pack()
    final_grade_entry = ttk.Entry(new_window)
    final_grade_entry.pack()
    status_label = ttk.Label(new_window, text="Status:")
    status_label.pack()
    status_entry = ttk.Entry(new_window)
    status_entry.pack()

    def add_new():
        new_id = id_entry.get()
        new_mail = mail_entry.get()
        new_name = name_entry.get()
        new_surname = surname_entry.get()
        new_project = project_entry.get()
        new_list_grades = list_entry.get().split(",")
        new_hw_grades = hw_entry.get().split(",")
        new_final_grade = final_grade_entry.get()
        new_status = status_entry.get()
        update_student(new_id, new_mail, new_name, new_surname, new_project
                       , new_list_grades[0], new_list_grades[1], new_list_grades[2],
                       new_hw_grades[0], new_hw_grades[1], new_hw_grades[2], new_hw_grades[3], new_hw_grades[4],
                       new_hw_grades[5], new_hw_grades[6], new_hw_grades[7], new_hw_grades[8], new_hw_grades[9],
                       new_final_grade, new_status)

        # Zamknięcie połączenia
        load_data()
        # Zamknięcie okna po zapisaniu zmian
        new_window.destroy()

    add_button = ttk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()


update_student_button = tk.Button(root, text="Zmień studenta", command=update_student_window)
update_student_button.pack(side="left")


def remove_student_window():
    new_window = tk.Toplevel(root)
    new_window.title("Usuń studenta")
    id_label = ttk.Label(new_window, text="Id:")
    id_label.pack()
    id_entry = ttk.Entry(new_window)
    id_entry.pack()

    def add_new():
        remove_by_id = id_entry.get()

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Student WHERE id = ?"
                , (remove_by_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        # Zamknięcie połączenia
        load_data()
        # Zamknięcie okna po zapisaniu zmian
        new_window.destroy()

    add_button = ttk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()


remove_student_button = tk.Button(root, text="Usuń studenta", command=remove_student_window)
remove_student_button.pack(side="left")

# Wywołanie funkcji wczytującej dane
load_data()
root.mainloop()


if __name__ == "__main__":
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Student 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                mail TEXT,
                imie TEXT,
                nazwisko TEXT,
                project REAL,
                lista1 REAL,
                lista2 REAL,
                lista3 REAL,
                hw1 REAL,
                hw2 REAL,
                hw3 REAL,
                hw4 REAL,
                hw5 REAL,
                hw6 REAL,
                hw7 REAL,
                hw8 REAL,
                hw9 REAL,
                hw10 REAL,
                grade REAL,
                status TEXT)''')
    conn.commit()
    conn.close()

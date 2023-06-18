import sqlite3
import tkinter as tk
import warnings
from tkinter import messagebox
from tkinter import ttk

import joblib
import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore", category=matplotlib.MatplotlibDeprecationWarning)

df = None
headers = ["Id number", "RI", "Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe", "Type of glass"]

# Podziel dane na cechy (X) i etykiety (y)
X = None
y = None

# Podziel dane na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = None, None, None, None

# Połączenie z bazą danych SQLite
conn = sqlite3.connect('glass_data.db')
cursor = conn.cursor()

# Utworzenie tabeli w bazie danych
create_table_query = """
CREATE TABLE IF NOT EXISTS glass (
    id INTEGER PRIMARY KEY,
    RI REAL,
    Na REAL,
    Mg REAL,
    Al REAL,
    Si REAL,
    K REAL,
    Ca REAL,
    Ba REAL,
    Fe REAL,
    glass_type INTEGER
)
"""
cursor.execute(create_table_query)


def load_data_online():
    global df, X, y, X_train, X_test, y_train, y_test

    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data"

    df = pd.read_csv(url, names=headers)

    # Podziel dane na cechy (X) i etykiety (y)
    X = df.drop("Type of glass", axis=1)
    y = df["Type of glass"]

    # Podziel dane na zbiór treningowy i testowy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


def save_data_to_db():
    data = X.copy()
    data["Type of glass"] = y
    data.to_sql('glass', conn, if_exists='replace', index=False)
    messagebox.showinfo("Zapisano dane", "Dane zostały zapisane w bazie SQLite.")


def load_data_from_db():
    global df, X, y, X_train, X_test, y_train, y_test

    query = 'SELECT * FROM glass'
    df = pd.read_sql(query, conn)

    # Podziel dane na cechy (X) i etykiety (y)
    X = df.drop("Type of glass", axis=1)
    y = df["Type of glass"]

    # Podziel dane na zbiór treningowy i testowy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    messagebox.showinfo("Wczytano dane", "Dane zostały wczytane z bazy SQLite.")


def train_model():
    global model

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    messagebox.showinfo("Model trenowany", f"Dokładność modelu: {accuracy}")


def predict_new_data():
    new_data_str = new_data_entry.get()
    new_data_list = list(map(float, new_data_str.split(",")))
    new_data_df = pd.DataFrame([new_data_list], columns=X.columns)
    prediction = model.predict(new_data_df)
    messagebox.showinfo("Predykcja dla nowych danych", f"Wynik predykcji: {prediction}")


def save_model():
    joblib.dump(model, "model.pkl")
    messagebox.showinfo("Zapisano model", "Model został zapisany na dysku.")


def load_model():
    global model
    model = joblib.load("model.pkl")
    messagebox.showinfo("Wczytano model", "Model został wczytany z dysku.")


# Tworzenie wykresu dla analizy typów szkła
def create_glass_type_analysis_plots():
    num_features = len(X.columns)
    fig, axes = plt.subplots(nrows=num_features, ncols=1, figsize=(8, num_features * 4))

    for i, feature in enumerate(X.columns):
        ax = axes[i]
        ax.scatter(X[feature], y, c=y)
        ax.set_xlabel(feature)
        ax.set_ylabel("Type of glass")
        ax.set_title(f"Analysis of Glass Types based on {feature}")

    plt.tight_layout()
    return fig


# Generowanie pliku PDF z wykresami
def generate_pdf():
    with PdfPages("wykresy.pdf") as pdf:
        fig = create_glass_type_analysis_plots()
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()
        pdf.savefig(fig)
        plt.close(fig)


def refresh_data():
    for index, row in df.iterrows():
        data_table.insert("", "end", text=index, values=row.tolist())


# Uruchomienie pętli głównej aplikacji
if __name__ == "__main__":
    # Tworzenie głównego okna
    window = tk.Tk()
    window.title("Aplikacja ML")
    window.geometry("900x700")

    # Przyciski i pola tekstowe
    button_frame_data = tk.Frame(window)
    button_frame_data.pack(pady=10)

    load_data_online_button = tk.Button(button_frame_data, text="Wczytaj dane z internetu", command=load_data_online)
    load_data_online_button.pack(side=tk.LEFT, padx=5)

    save_data_button = tk.Button(button_frame_data, text="Zapisz dane do bazy", command=save_data_to_db)
    save_data_button.pack(side=tk.LEFT, padx=5)

    load_data_button = tk.Button(button_frame_data, text="Wczytaj dane z bazy", command=load_data_from_db)
    load_data_button.pack(side=tk.LEFT, padx=5)

    button_frame_model = tk.Frame(window)
    button_frame_model.pack(pady=10)

    train_button = tk.Button(button_frame_model, text="Trenuj model", command=train_model)
    train_button.pack(side=tk.LEFT, padx=5)

    save_model_button = tk.Button(button_frame_model, text="Zapisz model", command=save_model)
    save_model_button.pack(side=tk.LEFT, padx=5)

    load_model_button = tk.Button(button_frame_model, text="Wczytaj model", command=load_model)
    load_model_button.pack(side=tk.LEFT, padx=5)

    new_data_label = tk.Label(window, text="Nowe dane (oddzielone przecinkami \n "
                                           "n.p. '1,1.5,2.7,1.8,1.2,1.9,0.5,1.2,0.3,0.1'):")
    new_data_label.pack()
    new_data_entry = tk.Entry(window)
    new_data_entry.pack()

    predict_button = tk.Button(window, text="Predykcja dla nowych danych", command=predict_new_data)
    predict_button.pack(pady=10)

    pdf_button = tk.Button(window, text="Generuj PDF", command=generate_pdf)
    pdf_button.pack(pady=10)

    refresh_button = tk.Button(window, text="Refresh", command=refresh_data)
    refresh_button.pack(pady=10)

    # Tabelka do przeglądania danych
    data_table = ttk.Treeview(window)
    data_table["columns"] = headers
    data_table.pack(pady=10)

    # Ustawienie nagłówków tabeli
    for header in headers:
        data_table.heading(header, text=header)

    # Ustawienie szerokości kolumn
    column_widths = [50, 80, 60, 60, 60, 60, 60, 60, 60, 60, 80]  # lista szerokości kolumn
    for header, width in zip(headers, column_widths):
        data_table.column(header, width=width)

    window.mainloop()

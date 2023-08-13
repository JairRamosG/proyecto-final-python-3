# %%
import sqlite3
import csv

def create_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS info_dia(
        id INTEGER PRIMARY KEY,
        region VARCHAR (30) NOT NULL,
        generacion FLOAT NOT NULL,
        demanda FLOAT NOT NULL,
        diferencia FLOAT NOT NULL,
        fecha smalldatetime NOT NULL, 
        hora INTEGER NOT NULL
        )
        """)
    conn.commit()
    conn.close()

def read_csv(csv_file):
    with open(csv_file, newline="") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def insert_data_to_table(data):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    for row in data:
        cursor.execute(
            """
            INSERT INTO info_dia(region, generacion, demanda, diferencia, fecha, hora)
            VALUES(?,?,?,?,?,?)
            """, (row['region'], row['generacion'], row['demanda'], row['diferencia'], row['fecha'], row['hora'])
            )
    conn.commit()
    conn.close()
# %%
if __name__ == "__main__":
    create_table()
# %%
if __name__ == "__main__":
    csv_file = "base_de_datos.csv"
    data_to_insert = read_csv(csv_file)
    insert_data_to_table(data_to_insert)

# %%

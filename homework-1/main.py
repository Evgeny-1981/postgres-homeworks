# """Скрипт для заполнения данными таблиц в БД Postgres."""
import os
import pandas as pd
import psycopg2

# """задаем параметры для подключения к БД."""
conn_params = {
    'dbname': 'north',
    'user': 'postgres',
    'password': '1238',
}

with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        # Считываем данные из файла CSV
        file1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'north_data', "customers_data.csv"))
        file2 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'north_data', "employees_data.csv"))
        file3 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'north_data', "orders_data.csv"))
        # data_files = (file1, file2, file3)
        # Заполнение таблицы данными
        for row in file1.values:
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
        for row in file2.values:
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
        for row in file3.values:
            cur.execute("INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)", row)
    cur.close()
conn.commit()

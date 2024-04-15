import psycopg2

# Подключаемся к базе данных
conn = psycopg2.connect(
    dbname="north",
    user="postgres",
    password="1238",
)
# Создаем объект-курсор для выполнения SQL-запросов
cur = conn.cursor()

# Выполняем SQL-запрос для получения списка таблиц
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

# Получаем результат запроса
tables = cur.fetchall()

# Выводим список таблиц
list_tabl = []
for table in tables:
    list_tabl.append(table[0])
print(list_tabl)
# Закрываем курсор и соединение с базой данных
cur.close()
conn.close()

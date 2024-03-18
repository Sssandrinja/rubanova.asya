import tabletka


table = tabletka.load_table_csv("data.csv")
print(table)
tabletka.save_table_csv(table, "data2.csv")
# table2 = tabletka.load_table_pickle("data.pickle")
# print(table2)
# tabletka.save_table_pickle("data2.pickle")
tabletka.save_table_text(table, "data.txt")
# print(tabletka.get_rows_by_number(1, None, True))

"""Тесты для исключительных случаев"""
# Чтобы протестировать функции - надо создать файлы в директории программы, названия которых приведены ниже

# Тестирование исключения FileNotFoundError для функции load_table_csv
try:
    table = tabletka.load_table_csv("nonexistent_file.csv")
except FileNotFoundError as e:
    print(e)

# Тестирование исключения ValueError для функции load_table_csv
try:
    table = tabletka.load_table_csv("invalid_format.xsl")
except ValueError as e:
    print(e)

# Тестирование исключения ValueError для функции save_table_csv
try:
    table = {"Name": ["Sasha", "Kate"], "Age": [18, 19, 35]}
    tabletka.save_table_csv(table, "invalid_table.csv")
except ValueError as e:
    print(e)

# Тестирование исключения FileNotFoundError для функции load_table_pickle
try:
    table = tabletka.load_table_pickle("nonexistent_file.pickle")
except FileNotFoundError as e:
    print(e)

# Тестирование исключения ValueError для функции load_table_pickle
try:
    table = tabletka.load_table_pickle("invalid_format.pickle")
except ValueError as e:
    print(e)

# Тестирование исключения ValueError для функции save_table_pickle
try:
    table = {"Name": ["Sasha", "Kate"], "Age": [18, 19, 35]}
    tabletka.save_table_pickle(table, "invalid_table.pickle")
except ValueError as e:
    print(e)

# Тестирование исключения ValueError для функции save_table_text
try:
    table = {"Name": ["Sasha", "Kate"], "Age": [18, 19, 35]}
    tabletka.save_table_text(table, "invalid_table.txt")
except ValueError as e:
    print(e)

# Тесты для функции get_rows_by_number
# 1. Попытка получить строки с некорректными номерами
tabletka.get_rows_by_number(-1)  # Ожидаемое исключение: ValueError
tabletka.get_rows_by_number(10, 5)  # Ожидаемое исключение: ValueError

# Тесты для функции get_rows_by_index
# 2. Попытка получить строки с некорректными значениями
tabletka.get_rows_by_index('abc', 'def')  # Ожидаемое исключение: TypeError
tabletka.get_rows_by_index()  # Ожидаемое исключение: TypeError

# Тесты для функции get_column_types
# 3. Попытка получить типы столбцов при некорректном аргументе
tabletka.get_column_types('abc')  # Ожидаемое исключение: TypeError

# Тесты для функции set_column_types
# 4. Попытка задать типы столбцов с некорректным аргументом
tabletka.set_column_types('abc')  # Ожидаемое исключение: TypeError

# Тесты для функции get_values
# 5. Попытка получить значения из несуществующего столбца
tabletka.get_values(10)  # Ожидаемое исключение: IndexError
tabletka.get_values('column')  # Ожидаемое исключение: KeyError

# Тесты для функции get_value
# 6. Попытка получить значение из несуществующего столбца
tabletka.get_value(10)  # Ожидаемое исключение: IndexError
tabletka.get_value('column')  # Ожидаемое исключение: KeyError
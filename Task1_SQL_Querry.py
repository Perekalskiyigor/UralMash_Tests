import sqlite3

# создаем соединение с базой данных
conn = sqlite3.connect('test.db')

# создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# создаем таблицу
cursor.execute('CREATE TABLE test_table (data TEXT)')

# наполняем таблицу данными
data = [('gsregtgs',), ('tgergegeer',), ('gregeg',)]
cursor.executemany('INSERT INTO test_table VALUES (?)', data)

# сохраняем изменения и закрываем соединение
conn.commit()
conn.close()






"""
Для подсчета количества вхождений символа или подстроки в заданной строке на любом SQL-диалекте можно использовать функцию CHARINDEX или INSTR (в зависимости от диалекта), которая возвращает позицию первого вхождения указанного символа или подстроки в строку.
"""


"""Для подсчета количества вхождений символа можно использовать следующий SQL-запрос:"""
querry = "SELECT (LEN(your_column) - LEN(REPLACE(your_column, 'your_substring', ''))) / LEN('your_substring') AS count FROM your_table;"


"""Здесь your_column - это название столбца, содержащего строковые данные, а your_char - это символ, который нужно подсчитать. Функция REPLACE заменяет все вхождения указанного символа на пустую строку, а функция LEN возвращает длину строки. Таким образом, разница между длиной исходной строки и длиной строки, в которой все вхождения символа заменены на пустую строку, равна количеству вхождений символа."""


querry2 = "SELECT (LEN(your_column) - LEN(REPLACE(your_column, 'your_substring', ''))) / LEN('your_substring') AS count FROM your_table;"

"""Здесь your_substring - это подстрока, которую нужно подсчитать. Разность между длиной исходной строки и длиной строки, в которой все вхождения подстроки заменены на пустую строку, делится на длину подстроки, что дает количество вхождений подстроки."""
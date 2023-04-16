# UralMash_Tests

Запустить Git Bash Клонировать репозиторий и перейти в него в командной строке Git Bash: git clone https://github.com/Perekalskiyigor/UralMash_Tests.git

Cоздать и активировать виртуальное окружение: на Mac или Linux: python3 -m venv env source env/bin/activate для Windows: python -m venv venv source venv/Scripts/activate Обновляем pip на Mac или Linux: python3 -m pip install --upgrade pip для Windows: python -m pip install --upgrade pip

Установить зависимости из файла requirements.txt: pip install -r requirements.txt:

Задание 1 
SQL. Как подсчитать, сколько раз символ
встречается в строке
*
Требуется подсчитать, сколько раз символ или подстрока встречаются
в заданной строке. 
На любом sql-"диалекте"

РЕШЕНИЕ
1. Запустите на исполнение файл Task1SQL. 
2. Окроется окно куда необходимо ввести искомую комбинацию и нажать кнопку Выполнить.
В ходе выполнения запроса программа обратиться к созданной тестовой БД test.db, данная бд исключена из git ignore и копируется с проектом.
3. Для наполнения бд можно воспользоваться скриптом написанным и закомментированном в теле программы (Нааполнение тестовой БД)
4. Результат работы программы будет выведен в label ниже
для Подсчета количества вхождений подстроки
для Подсчет количества вхождений символа


Задание 2
Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
Кодирование строки осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

РЕШЕНИЕ
1. Для задания 2 создан отдельный каталог с 3 вариантами решения Task2_crypt_v2.py, Task2_crypt_v3.py, Task2_crypt.py
2. На все решения создан интерфейс где необходимо внести кодируемую комбинацию и нажать кнопку "Выполнить"
3. Рзультат будет выведен в label
Для программы начал писать тесты (пока в процессе), файл test



Задание 3
Flutter
*
Предлагаю попробовать себя во Flutter.
Соберите самый простой проект на Flutter под Android  и Web. Достаточно 2-3 страниц. 
Результат покажите ссылкой на  github.

РЕШЕНИЕ
1. В разаработке

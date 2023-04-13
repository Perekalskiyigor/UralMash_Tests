from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sqlite3

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # создаем виджеты для ввода и вывода данных
        self.label = QLabel('Введите значение:', self)
        self.label.move(20, 20)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(140, 20)

        self.button = QPushButton('Выполнить', self)
        self.button.move(20, 60)

        self.result_label = QLabel(self)
        self.result_label.move(20, 100)

        self.result_label1 = QLabel(self)
        self.result_label1.move(20, 110)

        self.result_label2 = QLabel(self)
        self.result_label2.move(20, 130)

    
        # подключаем обработчик нажатия кнопки
        self.button.clicked.connect(self.execute_query)

        # создаем соединение с базой данных
        self.conn = sqlite3.connect('test.db')

    
    def execute_query(self):
        # получаем введенное значение из поля ввода
        data = self.line_edit.text()

        # создаем курсор для выполнения SQL-запросов
        cursor = self.conn.cursor()

        # cursor.execute('''CREATE TABLE IF NOT EXISTS test_table
        #         (data TEXT)''')
        
        # # наполняем таблицу данными
        # data = [('gsregtgs',), ('tgergegeer',), ('gregeg',)]
        # cursor.executemany('INSERT INTO test_table VALUES (?)', data)

        # выполняем запрос
        # cursor.execute("SELECT * FROM test_table WHERE text_field=?", (data,))
        """Для подсчета количества вхождений символа можно использовать следующий SQL-запрос:"""
        cursor.execute(f"SELECT text_field,LENGTH(text_field) - LENGTH(REPLACE(text_field, '{data}', '')) AS count FROM test_table;")

        # получаем результат запроса
        result = cursor.fetchall()
        second_elements = [t[1] for t in result]
        sumelements = sum(second_elements)
        print (sumelements)
        #print(result)

        # отображаем результат на экране
        if result:
            self.result_label1.setText('символов: ' + str(sumelements))
        else:
            self.result_label1.setText('Вхождений не найдено')

        """Для подсчета количества вхождений подстроки"""
        cursor.execute(f"SELECT COUNT(*) as occurrences FROM test_table WHERE text_field LIKE '%{data}%'")

        # получаем результат запроса
        result = cursor.fetchall()
        second_elements = result[0]
        second_elements = second_elements[0]

        # отображаем результат на экране
        if result:
            self.result_label2.setText('подстроки: ' + str(second_elements))
        else:
            self.result_label2.setText('Вхождений не найдено')

    def closeEvent(self, event):
        # закрываем соединение с базой данных при закрытии окна
        self.conn.close()

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
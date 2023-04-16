from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sqlite3

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(400,500,300,300)
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

    
        # Обработчики
        self.button.clicked.connect(self.execute_query)
        # База данных
        self.conn = sqlite3.connect('test.db')

    
    def execute_query(self):
        """Функция обработчик кнопки"""
        data = self.line_edit.text()
        cursor = self.conn.cursor()

        # Нааполнение тестовой БД

        # cursor.execute('''CREATE TABLE IF NOT EXISTS test_table
        #         (data TEXT)''')
        
        # data = [('gsregtgs',), ('tgergegeer',), ('gregeg',)]
        # cursor.executemany('INSERT INTO test_table VALUES (?)', data)

        # cursor.execute("SELECT * FROM test_table WHERE text_field=?", (data,))
        
        """Подсчет количества вхождений символа """
        cursor.execute(f"SELECT text_field,LENGTH(text_field) - LENGTH(REPLACE(text_field, '{data}', '')) AS count FROM test_table;")

        # Обработка результатов запроса
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

        """Подсчет количества вхождений подстроки"""
        cursor.execute(f"SELECT COUNT(*) as occurrences FROM test_table WHERE text_field LIKE '%{data}%'")

        # Обработка результатов запроса
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
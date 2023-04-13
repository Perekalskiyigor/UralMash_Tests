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

        # подключаем обработчик нажатия кнопки
        self.button.clicked.connect(self.execute_query)

        # создаем соединение с базой данных
        self.conn = sqlite3.connect('test.db')

    
    def execute_query(self):
        # получаем введенное значение из поля ввода
        data = self.line_edit.text()

        # создаем курсор для выполнения SQL-запросов
        cursor = self.conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS test_table
                (data TEXT)''')
        
        # наполняем таблицу данными
        data = [('gsregtgs',), ('tgergegeer',), ('gregeg',)]
        cursor.executemany('INSERT INTO test_table VALUES (?)', data)

        # выполняем запрос
        cursor.execute("SELECT * FROM test_table WHERE data=?", (data,))

        # получаем результат запроса
        result = cursor.fetchall()

        # отображаем результат на экране
        if result:
            self.result_label.setText('Результат: ' + str(result))
        else:
            self.result_label.setText('Результат не найден')

    def closeEvent(self, event):
        # закрываем соединение с базой данных при закрытии окна
        self.conn.close()

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
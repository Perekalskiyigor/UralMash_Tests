from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.label = QLabel('Введите список одинаковых букв:')
        self.input = QLineEdit()
        self.output_label = QLabel('Результат: ')
        self.output = QLabel()
        self.button = QPushButton('Подсчитать')
        
        # Обработчики
        self.button.clicked.connect(self.count_letters)
        
        # Группировка
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.input)
        vbox.addWidget(self.button)
        vbox.addWidget(self.output_label)
        vbox.addWidget(self.output)
        
        # Макет
        self.setLayout(vbox)
        
        # Размеры и заголовок окна
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('Подсчет букв')

    def count_letters(self):
        """Обработчик кнопки"""
        # Получаем введенный текст из поля ввода
        a = self.input.text()
        f = 1
        x = 1
        g = {}
        for i in a:
            if i in a[x:x+1]: #если есть i в a то f прибавляется на 1
                f += 1
            else:
                g[i] = f
                f = 1
            x += 1
        for i, c  in g.items():
            output = f"{i}{c}"
        # Выводим результаты подсчета в формате "количество буквы"
        self.output.setText(output)

if __name__ == '__main__':
    # Создаем приложение
    app = QApplication(sys.argv)
    # Создаем главное окно
    window = MainWindow()
    # Отображаем главное окно
    window.show()
    # Запускаем приложение
    sys.exit(app.exec_())




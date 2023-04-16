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
        s = self.input.text()
        # Создаем список для хранения подсчитанных букв и их количества
        counts = []
        # Инициализируем переменную для подсчета количества текущей буквы
        current_count = 1
        # Проходим по всем символам в строке
        for i in range(1, len(s)):
            # Если текущий символ равен предыдущему, увеличиваем счетчик текущей буквы
            if s[i] == s[i-1]:
                current_count += 1
            # Если текущий символ отличается от предыдущего, добавляем предыдущую букву и ее количество в список counts
            else:
                counts.append(str(current_count) + s[i-1])
                current_count = 1
        # Добавляем последнюю букву и ее количество в список counts
        counts.append(str(current_count) + s[-1])
        
        # Выводим результаты подсчета в формате "количество буквы"
        self.output.setText(''.join(counts))

if __name__ == '__main__':
    # Создаем приложение
    app = QApplication(sys.argv)
    # Создаем главное окно
    window = MainWindow()
    # Отображаем главное окно
    window.show()
    # Запускаем приложение
    sys.exit(app.exec_())




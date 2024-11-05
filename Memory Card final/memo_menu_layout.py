from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QFormLayout, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel
)
from memo_app import app
from memo_card_layout import layout_card

# Поля для введення запитання та варіантів відповідей
txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

# Створення форми для запитання та відповідей
layout_form = QFormLayout()
layout_form.addRow('Питання:', txt_Question)
layout_form.addRow('Правильна відповідь:', txt_Answer)
layout_form.addRow('Неправильныий варіант №1:', txt_Wrong1)
layout_form.addRow('Неправильныий варіант №2', txt_Wrong2)
layout_form.addRow('Неправильныий варіант №3:', txt_Wrong3)

# Кнопки для додавання питання та очищення полів
btn_create = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')

# Мітки для відображення статистики
lb_statistics = QLabel("Статистика")
lb_attempts = QLabel("Разів відповіли: " + "0")
lb_right = QLabel("Вірних відповідей: " + "0")
lb_success = QLabel("Успішність: " + "0")

# Кнопка для повернення назад
btn_back = QPushButton('Назад')

# Основний вертикальний макет
layout_main = QVBoxLayout()
layout_main.addLayout(layout_form)  # Додаємо форму до основного макету

# Горизонтальний макет для кнопок "Додати запитання" та "Очистити"
btn_line1 = QHBoxLayout()
btn_line1.addWidget(btn_create)
btn_line1.addWidget(btn_clear)
layout_main.addLayout(btn_line1)  # Додаємо горизонтальний макет для кнопок

# Додаємо мітки статистики та кнопку "Назад" до основного макету
layout_main.addWidget(lb_statistics)
layout_main.addWidget(lb_attempts)
layout_main.addWidget(lb_right)
layout_main.addWidget(lb_success)
layout_main.addWidget(btn_back)
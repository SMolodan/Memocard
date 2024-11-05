from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QFormLayout, QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox
)
from memo_app import app

# Основні кнопки і елементи
btn_Menu = QPushButton('Меню')          # Кнопка для повернення в основне меню
btn_Sleep = QPushButton('Відпочити')     # Кнопка для паузи (приховує вікно на час, встановлений у таймері)
box_Minutes = QSpinBox()                 # Поле введення часу паузи (в хвилинах)
box_Minutes.setValue(30)                 # Значення за замовчуванням: 30 хвилин
btn_OK = QPushButton('Відповісти')       # Кнопка для підтвердження відповіді
lb_Question = QLabel('')                 # Мітка для відображення запитання (слова для перекладу)

# Панель з варіантами відповідей
RadioGroupBox = QGroupBox("Варіанти відповідей")   # Група для варіантів відповідей
RadioGroup = QButtonGroup()                        # Група перемикачів, щоб обмежити вибір однією кнопкою

# Чотири варіанти відповідей
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

# Додаємо перемикачі в групу, щоб керувати ними як одним елементом
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Панель з результатом відповіді
AnsGroupBox = QGroupBox("Результат тесту")
lb_Result = QLabel('')    # Мітка для відображення результату ("правильно" чи "неправильно")
lb_Correct = QLabel('')   # Мітка для відображення правильної відповіді

# Розміщення варіантів відповідей у два стовпці
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()  # Перший стовпець
layout_ans3 = QVBoxLayout()  # Другий стовпець

# Додаємо перемикачі до вертикальних макетів
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

# Розміщуємо обидва стовпці у горизонтальний макет
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

# Застосовуємо горизонтальний макет як основний для панелі варіантів відповідей
RadioGroupBox.setLayout(layout_ans1)

# Розміщення елементів для панелі результату
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()  # Спочатку панель прихована

# Розміщення елементів на екрані (по рядках)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

# Перший рядок: кнопки меню, паузи, поле часу, і мітка "хвилин"
layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)   # Додаємо розрив між кнопками
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилин'))  # Мітка "хвилин" для пояснення таймера

# Другий рядок: питання по центру
layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

# Третій рядок: панель з варіантами відповідей і результатами
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

# Четвертий рядок: кнопка підтвердження відповіді по центру
layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2)
layout_line4.addStretch(1)

# Основний вертикальний макет для всього вікна
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  # Відстань між елементами

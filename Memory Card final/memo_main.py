from memo_card_layout import *
from memo_menu_layout import *
from time import sleep
from PyQt5.QtWidgets import QWidget
from random import shuffle, choice

# Розмір вікна
card_width, card_height = 600, 500
text_wrong = 'Невірно'
text_correct = 'Правильно'

# Клас питання, який зберігає текст питання та варіанти відповідей
class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_ans1
        self.wrong_answer2 = wrong_ans2
        self.wrong_answer3 = wrong_ans3

# Змінні для підрахунку правильних та загальної кількості відповідей
count_asked = 0
count_right = 0

# Функція, яка збільшує лічильник правильних відповідей
def got_right():
    global count_asked
    global count_right
    count_asked += 1
    count_right += 1

# Функція, яка збільшує лічильник неправильних відповідей
def got_wrong():
    global count_asked
    count_asked += 1

# Приклади запитань для тесту
q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

# Список питань
questions = [q1, q2, q3, q4]

# Функція для завантаження нового питання
def new_question():
    # Вибирає випадкове питання зі списку
    random_question = choice(questions)
    radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
    shuffle(radio_list)  # Перемішує варіанти відповідей

    # Призначає правильний варіант та інші варіанти
    global answer
    answer = radio_list[0]  # правильна відповідь
    wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]
    answer.setText(random_question.answer)
    wrong_answer1.setText(random_question.wrong_answer1)
    wrong_answer2.setText(random_question.wrong_answer2)
    wrong_answer3.setText(random_question.wrong_answer3)
    lb_Question.setText(random_question.question)

# Функція для відпочинку (приховує вікно на вибрану кількість хвилин)
def rest():
    n = box_Minutes.value()  # бере значення з поля для хвилин
    win_card.hide()  # приховує вікно
    sleep(n)  # пауза на вказаний час
    win_card.show()  # знову показує вікно

# Підключаємо кнопку відпочинку до функції
btn_Sleep.clicked.connect(rest)

# Функція для перевірки вибраної відповіді
def check_result():
    '''
    Перевіряє, чи обрана відповідь правильна.
    Якщо відповідь правильна, показує "Правильно", інакше - "Неправильно".
    Також оновлює статистику.
    '''
    correct = answer.isChecked()
    if correct:
        lb_Result.setText('Правильно')
        got_right()  # збільшує лічильник правильних відповідей
    else:
        lb_Result.setText('Неправильно')
        got_wrong()  # збільшує лічильник неправильних відповідей

# Функція для перемикання між питанням і результатом
def switch_screen():
    if btn_OK.text() == 'Відповісти':
        check_result()  # перевіряє відповідь
        RadioGroupBox.hide()  # приховує варіанти відповідей
        AnsGroupBox.show()  # показує результат
        btn_OK.setText('Наступне питання')
    else:
        new_question()  # завантажує нове питання
        RadioGroupBox.show()  # показує варіанти відповідей
        AnsGroupBox.hide()  # приховує результат
        btn_OK.setText('Відповісти')

        # Скидає вибір у радіокнопках
        RadioGroup.setExclusive(False)  # дозволяє скинути вибір
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)  # повертає обмеження (тільки одна кнопка може бути вибрана)

# Функція для очищення полів введення при додаванні нового питання
def clear_lines():
    txt_Question.clear()
    txt_Answer.clear()
    txt_Wrong1.clear()
    txt_Wrong2.clear()
    txt_Wrong3.clear()

# Підключаємо кнопку очищення до функції
btn_clear.clicked.connect(clear_lines)

# Функція для створення нового питання та додавання його до списку питань
def add_question():
    question = txt_Question.text()
    answer = txt_Answer.text()
    wrong_ans1 = txt_Wrong1.text()
    wrong_ans2 = txt_Wrong2.text()
    wrong_ans3 = txt_Wrong3.text()
    q = Question(question, answer, wrong_ans1, wrong_ans2, wrong_ans3)
    questions.append(q)  # додає питання до списку
    clear_lines()  # очищує поля введення

# Підключаємо кнопку створення питання до функції
btn_create.clicked.connect(add_question)

# Функція для переходу в меню статистики
def menu_stat():
    '''
    Відображає статистику після завершення тесту.
    Показує кількість питань, кількість правильних відповідей
    та успішність у відсотках.
    '''
    global count_asked
    global count_right
    if count_asked != 0:
        result = count_right / count_asked * 100  # обчислює успішність
    else:
        result = "0"
    win_card.hide()  # приховує
    win_menu.show()  # показує меню
    lb_attempts.setText("Разів відповіли: " + str(count_asked))
    lb_right.setText("Вірних відповідей: " + str(count_right))
    lb_success.setText("Успішність: " + str(result))

# Підключаємо кнопку меню до функції
btn_Menu.clicked.connect(menu_stat)

# Функція для повернення з меню статистики назад до вікна тесту
def card_stat():
    win_menu.hide()  # приховує меню
    win_card.show()  # показує вікно тесту


# Підключаємо кнопку повернення до функції
btn_back.clicked.connect(card_stat)


# Налаштування вікна тесту
win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

win_card.setLayout(layout_card)
new_question()  # завантажує перше питання

# Підключаємо кнопку відповіді до функції перемикання екрана
btn_OK.clicked.connect(switch_screen)

# Налаштування вікна меню
win_menu = QWidget()
win_menu.setLayout(layout_main)

# Показуємо вікно тесту та запускаємо застосунок
win_card.show()
app.exec_()
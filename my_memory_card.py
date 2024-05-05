from PyQt5.QtCore import Qt
from random import shuffle, randint
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QMessageBox, QRadioButton, QPushButton, QVBoxLayout, QApplication, QGroupBox, QButtonGroup

class Question():
    def  __init__ (self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Бразильский', 'Итальянский'))
question_list.append(Question('Когда закончилась 2-ая мировая?', '1945', '1948', '1946', '1947'))
question_list.append(Question('Когда началась 2-ая мировая?', '1939', '1941', '1937', '1938'))
question_list.append(Question('Как называется еврейский Новый год?', 'Рош-ха-Шана', 'Ханука', 'Йои Кипур' , 'Кванза'))
question_list.append(Question('Сколько синих полос на флаге США?', '0', '13', '6', '7'))
question_list.append(Question('Какое животное не фигурирует в китайском зодиаке?', 'Колибри', 'Дракон', 'Собака', 'Кролик'))
question_list.append(Question('В какой стране проходили летние Олимпийские игры 2016?', 'Бразилия', 'Ирландия', 'Китай', 'Италия'))
question_list.append(Question('Какая планета самая горячая?', 'Венера', 'Сатурн', 'Меркурий', 'Марс'))
question_list.append(Question('Самая редкая группа крови?', 'IV', 'I', 'II', 'III'))
question_list.append(Question('Сколько костей в теле человека?', '206','205','201','209'))
my_app = QApplication([])

text = QLabel('Самый сложный вопрос в мире !')
button = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

lay1 = QHBoxLayout()
lay2 = QVBoxLayout()
lay3 = QVBoxLayout()
lay4 = QHBoxLayout()
lay5 = QHBoxLayout()
lay6 = QHBoxLayout()

RadioGroupBox.setLayout(lay1)
lay4.addWidget(text, alignment = Qt.AlignHCenter| Qt.AlignVCenter)
lay6.addStretch(1)
lay6.addWidget(button, stretch = 2)
lay6.addStretch(1)
lay5.addWidget(RadioGroupBox)
lay2.addWidget(rbtn_1)
lay2.addWidget(rbtn_3)
lay3.addWidget(rbtn_2)
lay3.addWidget(rbtn_4)
lay1.addLayout(lay2)
lay1.addLayout(lay3)
lay4.addLayout(lay1)
laycard = QVBoxLayout()
laycard.addLayout(lay4, stretch=1)
laycard.addLayout(lay5, stretch=3)
laycard.addStretch(1)
laycard.addLayout(lay6, stretch = 1)
laycard.addStretch(1)
laycard.setSpacing(5)

AnsGroupBox = QGroupBox('Результаты теста')
Result = QLabel('прав ты или нет?')
Correct = QLabel('ответ будет тут')

lay_res = QVBoxLayout()
lay_res.addWidget(Result, alignment =(Qt.AlignLeft| Qt.AlignTop))
lay_res.addWidget(Correct, alignment = Qt.AlignCenter, stretch = 2)
AnsGroupBox.setLayout(lay_res)
lay5.addWidget(AnsGroupBox)
AnsGroupBox.hide()

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(False)

def show():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    Correct.setText(q.right_ans)
    show_question()

def show_correct(res):
    Result.setText(res)
    show()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика \n-Всего вопросов:' , main_win.total, '\n-Правильных ответов:', main_win.score)
        print('Рейнтинг:', (main_win.score/main_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейнтинг:', (main_win.score/main_win.total*100), '%')

def next_question():
    main_win.total += 1
    print('(Статистика \n-Всего вопросов:' , main_win.total, '\n-Правильных ответов:', main_win.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)
def click_OK():
    if button.text == 'Ответить':
        check_answer()
    else:
        next_question()

main_win = QWidget()
main_win.setLayout(laycard)
main_win.setWindowTitle('Memory Card')

main_win.cur_question = -1
button.clicked.connect(click_OK)

main_win.score = 0
main_win.total = 0
next_question()
main_win.resize(400,300)

main_win.show()
button.clicked.connect(check_answer)
my_app.exec_()
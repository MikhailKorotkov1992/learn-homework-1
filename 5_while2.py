"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""


questions_and_answers = {
  'как дела?' : 'хорошо', 'что делаешь?' : 'программирую', 'какой сейчас год?' : '2022'
}

def add_question(question):
    questions_and_answers[question] = input('Сами ответьте на свой вопрос и я его запомню =): ')

def ask_user(answers_dict):
    print('Задайте вопрос или нажмите Enter для выхода')
    while True:
        question = input('Задайте вопрос: ').lower()
        if question == '':
          print('Досвидания!')
          break
        answer = answers_dict.get(question)
        if answer:
            print(f'Программа: {answer}')
        else:
            add_question(question)

if __name__ == "__main__":
    ask_user(questions_and_answers)

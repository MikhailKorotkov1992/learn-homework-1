"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

questions_and_answers = {
  'как дела?' : 'хорошо', 'что делаешь?' : 'программирую', 'какой сейчас год?' : '2022'
}

def add_question(question):
    questions_and_answers[question] = input('Сами ответьте на свой вопрос и я его запомню =): ')

def ask_user(answers_dict):
    while True:
        try:
            question = input('Задайте вопрос: ').lower()
            answer = answers_dict.get(question)
            if answer:
                print(f'Программа: {answer}')
            else:
                add_question(question)
        except KeyboardInterrupt:
            print('Пока!')
            break

if __name__ == "__main__":
    ask_user(questions_and_answers)
""" student Mikhail Korotkov

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

right_answer = 'хорошо'
answer = ''

def hello_user(right_answer, answer):
    while answer.lower() != right_answer:
        answer = input('Как дела?: ')

    
if __name__ == "__main__":
    hello_user(right_answer, answer)

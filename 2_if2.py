"""student Mikhail Korotkov

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def check_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    str1 = str1.lower()
    str2 = str2.lower()
    if str1 == str2:
        return 1
    if str1 != str2:
        if str2 == 'learn':
            return 3
        if len(str1) > len(str2):
            return 2


def main():
    print(check_strings('Hello, World!', 'Hello, World!'))
    print(check_strings(1, 111))
    print(check_strings('1', 1))
    print(check_strings('Hello', 'World'))
    print(check_strings('Python', 'learn'))
    print(check_strings('long string', 'learn'))
    print(check_strings('very long string', 'short string'))
    
if __name__ == "__main__":
    main()

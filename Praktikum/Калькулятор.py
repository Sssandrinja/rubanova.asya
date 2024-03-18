def word_to_number(word):
    "Вспомогательная функция-конвертер для превращения слов-чисел в числа типа int для последующих операций над ними"
    numbers = {
        'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,
        'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12,
        'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17,
        'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30, 'сорок': 40,
        'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90
    }
    return numbers[word]


def number_to_words(n):
    """Функция, которая переводит число типа int в прописной вид этого числа на русском языке"""
    dig = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    dec = ['',  'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
           'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    teen = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
            'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    x = ''
    if n == 0:
        return 'ноль'
    if (10 < n % 100 < 20):
        x += teen[n % 10]
    else:
        d = dec[n % 100 // 10]
        x += d + (d and ' ' or '') + dig[n % 10]
    return x


def calc(expression):
    "Функция, которая вычисляет примеры, записанные текстом"
    operations = {'плюс': '+', 'минус': '-', 'умножить': '*', 'делить': '/'}
    words = expression.split()

    # Если одно число 2 значное и 1 однозначное
    if len(words) == 4:
        if words[1] in operations:
            num1 = word_to_number(words[0])
            operator = operations[words[1]]
            num2 = str(eval(str(word_to_number(words[2])) + word_to_number(str(words[3]))))
        elif words[2] in operations:
            num1 = str(eval(str(word_to_number(words[0])) + "+" + str(word_to_number(words[1]))))
            operator = operations[words[2]]
            num2 = word_to_number(words[3])
    # если 2 двухзначных числа
    elif len(words) == 5:
        if words[2] in operations:
            num1 = str(eval(str(word_to_number(words[0])) + "+" + str(word_to_number(words[1]))))
            operator = operations[words[2]]
            num2 = str(eval(str(word_to_number(words[3])) + word_to_number(str(words[4]))))
    # если 2 однозначных числа
    else:
        num1 = word_to_number(words[0])
        operator = operations[words[1]]
        num2 = word_to_number(words[2])

    # eval() вычисляет пример записаный в строке(str)
    result = eval(f"{num1} {operator} {num2}")
    # print(result)
    # конвертируем численный результат в слова
    return number_to_words(int(result))


# Пример использования
print(calc("двадцать пять плюс пять"))
print(calc("сорок пять минус шесть"))
print(calc("пять умножить пять"))
print(calc("двадцать восемь делить четыре"))
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def print_board(board): # вывод игрового поля
    for i in board:
        print(" ".join(i))
 
def input_check(y, x):  # проверка корректности ввода
    if not y.isdigit() or not x.isdigit():  # Если x или y - не цифры, то возвращаем ложь
        return False
    if not (1 <= int(y) <= 4) or not (1 <= int(x) <= 5):  # если x или y выходят за пределы поля - ввод ошибочный 
        return False
    if board[int(y) - 1][int(x) - 1] != '.': # если координаты клетки не заняты точкой, то ввод некорректный

        return False
    return True
 
def end_check():  # проверяем закончилась ли игра
    # Если все клетки пустые, то завершаем игру
    if '.' not in board[0] and '.' not in board[1] and '.' not in board[2] and '.' not in board[3]:  
        return True
    return False
 
def check(y1, x1): # проверка есть ли рядом символ для начисления штрафных баллов
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)] # все клетки вокруг
    for dy, dx in moves:
        dy1 = dy + y1 
        dx1 = dx + x1
        if 0 <= dy1 <= 3 and 0 <= dx1 <= 4: # Проверяем чтобы координаты не вышли за границы массива
            if board[y1][x1] == board[dy1][dx1]: # если клетка из окрестности равна клетки, в которую игрок поставил свой символ
                score[h % 3] += 1 # начисляем штрафное очко
# Игровое поле
board = [["."] * 5 for i in range(4)]
# print(board) Проверка
 
k = 0  # Cчетчик ходов
score = [0, 0, 0]  # счет
 
while True: # запускаем бесконечный цикл пока игра не закончится
    print_board(board)
 
    print("Текущий счет:", score[0], score[1], score[2])
    print("Ход игрока: ", h % 3 + 1, "Введи ЧЕРЕЗ ПРОБЕЛ координаты для своего символа. Первый по ОУ второй по ОХ")
 
    inp = input().split()
    move1 = inp[0]
    move2 = inp[1]
    if not input_check(move1, move2):
        print("Некорректный ход")
        continue
    y, x = int(move1) - 1, int(move2) - 1  # приводим введеные координату к типу <int>
    board[y][x] = str(h % 3 + 1)  # по введенным координатам заполняем ячейку символом игрока
    check(y, x)
    if end_check():
        print_board()
        print("Конец игры")
        print("Текущий счет:", score[0], score[1], score[2])
        print("Победил игрок", score.index(min(score)) + 1)
        break
    k += 1


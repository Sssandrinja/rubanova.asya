#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random 
 
def print_board(board): # создание игрового поля
    for row in board:
        print(" ".join(row)) # записать через пробел элементы строк 
 
def check_win(board): # проверка есть ли победитель
    for i in board: # проверяем элементы по их индексам
        if "0" in i: 
            return False # если на поле остаются пуговицы, то игра продолжается 
    return True # если пуговиц нет - определяется победитель
 
moves = ["a", "b", "c", "d", "e", "f", "g", "h"] # обозначения столбцов игрового поля
movesLn = ["8", "7", "6", "5", "4", "3", "2", "1"] # обозначения линий игрового поля
 
"""
# - пустые поля
0 - пуговицы
"""
 
board = [[random.choice(["#", "0"]) for i in range(8)] for j in range(8)] # создание игрового поля со случайным расположением пуговиц и крестов
 
 
# print(board) # ПРОВЕРКА
 
# print_board(board) # проверка
 
# game_finish = False
 
name1 = input("Первый игрок, введите свое имя: ")
name2 = input("Второй игрок, введите свое имя: ")
 
k = 1 # если k нечетный, то ходит игрок1

 
while True: # != True:
    # print(board)
    
    print_board(board)
    
    if check_win(board) == True:
        # game_finish = True
        winner = "" # вывод имени победителя 
        if k % 2 == 0: # сейчас ход второго игрока, но при этом все поля уже пустые, то игрок1 - победитель
            winner = name1
        else: 
            winner = name2
        print("Конец игры. Победа: ", winner)
        break # закончили бесконечный цикл while 
 
    if k % 2 != 0: # ход первого игрока
 
        print(name1, ", напишите номер строки(сверху вниз от 8 до 1) или букву столбца(cлева направо от a до h):")
        move = input("Ход: ")
 
        if move in moves: # ходит по столбцам
            stolbik_index = moves.index(move)
            # print(stolbik_index)
            for i in range(len(board)): # заменяем пуговицы на кресты на всей длине столбца 
                if board[i][stolbik_index] == "0": # если всё еще там есть пуговицы, то они заменятся на кресты
                    # print("YEEI")
                    board[i][stolbik_index] = "#"
           
            
        elif move in movesLn: # игрок ходит по строкам 
            line_index = movesLn.index(move)
            # print(line_index) # check
            if "0" in board[line_index]: # если пуговицы всё еще присутсвуют в этой сроке, то все элементы строки заменятся на кресты
                board[line_index] = ["#" for i in range(8)] 
        else:
            print("Некорректный ввод") 
            break 
        k += 1 # ход переходит второму игроку 
    elif k % 2 == 0: 
        print(name2, ", напишите номер строки(сверху вниз от 8 до 1) или букву столбца(cлева направо от a до h):")
        move = input("Ход: ")
        if move in moves:
            stolbik_index = moves.index(move)
            # print(stolbik_index)
            for i in range(len(board)):
                if board[i][stolbik_index] == "0":
                    # print("YEEI")
                    board[i][stolbik_index] = "#"
          
            
        elif move in movesLn:
            line_index = movesLn.index(move)
            # print(line_index) # check
            if "0" in board[line_index]:
                board[line_index] = ["#" for i in range(8)]
        else:
            print("Некорректный ввод")
            break
        k += 1
    else:
        print("Неизвестная ошибка")


# In[ ]:





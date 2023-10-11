import os
import time
import random


def row_equal(row):
    return all(element == row[0] for element in row)

def slope(arr):
    if arr[1][1] == ' ':
        return False
    else:
        return (arr[0][2] == arr[1][1] and arr[0][2] == arr[2][0]) or (arr[0][0] == arr[1][1] and arr[0][0] == arr[2][2])

def column_equal(my_2d_list, column_index):
    column_values = [row[column_index] for row in my_2d_list]
    return all(element == column_values[0] for element in column_values)

again = 1

while again == 1:
    placed = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    grid = f'''
       1    2    3
      ---  ---  ---
    1 | {placed[0][0]} | {placed[0][1]} | {placed[0][2]} |
      --- --- ---
    2 | {placed[1][0]} | {placed[1][1]} | {placed[1][2]} |
      --- --- ---
    3 | {placed[2][0]} | {placed[2][1]} | {placed[2][2]} |
      --- --- ---
    '''

    print(grid)

    win = False
    turn = 1

    while win != True and any(' ' in row for row in placed):
        if turn%2 :
            cur = 'X'
        else:
            cur = 'O'

        print(f"It's {cur} turn")
        row = int(input(f'row: '))
        col = int(input(f'column: '))

        if placed[row-1][col-1] == " ":
            placed[row-1][col-1] = cur
        else:
            print("\nAlready taken!!\nTurn skipped!!!")
            turn += 1
            continue

        grid = f'''
       1    2    3
      ---  ---  ---
    1 | {placed[0][0]} | {placed[0][1]} | {placed[0][2]} |
      --- --- ---
    2 | {placed[1][0]} | {placed[1][1]} | {placed[1][2]} |
      --- --- ---
    3 | {placed[2][0]} | {placed[2][1]} | {placed[2][2]} |
      --- --- ---
    '''

        print(grid)

        if row_equal(placed[row-1]) or slope(placed) or column_equal(placed, col-1):
            win = True
            break

        turn += 1

    if win:
        print(f'The winner is {cur}!!')
    else:
        print('Draw!!')
    
    again = int(input('Enter 1 to play again: '))

#tic-tac-toe
from random import randint

def print_test_field():
    print('\n\t 0 | 1 | 2\n\t ' + '-' * 9)
    print('\t 3 | 4 | 5\n\t ' + '-' * 9)
    print('\t 6 | 7 | 8\n\t')

def print_field(arg):
    print('\n\t {} | {} | {}\n\t '.format(arg[0], arg[1], arg[2]) + '-' * 9)
    print('\t {} | {} | {}\n\t '.format(arg[3], arg[4], arg[5]) + '-' * 9)
    print('\t {} | {} | {}\n\t'.format(arg[6], arg[7], arg[8]))

def comparisons(listf, tuplef):
    local_list = []
    for i in range(len(listf)):
        if listf[i] == 'X':
            local_list.append(i)
    for item in tuplef:
        for initem in item:
            local_count = 0
            if initem in local_list:
                local_count += 1
                if local_count == 3:
                    return 1

def main_script_X(index):
    field_list[index] = 'X'

def main_script_O(index):
    field_list[index] = 'O'

print('\nНиже указана нумерация клеток игрового поля:')
print_test_field()

vict_combs = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6), )
field_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

while True:
    turn = input('Хотите начать первым? (y/n): ')
    if turn.lower() == 'y' or turn.lower() == 'n':
        break

if turn.lower() == 'y':
    while True:

        c = comparisons(field_list, vict_combs)
        if c == 1:
            print('Вы победили! Поздравляю!')
            break

        print_field(field_list)
        hod = int(input('Введите номер ячейки: '))

        main_script_X(hod)
        main_script_O(randint(0,8))

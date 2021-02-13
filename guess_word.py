from random import randint

def print_word(*wrd, char=None, lst=[]):
    main_answer = ''
    for i in wrd:
        if (char == i) or (i in lst):
            main_answer += i
        else:
            main_answer += '_'
    return main_answer

words_tuple = ('python', 'computer', 'desktop', 'laptop', 'keyboard', 'mouse', 'internet', 'touchpad', 'windows', 'linux',)
WORD = words_tuple[randint(0,9)]

right_list = []

input('\nИГРА: Угадай слово\nУ тебя 10 попыток\nНажми ENTER чтобы начать...')

l = 10

print('\nСлово из {} букв: \n'.format(len(WORD)), print_word(*WORD).replace('', ' ').strip())

while True:
    if l != 0:
        char1 = input('\nВведите символ: ')

        if 0 < len(char1) < 2:

            if char1 in WORD:
                print('\nПравильно!')

                right_list.append(char1)
                print(print_word(*WORD, char=char1, lst=right_list).replace('', ' ').strip())

                if print_word(*WORD, char=char1, lst=right_list) == WORD:
                    print('\nПоздравляю! Ты победил!\n')
                    break

            else:
                l -= 1
                print('\nНеправильно!\nОсталось {} попыток...\n'.format(l))
                print(print_word(*WORD, lst=right_list).replace('', ' ').strip())
        else:
            print('\nНЕОБХОДИМО ВВЕСТИ СИМВОЛ!!!\nМинус одна попытка.')
            l -= 1
    else:
        print('\nВы проиграли...\nПраильное слово было: {}'.format(WORD))
        break


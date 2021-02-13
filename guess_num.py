from random import randint

def comparisons(num, ans):
    if ans < num:
        ans = int(input('\nНеверно.. Число больше(>)!\nПовтори попытку: '))
        return ans
    if ans > num:
        ans = int(input('\nНеверно.. Число меньше(<)!\nПовтори попытку: '))
        return ans
    else:
        return None

print('Угадай число от 1 до 100\n')
input('Нажми ENTER чтобы начать...\n')

NUMBER = randint(1,100)
ANSWER = int(input('Введи число: '))

while True:
    ANSWER = comparisons(NUMBER, ANSWER)

    if ANSWER == None:
        print('\nТы победил!!! Congratulations!\n')
        break

print('Число было: {}'.format(NUMBER))
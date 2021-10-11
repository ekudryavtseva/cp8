def perevod(a, b):
    chislo = ''
    while a > 0:
        chislo = str(a % b) + chislo
        a = a//b
    return int(chislo)


try:
    print('Введите свое число')
    numb = int(input())
    print('Выберете 2-ичную или 8-ичную')
    sist = int(input())
    while sist != 8 and sist != 2:
        print('2-ичную или 8-ичную')
        sist = int(input())
    print(perevod(numb, sist))
except ValueError:
    print('Это не число. Введите число.')

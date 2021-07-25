from os import system
import random,time

verde = '\033[5;32m'
red = '\033[1;31m'
feixa = '\033[m'


system('clear')

def arte():
    print(f'''
        {verde}
        ╔══╗╔══╗╔══╗╔╦╗╔══╗╔══╗╔══╗
        ╚╗╔╝║╔╗║║╔╗║║║║║╔╗║╚╗╗║║╔╗║
        ─║║─║╠╣║║╔╗║║║║║╠╣║╔╩╝║║╠╣║
        ─╚╝─╚╝╚╝╚══╝╚═╝╚╝╚╝╚══╝╚╝╚╝{feixa}''')


while True:
    arte()

    r1 = random.randint(0,10)
    r2 = random.randint(0,10)

    result = r1 * r2

    numero = int(input(f'\t\t{verde}{r1} X {r2} = ?\n\n\tqual E o Numero?:{feixa} '))

    if numero == result:
        print(f'\n\t{verde}ACERTOU{feixa}')
        time.sleep(2)
        system('clear')
        continue


    else:
        print(f'\t\t{red}ERROU E{feixa} {verde}{result}{feixa}')
        time.sleep(2)
        system('clear')


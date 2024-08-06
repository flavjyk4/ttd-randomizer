from keyboard import on_press, wait
from secrets import choice
from config import *
from sys import exit
newline = '\n'

def rollall():
    print(f'Mapa: {choice(maps)}')
    print(f'Tryb: {choice(modes)}')

    for n in range(6):
        print(f'Postać {n}: {choice(units).removesuffix(newline)}')

    for n in range(2):
        print(f'Utrudnienie {n}: {choice(impediments)}')

def onkey(event):
    try:
        key = int(event.name)
        if key > 0 and key < 7:
            print(f'Postać {key}: {choice(units).removesuffix(newline)}')
        elif key > 6 and key < 9:
            print(f'Utrudnienie {key - 6}: {choice(impediments)}')
        else:
            rollall()
    except ValueError:
        pass

rollall()
on_press(onkey)
try:
    wait()
except KeyboardInterrupt:
    print("Zatrzymano.")
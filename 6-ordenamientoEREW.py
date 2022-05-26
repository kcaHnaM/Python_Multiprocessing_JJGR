'''Programa 1: SUMA EREW
Estudiante: José Juan García Romero'''

from __future__ import print_function
from multiprocessing import Process
import multiprocessing
import time
import os

def print_titulo():
    for i in range (1,46):
        print('-',end='')
    print('\n')

def cls_screen():
    if os.name == "windows" or os.name == "nt" or os.name == "dos" or os.name == "ce":
        os.system("cls")
    else:
        os.system("clear")

def process_01(a, i, odd, even):
    a[2 * i] = odd[i]
    a[2 * i + 1] = even[i]

def process_02(a, i, Laux):
    if (a[2 * i + 1] < a[2 * i]):
        a[2 * i + 1], a[2 * i] = interchange(a[2 * i + 1], a[2 * i])

def interchange(b, c):
    aux = b
    b = c
    c = aux
    return b, c

def oddEvenSplit(a):
    n = len(a)
    aux = int(n / 2)
    b = a[0:aux]
    c = a[aux:n]
    return (b, c)

def oddEvenMergePRAM(a):
    n = len(a)
    if n == 2:
        if (a[0] > a[1]):
            a[0], a[1] = interchange(a[0], a[1])
    else:
        odd, even = oddEvenSplit(a)
        oddEvenMergePRAM(odd)
        oddEvenMergePRAM(even)
        return (odd, even)

def main():
    a = [16, 22, 35, 40, 55, 66, 70, 85, 15, 18, 23, 53, 60, 69, 72, 78]

    cls_screen()
    print_titulo()
    print('\tPrograma 6. ORDENAMIENTO EREW\n')
    print_titulo()

    print('Arreglo original: ', a)

    oddEvenMergePRAM(a)
    odd, even = oddEvenMergePRAM(a)
    n = len(a)

    print()

    for i in range(0, int(n / 2)):
        p1 = multiprocessing.Process(target=process_01, args=(a, i, even, odd))
        p1.run()
        p1.start()
        p1.join()
        print("Revisar Proceso 1: ",p1.is_alive)

    lCopy = a.copy()

    print()

    for i in range(0, int(n / 2)):
        p2 = multiprocessing.Process(target=process_02, args=(a, i, lCopy))
        p2.run()
        p2.start()
        p2.join()
        print("Revisar Proceso 2: ",p2.is_alive)

    print()
    print('Ordenando el arreglo')
    print()
    print(oddEvenMergePRAM(even))
    print(oddEvenMergePRAM(odd))
    print(oddEvenSplit(a))
    print(oddEvenMergePRAM(a))
    print()
    print('Arreglo Ordenado: \n', a)
    print()
    #time.sleep(2)

    input('\nPresiona cualquier tecla para salir...')
    cls_screen()

if __name__ == '__main__':
    main()
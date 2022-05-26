'''Programa 5: ORDENAMIENTO CRCW
Estudiante: José Juan García Romero'''

from multiprocessing import Process
import multiprocessing
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

def ordCRCW(a, c, n, b):
    for i in range(n):
        c[i] = 0
    print("Paso 01: ", c)


    for i in range(n):
        for j in range(n):
            if a[i] > a [j]:
                c[i] = c[i] + 1
    print("Paso 02: ", c)

    for i in  range (n):
        b [c[i]] = a[i]
    print("Paso 03: ", b)
    print()
    print("El arreglo ordenado es:", b)

def main():
    a = [95,10,6,15]
    b = [0,0,0,0]
    c = [9,9,9,9]
    n = len(a)

    cls_screen()
    print_titulo()
    print('\tPrograma 5. ORDENAMIENTO CRCW\n')
    print_titulo()

    print("El arreglo es: ", a)
    p = multiprocessing.Process(ordCRCW(a,c,n,b))
    p.run()
    p.start()
    p.join()
    print("Revisar Proceso: ",p.is_alive)

    input('\nPresiona cualquier tecla para salir...')
    cls_screen()

if __name__ == '__main__':
    main()
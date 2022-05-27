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

def process_01(win, i):
    win[i] = 0

def process_02(L, win, i, j):
    if(L[i] > L[j]):
        win[i] = win[i] + 1
    else:
        win[j] = win[j] + 1

def process_03(L, win, i, aux):
    L[win[i]] = aux[i]

def ordeamiento(L):
    n = len(L) - 1
    win = [None for _ in range(n + 1)]
    win[0] = 0

    processes = []

    for i in range(1, n + 1):
        p1 = multiprocessing.Process(target = process_01, args = (win, i))
        processes.append(p1)
        p1.run()
        p1.start()
        p1.join()
        print("Revisar Proceso 1: ",p1.is_alive)

    processes = []

    for i in range(1, n + 1):
        k = 0
        for j in range(i, n + 1):
            p2 = multiprocessing.Process(target = process_02, args = (L, win, k, j))
            processes.append(p2)
            p2.run()
            p2.start()
            k += 1
            p2.join()
            print("Revisar Proceso 2: ",p2.is_alive)
    
    processes = []

    aux = L.copy()

    for i in range(0, n + 1):
        p3 = multiprocessing.Process(target = process_03, args = (L, win, i, aux))
        processes.append(p3)
        p3.run()
        p3.start()
        p3.join()
        print("Revisar Proceso 3: ",p3.is_alive)

    print('\n\nOrdenamiento Win: ',win,"\n")
    print('Vector ordenado: ',L)

def main():
    L = [95, 10, 6, 15]

    cls_screen()
    print_titulo()
    print('\tPrograma 5. ORDENAMIENTO CRCW\n')
    print_titulo()

    print("Arreglo original: ", L,"\n")
    
    ordeamiento(L)

    input('\nPresiona cualquier tecla para salir...')
    cls_screen()

if __name__ == '__main__':
    main()
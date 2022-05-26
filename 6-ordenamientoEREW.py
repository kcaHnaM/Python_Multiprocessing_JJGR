'''Programa 6: ORDENAMIENTO CRCW
Estudiante: José Juan García Romero'''

from __future__ import print_function
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

def mergeSortPRAM(L):
    n = len(L)
    L1_aux = L[:int(n/2)]
    L2_aux = L[int(n/2):]
    Process_jobs = []

    if n >= 2:
        p = multiprocessing.Process(target=mergeSortPRAM, args=(L1_aux,))
        Process_jobs.append(p)
        p.run()
        p.start()
        p.join()
        print("Revisar Proceso 1: ",p.is_alive)

        p = multiprocessing.Process(target=mergeSortPRAM, args=(L2_aux,))
        Process_jobs.append(p)
        p.run()
        p.start()
        p.join()
        print("Revisar Proceso 2: ",p.is_alive)

        for i in range(0, n):
            if i < int(n / 2):
                L[i] = L1_aux[i]
            else:
                L[i] = L2_aux[i - int(n / 2)]

        oddEvenMergePRAM(L)

def oddEvenMergePRAM(L):
    n = len(L)
    Process_jobs = []

    if n == 2:
        if L[0] > L[1]:
            interchange(L, 0, 1)
    else:
        odd, even = oddEvenSplit(L)

        p = multiprocessing.Process(target=oddEvenMergePRAM, args=(odd,))
        Process_jobs.append(p)
        p.run()
        p.start()
        p.join()
        print("Revisar Proceso 3: ",p.is_alive)

        p = multiprocessing.Process(target=oddEvenMergePRAM, args=(even,))
        Process_jobs.append(p)
        p.run()
        p.start()
        p.join()
        print("Revisar Proceso 4: ",p.is_alive)

        for i in range(1, int(n/2)+1):
            p = multiprocessing.Process(target=executeMerge1, args=(i, odd, even, L,))
            Process_jobs.append(p)
            p.run()
            p.start()
            p.join()
            print("Revisar Proceso 5: ",p.is_alive)

        for i in range(1, int(n / 2)):
            p = multiprocessing.Process(target=executeMerge2, args=(i, L,))
            Process_jobs.append(p)
            p.run()
            p.start()
            p.join()
            print("Revisar Proceso 6: ",p.is_alive)

def executeMerge1(i, odd, even, L):
    L[2 * i - 2] = odd[i - 1]
    L[2 * i - 1] = even[i - 1]

def executeMerge2(i, L):
    if L[2*i - 1] > L[2*i]:
        interchange(L, 2*i - 1, 2*i)


def interchange(Array, index_a, index_b):
    aux = Array[index_a]
    Array[index_a] = Array[index_b]
    Array[index_b] = aux


def oddEvenSplit(array):
    odd = array[::2]
    even = array[1::2]
    return odd, even


def copyArray(A, B):
    for i in range(0, len(A)):
        A[i] = B[i]

def main():
    L = [16, 22, 35, 40, 55, 66, 70, 85, 15, 18, 23, 53, 60, 69, 72, 78]

    cls_screen()
    print_titulo()
    print('\tPrograma 6. ORDENAMIENTO EREW\n')
    print_titulo()

    print('Arreglo original: ', L,"\n\n")

    mergeSortPRAM(L)

    print('\n\nArreglo Ordenado: ', L)
    print()
    #time.sleep(2)

    input('\nPresiona cualquier tecla para salir...')
    cls_screen()

if __name__ == '__main__':
    main()
'''Programa 2: SUMA CREW
Estudiante: José Juan García Romero'''

from multiprocessing import Process
import multiprocessing
import math
import time
import os

def process(i,j,A):
    if(((int)(math.pow(2,i-1)) + 1) <= j):
        A[j] = A[j] + A[j - ((int)(math.pow(2,i-1)))]
        print(A[1:9])
    #time.sleep(1)

def print_titulo():
    for i in range (1,41):
        print('-',end='')
    print('\n')

def cls_screen():
    if os.name == "windows" or os.name == "nt" or os.name == "dos" or os.name == "ce":
        os.system("cls")
    else:
        os.system("clear")

def main():
    A = [0,5,2,10,1,8,12,7,3]
    n = len(A) - 1
    j = 1
    log = (int)(math.log(n,2))

    processes = []

    cls_screen()
    print_titulo()
    print('\tPrograma 2. SUMA CREW\n')
    print_titulo()

    print(A[1:n+1])

    for i in range(1, log + 1):
        while j <= n:
            p = multiprocessing.Process(target=process, args=(i,j,A))
            processes.append(p)
            p.run()
            p.start()
            p.join()
            print("Revisar Proceso: ",p.is_alive)
            j = j + 1

    print(A[1:n+1])

    print('\nSuma Total: ',A[n])

    input('\nPresiona cualquier tecla para salir...')
    cls_screen()

if __name__ == '__main__':
    main()
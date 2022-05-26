'''Programa 1: SUMA EREW
Estudiante: José Juan García Romero'''

from concurrent.futures import process
import multiprocessing
import math
import time
import os

def executeMultProc(i,j,A):
    if (((2*j)%(math.pow(2,i))) == 0):
        A[2*j] = A[2*j] + A[((2*j)-((int) (math.pow(2,i-1))))]
    

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

    cls_screen()
    print_titulo()
    print('\tPrograma 1. SUMA EREW\n')
    print_titulo()

    print(A[1:len(A)])

    a = len(A)-1
    log = int(math.log(a,2))

    processes = []

    for i in range(1,log+1):
        for j in range(1,(int)(a/2)+1):
            p = multiprocessing.Process(target=executeMultProc,args=(i,j,A))
            processes.append(p)
            p.start()
            p.join()

        print(A[1:a+1])
    
    print('\nSuma total: ',A[a])
    
    input('\nPresiona cualquier tecla para salir...')
    cls_screen()

if __name__ == '__main__':
    main()

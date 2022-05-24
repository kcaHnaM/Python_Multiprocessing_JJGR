'''Programa 1: SUMA EREW
Estudiante: José Juan García Romero'''

import threading
import math
import time
import os

def executeThread(i,j,A):
    if (((2*j)%(math.pow(2,i))) == 0):
        A[2*j] = A[2*j] + A[((2*j)-((int) (math.pow(2,i-1))))]
    time.sleep(1)

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

    print(A)

    a = len(A)-1
    threads = []
    log = int(math.log(a,2))
    for i in range(1,log+1):
        for j in range(1,(int)(a/2)+1):
            thread = threading.Thread(target=executeThread,args=(i,j,A))
            threads.append(thread)
            thread.start()
        
        for hilo in threads:
            hilo.join()

        print(A[1:a+1])
    
    print('\nSuma total: ',A[a])
    
    input('\nPresiona cualquier tecla para salir...')
    cls_screen()

if __name__ == '__main__':
    main()

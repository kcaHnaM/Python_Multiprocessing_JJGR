'''Programa 4: Busqueda CRCW
Estudiante: José Juan García Romero'''

from concurrent.futures import process
from multiprocessing import Process
import multiprocessing
from statistics import multimode
import time
import os

def print_titulo():
    for i in range (1,41):
        print('-',end='')
    print('\n')

def cls_screen():
    if os.name == "windows" or os.name == "nt" or os.name == "dos" or os.name == "ce":
        os.system("cls")
    else:
        os.system("clear")

def process_01(Win,i):
    Win[i]=0
    
def process_02(L,Win,i,j):
    if(L[i]>L[j]):
        Win[i]=1
    else:
        Win[j]=1
    
def process_03(Win,i,ind):
    if(Win[i] == 0):
        ind[0] = i

def minCRCW(L):
    n = len(L) - 1
    Win = [None for _ in range(n+1)]
    Win[0] = 0

    processes = []

    for i in range(1, n + 1):
        p = multiprocessing.Process(target=process_01, args = (Win,i))
        p.run()
        p.start()
        p.join()
        print("Revisar Proceso 1: ",p.is_alive)
    
    processes = []

    ind = [0]
    for j in range(1, n + 1):
        i = j - 1
        p = multiprocessing.Process(target=process_02, args = (L,Win,i,j))
        p.run()
        p.start()
        p.join()
        print("Revisar Proceso 2: ",p.is_alive)
    
    processes = []

    ind = [0]

    for i in range(1, n + 1):
        p = multiprocessing.Process(target=process_03, args = (Win,i,ind))
        p.run()
        p.start()
        p.join()
        print("Revisar Proceso 3: ",p.is_alive)
    
    processes = []

    print('\n', Win)

    print('\nindice minimo es:', ind, '\nEl número más pequeño es:', L[ind[0]])
    return L[ind[0]]

def main():

    L=[95,10,6,15]    
    
    cls_screen()
    print_titulo()
    print('\tPrograma 4. Busqueda CRCW\n')
    print_titulo()
    
    print ('Vector original: ', L)

    print ('\n\t\tBusqueda:\n')
    minCRCW(L)

    input('\nPresiona cualquier tecla para salir...')
    cls_screen()

if __name__ == '__main__':
    main()
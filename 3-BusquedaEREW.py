'''Programa 3: Búsqueda EREW
Estudiante: José Juan García Romero'''

from os import system
import sys
import threading
import math
import time
import os

inf = 100000

def executeThreadBroadCast(i,j,A):
    A[j] = A[(j - 2**(i-1) )]

def executeThreadMinimo(L,i):
    if(L[2*i-1] > L[2*i] ):
        L[i] = L[2*i]
    else:
        L[i] = L[2*i-1]


def executeThreadBusqueda(L,Laux,i):
    if(L[i] == Laux[i]):
        Laux[i] = i
    else:
        Laux[i] = inf

def BroadCast(A, x,k):
    threads = []
    A[1] = x
    for i in range(1,k+1):
        for j in range( 2**(i-1) + 1,  2**i+1):
            thread = threading.Thread(target=executeThreadBroadCast,args=(i,j,A))
            threads.append(thread)
            thread.start()

        for hilo in threads:
            hilo.join()

def minimo(L,N):
    threads = []
    lg = int( math.log(N,2) )
    for j in range(1,lg+1):
        for i in range(1, int(N/2**j)+1):
            thread = threading.Thread(target=executeThreadMinimo,args=(L,i))
            threads.append(thread)
            thread.start()

        for hilo in threads:
            hilo.join()

    return L[1]

def busquedaErew(L,x):
    threads = []
    Laux = []
    for i in range(0, N+1):
        Laux.append(x)
    Laux[0] = inf
    BroadCast(Laux, x, k)

    for i in range(1,N+1):
        thread = threading.Thread(target=executeThreadBusqueda,args=(L,Laux,i))
        threads.append(thread)
        thread.start()

        for hilo in threads:
            hilo.join()

    imin = minimo(Laux,N)
    return imin

def print_titulo():
    for i in range (1,41):
        print('-',end='')
    print('\n')

def cls_screen():
    if os.name == "windows" or os.name == "nt" or os.name == "dos" or os.name == "ce":
        os.system("cls")
    else:
        os.system("clear")

L = [0,15,-70,63,-78,102,145,-36,90,14,2,-97,-400,1,410,34,-51]

N = len(L)-1
k = int(math.log(N,2))


cls_screen()
print_titulo()
print('\tPrograma 3. BUSQUEDA EREW\n')
print_titulo()
time.sleep(1)
print('Vector Ingresado: \n')
print(L)
time.sleep(1)
x = int(input('\nIngrese el número a buscar: '))
indice = busquedaErew(L,x)
print('\nEl número ',x,' se encuentra en la posición: ',indice)
input('\nPresiona cualquier tecla para salir...')
cls_screen()
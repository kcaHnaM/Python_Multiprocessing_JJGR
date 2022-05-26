'''Programa 2: SUMA CREW
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

def p1(Win,i):
    Win[i]=0
    
def p2(L,Win,i,j):
    if(L[i]>L[j]):
        Win[i]=1
    else:
        Win[j]=1
    
def p3(Win,i,ind):
    if(Win[i]==0):
        ind[0]=i


def main():
    L=[]
    
    i=1
    Win=[1,1,1,1,1,1,1,1,1,1,1,1,1]
    ind=[1000000000000000000000000]


    cls_screen()
    print_titulo()
    print('\tPrograma 4. Busqueda CRCW\n')
    print_titulo()

    x=int(input('Numero de datos a ingresar: '))
    print('\n')

    for i in range (x):
        datos=int(input('Valor: '))
        L.append(datos)
    
    cls_screen()
    print_titulo()
    print('\tPrograma 4. Busqueda CRCW\n')
    print_titulo()
    
    i=0
    n=len(L)

    


    while(i<n):
        if(i>=0):
            p = multiprocessing.Process(target=p1, args = (Win,i))
            p.run()
            p.start()
            p.join()
            print("Revisar Proceso: ",p.is_alive)
        i=i+1
    i=0
    j=i+1

    print ('\t\tPROCESO 1:\n')
    print ('Vector original: ', L)
    print ('\n',Win[:x])

    while(j<n):
        if(i<j):
            if(i>=0):
                p = multiprocessing.Process(target=p2, args = (L,Win,i,j))
                p.run()
                p.start()
                p.join()
                print("Revisar Proceso: ",p.is_alive)
        i=i+1
        j=j+1
    i=0
    print ('\n\t\tPROCESO 2:\n')
    print (Win[:x])



    while(i<n):
        if(i>=0):
            p = multiprocessing.Process(target=p3, args = (Win,i,ind))
            p.run()
            p.start()
            p.join()
            print("Revisar Proceso: ",p.is_alive)
            i=i+1

    print ('\n\t\tPROCESO 3:\n')
    print ('Señalando el valor minimo con un cero en el vector 0\n\n', Win[:x])

            
    print ('\n\nEl valor minimo es:  ', L[ind[0]])

    input('\nPresiona cualquier tecla para salir...')
    cls_screen()

if __name__ == '__main__':
    main()
'''Programa 1: SUMA EREW
Estudiante: José Juan García Romero'''

import math
from multiprocessing import Process
import multiprocessing

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

    print("El arreglo es: ", a)
    p = multiprocessing.Process(ordCRCW(a,c,n,b))
    p.run()
    p.start()
    p.join()
    print("Revisar Proceso: ",p.is_alive)

if __name__ == '__main__':
    main()
'''Programa 1: SUMA EREW
Estudiante: José Juan García Romero'''

import math
import  threading

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
    n = 4

    print("El arreglo es: ", a)
    thread = threading.Thread(ordCRCW(a,c,n,b))
    thread.start()
    thread.join()

if __name__ == '__main__':
    main()
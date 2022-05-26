'''Programa 7:  MULTIPLICACIÓN DE MATRICES
Estudiante: José Juan García Romero'''

from multiprocessing import Process
import multiprocessing
import math
#import time
import numpy as np
import os

def print_titulo():
    for i in range (1,55):
        print('-',end='')
    print('\n')

def cls_screen():
    if os.name == "windows" or os.name == "nt" or os.name == "dos" or os.name == "ce":
        os.system("cls")
    else:
        os.system("clear")

def MatMultCREW(A, B, C, i, j, k):
    C[i][j][k] = A[i][k] * B[k][j]

def suma(C, i, j, k, L):
    if ((2 * (k + 1)) % (2 ** L) == 0):
        C[i][j][2 * k] = C[i][j][2 * k] + C[i][j][2 * k - 2 ** (L)]

def MultiplicacionCREW(A, B, C, N):
    processes = []
    log = int(math.log(N, 2))

    for i in range(0, N):
        for j in range(0, N):
            for k in range(0, N):
                p1 = multiprocessing.Process(target=MatMultCREW, args=(A, B, C, i, j, k))
                processes.append(p1)
                p1.run()
                p1.start()
                p1.join()

            processes = []

    for L in range(0, log):
        for i in range(0, N):
            for j in range(0, N):
                for k in range(0, int(N / 2)):
                    p2 = multiprocessing.Process(target=suma, args=(C, i, j, k, L))
                    processes.append(p2)
                    p2.run()
                    p2.start()
                    p2.join()

                processes = []

def Aux(N):
    C = []
    m_aux = 0
    for i in range(0, N):
        aux0 = []
        for j in range(0, N):
            aux1 = []
            for k in range(0, N):
                aux1.append(m_aux)
                m_aux += 1
            aux0.append(aux1)
        C.append(aux0)
    return C

def Matriz(M):
    cad = ""
    for i in range(0, N):
        aux0 = []
        for j in range(0, N):
            aux1 = []

            for k in range(0, N):
                cad += str(M[i][j][k]) + ', '

            cad += '\t'

        cad += '\n'
    print("\nMatriz:")
    print(cad)

def ResultadoDeMatriz(M):
    cad = ""
    for i in range(0, N):
        aux0 = []
        for j in range(0, N):
            aux1 = []
            for k in range(0, 1):
                cad += (' '+str(M[i][j][k])+' ')

            #cad += '\t'

        cad += '\n'

    print('Resultado:')
    print(cad)

A = np.array([[1,2],[3,4]])
B = np.array([[4,3],[2,1]])
N = 2
C = Aux(N)

def main():

    cls_screen()
    print_titulo()
    print('\tPrograma 7. Multiplicación De Matrices\n')
    print_titulo()

    #time.sleep(2)
    print("Matriz A:")
    print(A)
    #time.sleep(2)
    print('\n')
    print("Matriz B:")
    print(B)
    #time.sleep(2)
    print('\n')

    MultiplicacionCREW(A, B, C, N)

    ResultadoDeMatriz(C)
    input('\nPresiona cualquier tecla para salir...')
    cls_screen()

if __name__ == '__main__':
    main()
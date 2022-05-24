'''Programa 1: SUMA EREW
Estudiante: José Juan García Romero'''

import threading
import time

def thread01(a, i, odd, even):
    a[2 * i] = odd[i]
    a[2 * i + 1] = even[i]

def thread02(a, i, Laux):
    if (a[2 * i + 1] < a[2 * i]):
        a[2 * i + 1], a[2 * i] = interchange(a[2 * i + 1], a[2 * i])

def interchange(b, c):
    aux = b
    b = c
    c = aux
    return b, c

def oddEvenSplit(a):
    n = len(a)
    aux = int(n / 2)
    b = a[0:aux]
    c = a[aux:n]
    return (b, c)

def oddEvenMergePRAM(a):
    n = len(a)
    if n == 2:
        if (a[0] > a[1]):
            a[0], a[1] = interchange(a[0], a[1])
    else:
        odd, even = oddEvenSplit(a)
        oddEvenMergePRAM(odd)
        oddEvenMergePRAM(even)
        return (odd, even)

def main():
    a = [16, 22, 35, 40, 55, 66, 70, 85, 15, 18, 23, 53, 60, 69, 72, 78]

    print()

    print('Arreglo original: ', a)

    oddEvenMergePRAM(a)
    odd, even = oddEvenMergePRAM(a)
    n = len(a)

    for i in range(0, int(n / 2)):
        thread = threading.Thread(target=thread01, args=(a, i, even, odd))
        thread.start()
        thread.join()

    lCopy = a.copy()
    for i in range(0, int(n / 2)):
        thread = threading.Thread(target=thread02, args=(a, i, lCopy))
        thread.start()
        thread.join()
    print()
    print('Ordenando el arreglo')
    print()
    print(oddEvenMergePRAM(even))
    print(oddEvenMergePRAM(odd))
    print(oddEvenSplit(a))
    print(oddEvenMergePRAM(a))
    print()
    print('Arreglo Ordenado: \n', a)
    print()
    time.sleep(2)


if __name__ == '__main__':
    main()
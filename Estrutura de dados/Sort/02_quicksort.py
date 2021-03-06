'''
Monte uma função quebra em dois 
que recebe uma lista L e um numero D

Ela devolve duas listas: uma dos numeros de L menores que D
e a outra, dos numeros de L maiores que D
'''


def quebra_em_dois(lista,divisor):
    maiores = []
    menores = []
    for i in range(len(lista)):
        if lista[i] < divisor:
            menores.append(lista[i])
        else:
            maiores.append(lista[i])
    return menores, maiores

'''
Implemente o quicksort: 

Um algoritmo recursivo de ordenação que, dada uma lista,

separa o primeiro elemento D

"quebra" o resto da lista em numeros menores que D e 
numeros maiores de D

Ordena os maiores e os menores (recursivamente)

Retorna uma lista com os menores (ordenados), 
depois D, depois os maiores (ordenados)

(qual um bom "caso base" ou "caso simples" ?)
'''

def quicksort(lista):
    if len(lista) == 1 or len(lista) == 0:
        return lista
    else:
        first = lista[0]
        i = 0
        for j in range(len(lista)-1):
            if lista[j+1] < first:
                lista[j+1],lista[i+1] = lista[i+1], lista[j+1]
                i += 1
        lista[0],lista[i] = lista[i],lista[0]
        left = quicksort(lista[:i])
        right = quicksort(lista[i+1:])
        left.append(lista[i])
        return left + right
    return lista
    print(lista)


'''
Volte para o arquivo de testes de tempos, e teste 
o tempo do quicksort junto com os tempos 
do mergesort e do selectionsort
'''

import unittest

class TestStringMethods(unittest.TestCase):

    def test_00_quebra(self):
        self.assertEqual(
          quebra_em_dois([1,2,3,4,5,5,6,7],4),
          ([1, 2, 3], [4, 5, 5, 6, 7]))

        self.assertEqual(
          quebra_em_dois([10,20,30,40,5,5,6,7],4),
          ([], [10, 20, 30, 40, 5, 5, 6, 7]))

        self.assertEqual(
          quebra_em_dois([10,20,30,40,5,5,6,7],100),
          ([10, 20, 30, 40, 5, 5, 6, 7], []))

    def test_01_quicksort(self):
        self.assertEqual(
          quicksort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]), 
          [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50])
        self.assertEqual(
          quicksort([46,1,18,35,18,9,6,26,47,24,4,29,38,26,30,23,49,5,44,6]), 
          [1, 4, 5, 6, 6, 9, 18, 18, 23, 24, 26, 26, 29, 30, 35, 38, 44, 46, 47, 49])
        self.assertEqual(
          quicksort( [1,5,15,20,18,30,35,35,38,45,47,48,50]), 
          [1,5,15,18,20,30,35,35,38,45,47,48,50])

    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


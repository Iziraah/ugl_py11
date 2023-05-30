# Создайте класс Матрица.
# Добавьте методы для:
#   вывода на печать,
#   сравнения,
#   сложения,
#   *умножения матриц (транспорирование)


import copy
from random import randint


class Matrix:
    def __init__(self, a, b) -> None:
        self.a = a # строки
        self.b = b # столбцы
        self.arr =[[[] for i in range(self.b)] for j in range (self.a)]
                
        for i in range (self.a):
            for j in range (self.b):
                self.arr [i][j]= randint(0,10)
    
    def Print_Matrix (self):
        print ()
        for i in range(self.a):
            print(self.arr[i])
        return 
    
    def __add__(self, other):
        # if (self.a != other.a and self.b != other.b):
        #     return print("try adding some another matrices")
        
        m = Matrix(self.a, other.b)
        m.arr =[[[] for i in range(self.b)] for j in range (self.a)]
        
        for i in range (self.a):
            for j in range (other.b):
                m.arr[i][j]= self.arr[i][j] + other.arr[i][j]
        return m
    
    def __eq__(self, other):
        return self is other
    
    def transpone(self):
        m = Matrix(self.b, self.a)
        m.arr =[[[] for i in range(self.b)] for j in range (self.a)]
        for i in range (self.a):
            for j in range (self.b):
                m.arr[i][j]= self.arr[j][i]
        return m
    
    def __mul__(self, other):
        if (self.a != other.b):
            return print("try multiplying some another matrices")
        m = Matrix(self.a, other.b)
        m.arr =[[[] for i in range(self.b)] for j in range (self.a)]
        for i in range (self.a):
            for j in range (self.b):
                for k in range(other.a):
                    m.arr[i][j]= self.arr[i][k] + other.arr[k][j]
        return m
        
        
    
m1 = Matrix(4,4)
m1.Print_Matrix()
m2 = Matrix(3,4)
m2.Print_Matrix()
# m3 = m1 + m2
# m3.Print_Matrix()
print(m1 == m2)
m4 = m1.transpone()
m4.Print_Matrix()
m5 = m1 * m2
# m5.Print_Matrix()
    
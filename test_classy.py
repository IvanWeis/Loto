import pytest
from classy import Bag

def test_set():            # тестирующая функция проверяет в классе Bag Метод set (список 90 чисел)
    bag = Bag()            # создаем объект bag  класса Bag
    ostatok = bag.set()    # в переменную ostatok записываем массив из 90 случайных неповторяющихся чисел
    assert len(ostatok) == 90  # проверяем, что длина массива равна 90
    assert ostatok[1] != ostatok[2]  # проверяем на неповторяемость

def test_de_set():          # тестирующая функция проверяет в классе Bag Метод de-set (удаление одного)
    bag = Bag()             # создаем объект bag  класса Bag
    ostatok = bag.set()     # в переменную ostatok записываем массив из 90 случайных неповторяющихся чисел
    ostatok = bag.de_set(ostatok)  # удаляем первый элемент массива
    assert len(ostatok) == 89  # проверяем, что длина массива уменьшилась на 1 и стала равна 89
   
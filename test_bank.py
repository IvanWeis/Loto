# ТЕСТИРУЕМ КЛАСС Bill (проверяем его Свойства и Методы) с помощью unittest
import unittest
from bill01 import Bill

class TestBill(unittest.TestCase):
    def test_init(self):  # проверяем Свойства  money  и   history
        bill = Bill()     # создаем новый объект  bill  класса Bill
        self.assertEqual(bill.money, 0) # проверяем, что money равно нулю (т.к. только что создали)
        self.assertEqual(len(bill.history), 0) # длина списка histoty нулевая, т.е. history пустая

    def test_add(self):  # проверяем Метод пополнения счета
        bill = Bill()    # создаем новый объект  bill  класса Bill
        bill.add(100)    # пополняем счет на 100  с помощью Метода add (добавляем к money 100)
        self.assertEqual(bill.money, 100) # проверяем, что свойство money равно 100

    def test_buy(self):  # проверяем Метод осуществления закупки
        bill = Bill()    # создаем новый объект  bill  класса Bill
        bill.add(100)    # пополняем счет на 100 (чтобы можно было совершить покупку)
        bill.buy(50, 'Чемодан')  # счет (money) уменьшаем на 50, формируем историю покупок (history)
        self.assertEqual(bill.money, 50) # проверяем, что свойство money равно 50 (100 - 50)
        self.assertEqual(bill.history, [('Чемодан', 50)]) # проверяем историю покупок

    def test_add_history(self): # проверяем Метод записи истории из переменной, значение которой берем из файла
        bill = Bill()   # создаем новый объект  bill  класса Bill
        hist = [50, 'Кресло']   # в переменную hist записываем покупку Кресла за  50
        bill.add_history(hist)  # записываем в историю (history) покупку Кресла (значение переменной hist)
        self.assertEqual(bill.history, [50, 'Кресло']) # проверяем равенство history покупке Кресла за 50

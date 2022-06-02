import json
import os.path
from bill01 import Bill  # из модуля bill01 импортировал класс Bill

my_bill = Bill()  # создал конкретный счет как объект класса Bill (унаследовав его свойства и методы)

# ОПИСАЛ ФУНКЦИЮ bank() с применением объекта my_bill
def bank():
    # Готовим переменные и считываем из файлов необходимую информацию
    money = 0  # обнуляем остаток денег на счету
    history = []  # в данном списке храним историю покупок
    if os.path.exists('file_remains.txt'): # если такой файл существует
        f = open('file_remains.txt', 'r')  # открываем файл
        money = int(f.read()) # счмтываем из файла остаток денег на счете
        f.close() # закрываем файл
        my_bill.add(money)  # записываем исходный остаток счета в свойство money
    if os.path.exists('file_history.json'): # если такой файл существует
        with open('file_history.json', 'r') as f:
            history = json.load(f) # считываем из файла историю покупок
        f.close() # закрываем файл
        my_bill.add_history(history) # записываем исходную историю, прочитанную из файла в свойство history
    while True:             # бесконечный цикл организует меню
        print()                        # печатаем пустую строку (для удобства восприятия)
        print('  У Вас на счету: ', my_bill.money) # печатаем значение свойства money
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':  # пополнение счета с проверкой на ошибку
            while True: # если в блоке try ошибки, то выполняем код блока except, иначе - пропускаем блок except
                count = 0   # объявляем переменную для хранения величины пополнения счета
                print("У Вас на счету: ", my_bill.money) # выводим на экран текущее состояние счета
                try:
                    # тот код, который может вызвать исключение (ошибку) при вводе текста вместо числа
                    count = int(input("Введите сумму пополнения счета: "))
                    break    # если все хорошо, то выходим из цикла  while True (пополнение счета)
                except:
                    # часть программы, которая будет выполняться при возникновении исключения (ошибки)
                    print("Вы ввели не число")
            my_bill.add(count)  # если правильно введено число, то увеличиваем счет на величину count
            print("У Вас на счету: ", money) # выводим на экран новое состояние счета
        elif choice == '2':
            name = input("Введите Наименование товара: ") # вводим наименование
            count = int(input("Введите Стоимость товара: "))
            my_bill.buy(count, name) # покупка - уменьшаем счет и дописываем историю покупок
        elif choice == '3':
            print("История Ваших покупок: ")  # вывод истории покупок
            print(my_bill.history) # печатаем свойство history
        elif choice == '4':  # ВЫход. Передвыходом сохраняем в файлы остаток на счете и историюпокупок
            f = open('file_remains.txt', 'w') # открываем файл на запись
            f.write(str(my_bill.money)) # записываем в виде текста остаток денег (свойство main)
            f.close()  # закрываем файл
            with open('file_history.json', 'w') as f: # открываем файл на запись
                json.dump(my_bill.history, f) # записываем в виде текста историю покупок
            break                             # выход из программы
        else:
            print('Неверный пункт меню')

# ИСПОЛНЯЕМАЯ ЧАСТЬ ПРОГРАММЫ:
if __name__ == '__main__':
    bank() # вызываем функциюю bank()
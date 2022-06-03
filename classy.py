# СОЗДАЕМ Два КЛАССА  Kart - карточка  Bag - мешок с бочонками
import random  # импортируем библиотеку, необходимую длягенерирования случайных чисел

# Класс Kart получает исходный массив spisok и преобразует его для печати в 3 строки
class Kart:  # создаем класс Kart
    def __init__(self):        # Свойство
        self.spisok = []       # задаем свойство spisok  класса Kart
    def add(self, new_kart):   # загрузить в свойство spisok массив new_kart ПОСТРОЧНО  Метод
        self.spisok = str(new_kart[0:9]) + '\n' + str(new_kart[9:18]) + '\n' + str(new_kart[18:28])

# Класс Bag (мешок) формирует массив из 90 бочонков в случайном порядке bag_list (Метод set)
# удаляет вынутый бочонок из массива (Метод de_set)
class Bag:   # создаем класс Bag
    def __init__(self):        # Свойство
        self.bag_list = []     # задаем свойство bag_list  класса Bag

    def set(self):     # кладем в мешок 90 бочонков  Метод
        bag_list = []  # создаем пустой список случайных чисел
        while len(bag_list) < 90:        # делаем пока длина массива bag_list меньше 89 (90 раз)
            num = random.randint(1, 90)  # генерируем целое случайное число из интервала от 1 до 90
            if num not in bag_list:      # если num не содержится в bag_list (неповторяемость)
                bag_list.append(num)     # добавляем num в bag_list
        return bag_list # возвращает сформированный список неповторяющихся случ. чисел

    def de_set(self, t_list): # удаляем из мешка первый бочонок
        bag_list = t_list[1:]
        return bag_list
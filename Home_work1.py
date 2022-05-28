# Домашнее задание №1
# Условный оператор: Возраст
# * Попросить пользователя ввести возраст при помощи input и положить 
#   результат в переменную
# * Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
#   учиться в детском саду, школе, ВУЗе или работать
# * Вызвать функцию, передав ей возраст пользователя и положить результат 
#   работы функции в переменную
# * Вывести содержимое переменной на экран

# age = int(input('Введите возраст: '))
# def main():
# #     Эта функция вызывается автоматически при запуске скрипта в консоли
# #     В ней надо заменить pass на ваш код
#     if age < 7:
#         print('Учиться в детсвокм саду')
#     elif 7 <= age <= 18:
#         print('идите в школу')
#     elif 19 <= age <= 25:
#         print('Идите в ВУЗ')
#     else:
#         print('Идите работать')


# if __name__ == "__main__":  
#     main()

# Домашнее задание №1
# Условный оператор: Сравнение строк
# * Написать функцию, которая принимает на вход две строки
# * Проверить, является ли то, что передано функции, строками. 
#   Если нет - вернуть 0
# * Если строки одинаковые, вернуть 1
# * Если строки разные и первая длиннее, вернуть 2
# * Если строки разные и вторая строка 'learn', возвращает 3
# * Вызвать функцию несколько раз, передавая ей разные праметры 
#   и выводя на экран результаты
#
#  line1 = 'Learn'
# line2 = 'Python'
# if isinstance(line2, str):
#     print('0')

# line1 = input()
# line2 = input()
# def lines(line1, line2):
#     if isinstance(line2, str) and isinstance(line1, str):
#         return 0
#     elif line1 == line2:
#         return 1
#     elif line1 != line2 and len(line1) > len(line2):
#         return 2
#     elif line1 != line2 and line2 == 'learn':
#         return 3

# lines(line1, line2)        

# def main():

#     Эта функция вызывается автоматически при запуске скрипта в консоли
#     В ней надо заменить pass на ваш код

#     pass

# if __name__ == "__main__":
#     main()


# Домашнее задание №1
# Цикл for: Продажи товаров
# * Дан список словарей с данными по колличеству проданных телефонов



catalog = [{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
{'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
{'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},]
# * Посчитать и вывести суммарное количество продаж для каждого товара
# * Посчитать и вывести среднее количество продаж для каждого товара
# * Посчитать и вывести суммарное количество продаж всех товаров
# * Посчитать и вывести среднее количество продаж всех товаров

def count_product(model_phone):
    sale_sum = 0
    for amount in model_phone:
        sale_sum = sale_sum + amount
    return sale_sum

def count_product_avg(model_phone):
    sale_sum = 0
    for amount in model_phone:
        sale_sum = sale_sum + amount
    return sale_sum / len(model_phone)



    
sum_all_phone = 0
avg_sum_phone = 0
for one_model in catalog:
    phone_sum = count_product(one_model['items_sold'])
    phone_avg = count_product_avg(one_model['items_sold'])
    print(f'Всего проданно {one_model["product"]}: {phone_sum}')
    print(f'Среднее колличества продаж каждого товара {round(phone_avg)}')
    sum_all_phone = sum_all_phone + phone_sum
    avg_sum_phone = avg_sum_phone + phone_avg
    
    
print(f'Общая сумма продаж {sum_all_phone}')
print(f'Среднее колличество продаж всех товаров {round(avg_sum_phone)}')

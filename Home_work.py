# Home Work
# Задание 
# Пройдите в цикле по списку ['Вася',' Маша', 'Петя',' Валера', 'Саша', 'Даша'] пока не встретиться имя 'Валера'.
# Когда найдете напишите 'Валера нашелся'

names = ['Вася',' Маша', 'Петя', 'Валера', 'Саша', 'Даша']  

# for element in names:
#     if element == 'Валера':
#         print('Валера нашелся')
#         break  # закончить цикл
while len(names) > 0:
    name = names.pop() 
    if name == 'Валера':
        print('Валера нашелся')
        break




# Exercise 2
# def find_peson(name):    
#     while True:
#         user_say = input('Скажи что-нибудь: ')
#         if user_say == 'Пока':
#             print('Ну пока')
#             break
#         else:
#             print('Сам ты {}'.format(user_say))

# # Exercise 3
# def ask_user():
#     while True:
#         state = input('Как дела?: ').capitalize()
#         if state == 'Хорошо':
#             break
#         else:
#             print('Повторяю вопрос')    
# ask_user()

# # Exercise 4
# def get_answer(ask_user):
#     while True:
#         ask_user()
# get_answer()
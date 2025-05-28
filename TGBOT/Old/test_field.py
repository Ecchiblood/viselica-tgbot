import random

words = ['моча', 'пенис', 'говно', 'еблан', 'семен']
my_string = random.choice(words)
censored_string = "*" * len(my_string)
print("Слово загадано:", censored_string)
counter = int(len(my_string)/1.3)
print("Кол-во попыток: ", counter)
coincidence_counter = 0
while counter > 0:
    character = input("Введите букву: ").lower()
    orig_list = list(my_string)
    censored_list = list(censored_string)
    for i in range(len(my_string)):
        if orig_list[i] == character:
            censored_list[i] = character
            censored_string = ''.join(censored_list)
            coincidence_counter = coincidence_counter + 1
    if coincidence_counter == 0:
        print("Такой буквы нет!")
        counter = counter - 1
        print("Кол-во попыток: ", counter)
    coincidence_counter = 0
    if my_string == censored_string:
        print("Слово угадано: ", my_string)
    else:
        print(censored_string)
print("Ты проиграл. Загаданное слово: ", my_string)
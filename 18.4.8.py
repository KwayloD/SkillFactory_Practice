string=input("Введите числа через пробел: ")
list_of_string=string.split()
try:
    L=list(map(int,list_of_string))
except ValueError as error:
    print("Не надо писать буквы!")
else:
    print(L)
finally:
    print("Выход из программы")

#Создайте скрипт, который будет в input() принимать строки, их необходимо будет конвертировать в числа, добавьте try-except, чтобы строки могли быть сконвертированы в числа.
#В случае удачного выполнения скрипта пусть выведется: «Вы ввели правильное число».
#В конце скрипта обязательно должна быть надпись «Выход из программы».
#ПРИМЕЧАНИЕ: Для отлова ошибок используйте try-except, а также блоки finally и else.
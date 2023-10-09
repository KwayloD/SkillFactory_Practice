def check_palindrome(str_):
    str_ = str_.lower()
    str_ = str_.replace(" ", "")

    if str_ == str_[::-1]:
        return True
    else:
        return False

print(check_palindrome("test"))  # False

print(check_palindrome("Кит на море не романтик"))  # True


#Напишите функцию, которая проверяет, является ли данная строка
#палиндромом или нет, и возвращает результат проверки.
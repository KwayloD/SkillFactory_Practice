# Практика по PYTHON на курсе SKILLFACTORY.
**В этом репозитории я собираю все **свои** практические работы, выполненные в процессе прохождения курса.** 
**Я сохраняю их здесь, чтобы в любой момент освежить свои знания в написании конкретного кода. Кроме того, это также служит своего рода ***портфолио*** моих работ.**
___

***ПРИМЕР ВЫПОЛНЕННЫХ МНОЮ ЗАДАНИЙ***

* Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. При этом, если человек регистрирует больше
трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа. (Задание 18.8.19)

```python
tickets = int(input("Введите колличество билетов: "))

total_cost = 0
discount = False

for i in range(tickets):
    age = int(input(f"Введите возраст посетителя №{i+1}: "))
    if age < 18:
        continue
    elif 18 <= age <= 25:
        total_cost += 990
    elif age >= 25:
        total_cost += 1390

if tickets > 3:
    discount = True
    total_cost -= total_cost * 0.1

print(f"Общая стоимость билетов: {int(total_cost)} руб.")
if discount:
    print("Вам предоставлена скидка 10%.")
```
* Напишите программу, в результате которой будет сформирован список *deposit* значений — накопленные средства за год вклада в каждом из банков. (Задание 17.7.3)

```python
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Ввод суммы под проценты
money = float(input('Введите сумму, которую вы планируете положить под проценты: '))

# Расчет и вывод накопленных средств для каждого банка
for bank, percent in per_cent.items():
    deposit_amount = int(money * percent / 100)
    print(f'Накопленные средства в банке {bank}: {deposit_amount} руб.')

# Поиск и вывод максимальной суммы
max_deposit = max(per_cent.values())
print(f'Максимальная сумма, которую вы можете заработать: {int(money * max_deposit / 100)} руб.')
```
* Программа, которая находит индекс последнего отрицательного элемента в списке.

```python
list_ = [-5, 2, 4, 8, 12, -7, 5]
index_negative = None

for i, value in enumerate(list_):
    if value < 0:
        print("Отрицательное число: ", value)
        index_negative = i  # перезаписываем значение индекса
        print("Новый индекс отрицательного числа: ", index_negative)
    else:
        print("Положительное число: ", value)
    print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
```
* Напишите функцию, которая проверяет, является ли данная строка палиндромом или нет, и возвращает результат проверки.

```python
def check_palindrome(str_):
    str_ = str_.lower()
    str_ = str_.replace(" ", "")

    if str_ == str_[::-1]:
        return True
    else:
        return False

print(check_palindrome("test"))  # False

print(check_palindrome("Кит на море не романтик"))  # True
```
* Напишите функцию, которая определяет, можно ли составить треугольник из трёх отрезков, длины которых передаются в функцию.
Например, вызов функции is_triangle(3, 4, 5) возвращает True, а вызов is_triangle(1, -4, 5) возвращает False. Напишите параметризованный тест на эту функцию,
используя фикстуру @pytest.mark.parametrize, который рассматривает все возможные варианты параметров:

```python
def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False
      
@pytest.mark.parametrize("a, b, c, expected", [
    (3, 4, 5, True),
    (1, -4, 5, False),
    (2, 2, 5, False),
    (1, 0, 3, False)
])
def test_is_triangle(a, b, c, expected):
    assert is_triangle(a, b, c) == expected
```

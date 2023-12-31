#Накопленные средства за год в банках.

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

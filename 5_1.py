from random import sample

mas = sample(range(10), 5)

ans = int(input("Введите число: "))
print(mas)
if ans in mas:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")

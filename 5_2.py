from random import randint
from collections import Counter
mas = [randint(0, 10) for _ in range(10)]
print("Список: ", mas)
c = Counter(mas)
if c.most_common()[0][1] != 1:
    print("В списке повторяются значения: ", end="")
    for i in c.most_common():
        if i[1] != 1:
            print(i[0], end=" ")
        else:
            break
else:
    print("В списке нет повторяющихся значений")





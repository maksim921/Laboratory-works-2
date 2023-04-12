from random import sample
my_gr = "Иванов", "Смирнов", "И", "Еще", "Несколько", "Фамилий", "Студентов", "Тут", "Должно", "Быть"
other_gr = "А", "Тут", "10", "Фамилий", "Ребят", "Из", "Другой", "Группы", "Петя", "Вася"

team = tuple(sample(my_gr, 5) + sample(other_gr, 5))

print(my_gr)
print(other_gr)
print(team)
print(len(team))
print(tuple(sorted(team)))
if "Иванов" in team:
    print("Ивановых в команде: ",end="")
    print(team.count("Иванов"))
else:
    print("Иванов не в команде")
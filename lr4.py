a = input("Введите название первого файла: ")
s1 = set(open(a).read().split())
b = input("Введите название второго файла: ")
s2 = set(open(b).read().split())
def union(a,b):
    return a | b
def intersection(a,b):
    return a & b
def difference(a,b):
    return a - b
def symmetric_difference(a,b):
    return a ^ b
def calculations(s1,s2):
    operations = {
        '1': ('Объединение', union(s1,s2)),
        '2': ('Пересечение', intersection(s1, s2)),
        '3': ('Разность A-B', difference(s1, s2)),
        '4': ('Симметричная разность', symmetric_difference(s1, s2)),
    }
    while True:
        for i, (name, _) in operations.items():
            print(f"Введите {i}, чтобы найти {name}")
        print("Введите 0/exit, чтобы выйти из калькулятора")
        a = input()
        if a == "0" or a == "exit":
            print("До встречи")
            break
        result = operations[str(a)][1]
        print(result)
            
calculations(s1,s2)

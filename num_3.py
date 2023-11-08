def is_natural_and_positive(num):
    if num.isnumeric() and int(num) > 0:
        try:
            num = int(num)
            return True
        except ValueError:
            print("Введено не натуральное число")
            exit()
    print("Введено не натуральное число")
    exit()


def inp(arr):
    for i in range(len(arr)):
        try:
            arr[i] = int(input(f"arr[{i}] = "))
        except ValueError:
            print("Вы ввели не целое число")
            exit()
    return arr


# Создание списка
size = input('Введите размер списка: ')
is_natural_and_positive(size)
zero_lst = [0 for i in range(int(size))]
lst = inp(zero_lst)

# Поиск моды списка
if len(lst) == len(set(lst)) and len(lst) != 1:
    print("Массив не имеет моды")
    exit()

# Поиск самых часто встречающихся чисел
k = 0
max = 0
temp = []
for i in set(lst):
    for j in lst:
        if i == j:
            k += 1
    if k > max:
        max = k
    k = 0

for i in set(lst):
    if lst.count(i) == max:
        temp.append(i)
if len(temp) > 1:
    print("Моды массива нет")
    exit()
print(f"Мода массива = {temp[0]}")

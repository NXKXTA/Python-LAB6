def inp(arr):
    for i in range(len(arr)):
        try:
            arr[i] = int(input(f"arr[{i}] = "))
        except ValueError:
            print("Вы ввели не целое число")
            exit()
    return arr


# Создание списка
try:
    array_size = int(input("Введите размер массива: "))
except ValueError:
    print("Вы ввели не целое число")
    exit()

if array_size <= 0:
    print("Вы ввели не натуральное число")
    exit()

zero_lst = [0 for i in range(array_size)]
lst = inp(zero_lst)

# Поиск моды списка
if len(lst) == len(set(lst)) and len(lst) != 1:
    # Если ввести список из одного элемента, то без второго условия программа его забракует
    print("Массив не имеет моды")
    exit()

# Поиск самых часто встречающихся чисел
k = 0
mx = 0
temp = []
for i in set(lst):
    for j in lst:
        if i == j:
            k += 1
    if k > mx:
        mx = k
    k = 0

for i in set(lst):
    if lst.count(i) == mx:
        temp.append(i)
if len(temp) > 1:
    print("Моды массива нет")
    exit()
print(f"Мода массива = {temp[0]}")

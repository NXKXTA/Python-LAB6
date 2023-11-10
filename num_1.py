def input_in_array(arr):
    i = 0
    while i < int(array_size):
        try:
            arr.append(int(input()))
            i += 1
        except ValueError:
            print("Вы ввели не целое число")
            exit()
    return arr


vector_1 = []
vector_2 = []

try:
    array_size = int(input("Введите размер векторов: "))
except ValueError:
    print("вы ввели не целое число")
    exit()

if array_size <= 0:
    print("вы ввели не натуральное число")
    exit()

print("Введите вектор 1, каждое число через Enter:")
vector_1 = input_in_array(vector_1)

print("Введите вектор 2, каждое число через Enter:")
vector_2 = input_in_array(vector_2)

print(f"Вектор 1 выглядит так: {vector_1}")
print(f"Вектор 2 выглядит так: {vector_2}")

print("Скалярное произведение = ", sum(a * b for a, b in zip(vector_1, vector_2)))

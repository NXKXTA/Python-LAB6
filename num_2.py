def matrix_multiplication(A, B):
    # Determine the matrices' dimensions.
    rows_a = len(A)
    cols_a = len(A[0])
    cols_b = len(B[0])
    # Установить матрицу результатов в нули.
    result = [[0 for _ in range(cols_b)] for __ in range(rows_a)]
    for s in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[s][j] += A[s][k] * B[k][j]
    return result


def input_in_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            try:
                arr[i][j] = int(input())
            except ValueError:
                print("Вы ввели не целое число")
                exit()
    return arr


print("Введите размеры матрицы порядка М * К и К * N")
try:
    M = int(input("Введите M:"))
    K = int(input("Введите K:"))
    N = int(input("Введите N:"))
except ValueError:
    print("Вы ввели не целое число")
    exit()

if M <= 0 or K <= 0 or N <= 0:
    print("Вы ввели не натуральное число")
    exit()

matrix_1 = [[0 for i in range(K)] for j in range(M)]
matrix_2 = [[0 for i in range(N)] for j in range(K)]

print("Введите матрицу 1: ")
matrix_1 = input_in_matrix(matrix_1)
print("Введите матрицу 2: ")
matrix_2 = input_in_matrix(matrix_2)

print("Введенные матрицы: ")
print(matrix_1, "\n")
print(matrix_2, "\n")
print("Их произведение: ")
print(matrix_multiplication(matrix_1, matrix_2))

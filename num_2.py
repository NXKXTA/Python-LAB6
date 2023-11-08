def matrix_multiplication(A, B):
    # Determine the matrices' dimensions.
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    # Установить матрицу результатов в нули.
    result = [[0 for row in range(cols_B)] for col in range(rows_A)]
    for s in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[s][j] += A[s][k] * B[k][j]
    return result


def inpm(arr):
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
matrix_1 = inpm(matrix_1)
print("Введите матрицу 2: ")
matrix_2 = inpm(matrix_2)

print("Введенные матрицы: ")
print(matrix_1, "\n")
print(matrix_2, "\n")
print("Их произведение: ")
print(matrix_multiplication(matrix_1, matrix_2))

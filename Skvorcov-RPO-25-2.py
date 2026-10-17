def validate_matrix(matrix):
    # проверяет, что матрица непустая и прямоугольная
    
    if not matrix or not matrix[0]:
        raise ValueError("Матрица не должна быть пустой")

    columns = len(matrix[0])

    if any(len(row) != columns for row in matrix):
        raise ValueError("Все строки матрицы должны иметь одинаковую длину")

    return len(matrix), columns


def matrix_add(a, b):
    # складывает две матрицы одинакового размера
    
    rows_a, cols_a = validate_matrix(a)
    rows_b, cols_b = validate_matrix(b)

    if (rows_a, cols_a) != (rows_b, cols_b):
        raise ValueError("Для сложения размеры матриц должны совпадать")

    return [
        [a[i][j] + b[i][j] for j in range(cols_a)]
        for i in range(rows_a)
    ]


def matrix_transpose(matrix):
    # меняет строки матрицы на столбцы
    validate_matrix(matrix)

    return [
        [matrix[i][j] for i in range(len(matrix))]
        for j in range(len(matrix[0]))
    ]


def matrix_multiply(a, b):
    # умножает матрицы по правилу строки на столбец
    rows_a, cols_a = validate_matrix(a)
    rows_b, cols_b = validate_matrix(b)

    if cols_a != rows_b:
        raise ValueError(
            "Число столбцов первой матрицы должно "
            "равняться числу строк второй"
        )

    return [
        [
            sum(a[i][k] * b[k][j] for k in range(cols_a))
            for j in range(cols_b)
        ]
        for i in range(rows_a)
    ]


def input_matrix(name):
    # считывает матрицу произвольного размера с клавиатуры
    rows = int(input(f"Количество строк матрицы {name}: "))
    cols = int(input(f"Количество столбцов матрицы {name}: "))

    if rows <= 0 or cols <= 0:
        raise ValueError("Размеры матрицы должны быть положительными")

    matrix = []

    for i in range(rows):
        while True:
            values = input(
                f"Строка {i + 1} ({cols} чисел через пробел): "
            ).split()

            if len(values) != cols:
                print(f"Ошибка: необходимо ввести ровно {cols} чисел.")
                continue

            try:
                matrix.append([float(value) for value in values])
                break
            except ValueError:
                print("Ошибка: вводите только числа.")

    return matrix


def print_matrix(matrix):
    # выводит матрицу в удобном табличном виде
    
    for row in matrix:
        print(" ".join(
            f"{value:g}" for value in row
        ))


if __name__ == "__main__":
    print("=== калькулятор матриц ===")
    print("1 — Сложение")
    print("2 — Транспонирование")
    print("3 — Умножение")
    print("4 — Вычислить C = (A + B^T) * A")

    choice = input("Выберите операцию: ").strip()

    try:
        match choice:
            case "1":
                a = input_matrix("A")
                b = input_matrix("B")
                result = matrix_add(a, b)

            case "2":
                a = input_matrix("A")
                result = matrix_transpose(a)

            case "3":
                a = input_matrix("A")
                b = input_matrix("B")
                result = matrix_multiply(a, b)

            case "4":
                a = input_matrix("A")
                b = input_matrix("B")
                result = matrix_multiply(
                    matrix_add(a, matrix_transpose(b)), a
                )

            case _:
                print("Неизвестная операция.")
                result = None

        if result is not None:
            print("\nРезультат:")
            print_matrix(result)

    except ValueError as error:
        print("Ошибка:", error)



# Test whether a matrix is Markov or not

def markov_test():

    n = int(input("Enter size of square matrix: "))

    matrix = []
    print("Enter matrix row by row:")

    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    print("\nMatrix:")
    for row in matrix:
        print(row)

    all_positive = True
    row_sum_one = True

    # check elements between 0 and 1
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0 or matrix[i][j] > 1:
                all_positive = False

    # check row sum = 1
    for i in range(n):
        s = sum(matrix[i])
        print("Sum of row", i+1, "=", round(s,4))
        if abs(s - 1) > 0.0001:
            row_sum_one = False

    # final result
    if all_positive and row_sum_one:
        print("\nMatrix is a Markov Matrix")
    else:
        print("\nMatrix is NOT a Markov Matrix")


markov_test()
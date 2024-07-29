def matrix_multiply(n, A, B):
    """
    Multiplies two square matrices.

    :parameter:
    --------------------------------------------------------------------
        n (int): The dimension of the square matrices.
        A (list[list[float]]): The first square matrix.
        B (list[list[float]]): The second square matrix.

    :return:
    ---------------------------------------------------------------------
        list[list[float]]: The product of matrices A and B

    """
    # Create an empty matrix to store the result
    C = [[0] * n for _ in range(n)]  # Create an empty matrix

    # Multiply matrices A and B
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def print_matrix(matrix):
    """
    Prints a matrix in a formatted way.

    :parameter:
    ----------------------------------------------------------
        matrix (list[list[float]]): The matrix to print.
    """
    # Iterate over each row in the matrix
    for row in matrix:
        formatted_row = ' '.join(f'{value:.1f}' for value in row)
        print(formatted_row)

if __name__ == "__main__":
    # Test case a
    n1 = 2
    A1 = [
        [2, 7],
        [3, 5]
    ]
    B1 = [
        [8, -4],
        [6, 6]
    ]
    result1 = matrix_multiply(n1, A1, B1)
    print(f'The product A1, B1 of the matrices: ')
    print_matrix(result1)

    # Test case b
    n2 = 3
    A2 = [
        [1, 0, 2],
        [3, -2, 5],
        [6, 2, -3]
    ]
    B2 = [
        [0.3, 0.25, 0.1],
        [0.4, 0.8, 0],
        [-0.5, 0.75, 0.6]
    ]
    result2 = matrix_multiply(n2, A2, B2)
    print(f'\nThe product A2, B2 of the matrices: ')
    print_matrix(result2)



def matrix_einlesen(ar):
    import numpy as np
    import sympy as sy

    var_e = int(ar[0][ar[0].index('e') + 1])
    var_m = int(ar[0][ar[0].index('m') + 1])

    A11 = None
    A12 = None
    x = sy.S('x')

    matrix_A = sy.Matrix([[x, x, x, 0., 0., 0.], [x, x, x, 0., 0., 0.], [x, x, x, 0., 0., 0.], [0., 0., 0., x, 0., 0.],
                          [0., 0., 0., 0., x, 0.], [0., 0., 0., 0., 0., x]])
    matrix_B = sy.Matrix([[0., 0., 0., 0., x, 0.], [0., 0., 0., x, 0., 0.], [x, x, x, 0., 0., 0.]])
    matrix_C = sy.Matrix([[x, 0., 0.], [0., x, 0.], [0., 0., x]])

    for i in range(0, len(ar)):
        ar_row = ar[i]
        if ar_row[0] == 'A' and ar_row[2] == '1' and ar_row[4] == '1':
            matrix_A[0, 0] = float(ar_row[5])
            matrix_A[1, 1] = float(ar_row[5])
            A11 = float(ar_row[5])
        if ar_row[0] == 'A' and ar_row[2] == '1' and ar_row[4] == '2':
            matrix_A[0, 1] = float(ar_row[5])
            matrix_A[1, 0] = float(ar_row[5])
            A12 = float(ar_row[5])
        if ar_row[0] == 'A' and ar_row[2] == '1' and ar_row[4] == '3':
            matrix_A[0, 2] = float(ar_row[5])
            matrix_A[2, 0] = float(ar_row[5])
            matrix_A[1, 2] = float(ar_row[5])
            matrix_A[2, 1] = float(ar_row[5])
        if ar_row[0] == 'A' and ar_row[2] == '3' and ar_row[4] == '3':
            matrix_A[2, 2] = float(ar_row[5])
        if ar_row[0] == 'A' and ar_row[2] == '5' and ar_row[4] == '5':
            matrix_A[4, 4] = float(ar_row[5])
            matrix_A[3, 3] = float(ar_row[5])
        if A11 is not None and A12 is not None:
            matrix_A[5, 5] = (A11 - A12) / (2 ** calc_vorzeichen(var_m))
        if ar_row[0] == 'B' and ar_row[2] == '3' and ar_row[4] == '1':
            matrix_B[2, 0] = float(ar_row[5])
            matrix_B[2, 1] = float(ar_row[5])
        if ar_row[0] == 'B' and ar_row[2] == '3' and ar_row[4] == '3':
            matrix_B[2, 2] = float(ar_row[5])
        if ar_row[0] == 'B' and ar_row[2] == '1' and ar_row[4] == '5':
            matrix_B[0, 4] = float(ar_row[5])
            matrix_B[1, 3] = float(ar_row[5])
        if ar_row[0] == 'C' and ar_row[2] == '1' and ar_row[4] == '1':
            matrix_C[0, 0] = float(ar_row[5])
            matrix_C[1, 1] = float(ar_row[5])
        if ar_row[0] == 'C' and ar_row[2] == '3' and ar_row[4] == '3':
            matrix_C[2, 2] = float(ar_row[5])

    return matrix_A, matrix_B, matrix_C

def matrix_rausschreiben(ar):
    import sympy as sy
    return_matrix = []
    if (ar.shape == (6, 6)):
        if (ar[0, 0] != 0. and type(ar[0, 0]) == sy.core.numbers.Float):
            return_matrix.append([1, 1, 2, 1, ar[0, 0]])
        if (ar[0, 1] != 0. and type(ar[0, 1]) == sy.core.numbers.Float):
            return_matrix.append([1, 1, 2, 2, ar[0, 1]])
        if (ar[0, 2] != 0. and type(ar[0, 2]) == sy.core.numbers.Float):
            return_matrix.append([1, 1, 2, 3, ar[0, 2]])
        if (ar[2, 2] != 0. and type(ar[2, 2]) == sy.core.numbers.Float):
            return_matrix.append([1, 3, 2, 3, ar[2, 2]])
        if (ar[4, 4] != 0. and type(ar[4, 4]) == sy.core.numbers.Float):
            return_matrix.append([1, 5, 2, 5, ar[4, 4]])

    if (ar.shape == (3, 6)):
        if (ar[2, 0] != 0. and type(ar[2, 0]) == sy.core.numbers.Float):
            return_matrix.append([1, 3, 2, 1, ar[2, 0]])
        if (ar[2, 2] != 0. and type(ar[2, 2]) == sy.core.numbers.Float):
            return_matrix.append([1, 3, 2, 3, ar[2, 2]])
        if (ar[0, 4] != 0. and type(ar[0, 4]) == sy.core.numbers.Float):
            return_matrix.append([1, 1, 2, 5, ar[0, 4]])

    if (ar.shape == (3, 3)):
        if (ar[0, 0] != 0. and type(ar[0, 0]) == sy.core.numbers.Float):
            return_matrix.append([1, 1, 2, 1, ar[0, 0]])
        if (ar[2, 2] != 0. and type(ar[2, 2]) == sy.core.numbers.Float):
            return_matrix.append([1, 3, 2, 3, ar[2, 2]])

    return return_matrix

def calc_vorzeichen(i):
    if i == 0:
        return -1
    elif i == 1:
        return 1
    else:
        return None
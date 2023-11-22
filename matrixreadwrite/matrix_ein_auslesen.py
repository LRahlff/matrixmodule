def matrix_einlesen(ar):
    import json
    import sympy as sy

    values_in = []
    for a in ar:
        values_in.append({'in_number': a['in_number'], 'value': json.loads(a['value'])})
    var_m = int(values_in[0]['value'][0])
    var_e = int(values_in[0]['value'][1])
    A11 = None
    A12 = None
    x = sy.S('x')

    matrix_A = sy.Matrix([[x, x, x, 0., 0., 0.], [x, x, x, 0., 0., 0.], [x, x, x, 0., 0., 0.], [0., 0., 0., x, 0., 0.],
                          [0., 0., 0., 0., x, 0.], [0., 0., 0., 0., 0., x]])
    matrix_B = sy.Matrix([[0., 0., 0., 0., x, 0.], [0., 0., 0., x, 0., 0.], [x, x, x, 0., 0., 0.]])
    matrix_C = sy.Matrix([[x, 0., 0.], [0., x, 0.], [0., 0., x]])

    for ar_row in values_in:
        values = ar_row['value']
        if ar_row['in_number'] == 1 and values[2] == 1 and values[3] == 1:
            matrix_A[0, 0] = float(values[4])
            matrix_A[1, 1] = float(values[4])
            A11 = float(values[4])
        if ar_row['in_number'] == 1 and values[2] == 1 and values[3] == 2:
            matrix_A[0, 1] = float(values[4])
            matrix_A[1, 0] = float(values[4])
            A12 = float(values[4])
        if ar_row['in_number'] == 1 and values[2] == 1 and values[3] == 3:
            matrix_A[0, 2] = float(values[4])
            matrix_A[2, 0] = float(values[4])
            matrix_A[1, 2] = float(values[4])
            matrix_A[2, 1] = float(values[4])
        if ar_row['in_number'] == 1 and values[2] == 3 and values[3] == 3:
            matrix_A[2, 2] = float(values[4])
        if ar_row['in_number'] == 1 and values[2] == 5 and values[3] == 5:
            matrix_A[4, 4] = float(values[4])
            matrix_A[3, 3] = float(values[4])
        if A11 is not None and A12 is not None:
            matrix_A[5, 5] = (A11 - A12) / (2 ** calc_vorzeichen(var_m))
        if ar_row['in_number'] == 2 and values[2] == 3 and values[3] == 1:
            matrix_B[2, 0] = float(values[4])
            matrix_B[2, 1] = float(values[4])
        if ar_row['in_number'] == 2 and values[2] == 3 and values[3] == 3:
            matrix_B[2, 2] = float(values[4])
        if ar_row['in_number'] == 2 and values[2] == 1 and values[3] == 5:
            matrix_B[0, 4] = float(values[4])
            matrix_B[1, 3] = float(values[4])
        if ar_row['in_number'] == 3 and values[2] == 1 and values[3] == 1:
            matrix_C[0, 0] = float(values[4])
            matrix_C[1, 1] = float(values[4])
        if ar_row['in_number'] == 3 and values[2] == 3 and values[3] == 3:
            matrix_C[2, 2] = float(values[4])

    return matrix_A, matrix_B, matrix_C, var_m, var_e

def matrix_rausschreiben(ar, m, e):
    import sympy as sy
    import json
    return_matrix = []
    if (ar.shape == (6, 6)):
        if (ar[0, 0] != 0. and type(ar[0, 0]) == sy.core.numbers.Float):
            return_matrix.append({'m': m, 'e': e, 'zeile': 1, 'spalte': 1, 'A': float(ar[0, 0])})
        if (ar[0, 1] != 0. and type(ar[0, 1]) == sy.core.numbers.Float):
            return_matrix.append({'m': m, 'e': e, 'zeile': 1, 'spalte': 2, 'A': float(ar[0, 1])})
        if (ar[0, 2] != 0. and type(ar[0, 2]) == sy.core.numbers.Float):
            return_matrix.append({'m': m, 'e': e, 'zeile': 1, 'spalte': 3, 'A': float(ar[0, 2])})
        if (ar[2, 2] != 0. and type(ar[2, 2]) == sy.core.numbers.Float):
            return_matrix.append({'m': m, 'e': e, 'zeile': 3, 'spalte': 3, 'A': float(ar[2, 2])})
        if (ar[4, 4] != 0. and type(ar[4, 4]) == sy.core.numbers.Float):
            return_matrix.append({'m': m, 'e': e, 'zeile': 5, 'spalte': 5, 'A': float(ar[4, 4])})

    if (ar.shape == (3, 6)):
        if (ar[2, 0] != 0. and type(ar[2, 0]) == sy.core.numbers.Float):
            return_matrix.append({'m': m, 'e': e, 'zeile': 3, 'spalte': 1, 'B': float(ar[2, 0])})
        if (ar[2, 2] != 0. and type(ar[2, 2]) == sy.core.numbers.Float):
            return_matrix.append({'m': m, 'e': e, 'zeile': 3, 'spalte': 3, 'B': float(ar[2, 2])})
        if (ar[0, 4] != 0. and type(ar[0, 4]) == sy.core.numbers.Float):
            return_matrix.append({'m': m, 'e': e, 'zeile': 1, 'spalte': 5, 'B': float(ar[0, 4])})

    if (ar.shape == (3, 3)):
        if (ar[0, 0] != 0. and type(ar[0, 0]) == sy.core.numbers.Float):
            return_matrix.append({'m': m, 'e': e, 'zeile': 1, 'spalte': 1, 'C': float(ar[0, 0])})
        if (ar[2, 2] != 0. and type(ar[2, 2]) == sy.core.numbers.Float):
            return_matrix.append({'m': m, 'e': e, 'zeile': 3, 'spalte': 3, 'C': float(ar[2, 2])})
    return json.dumps(return_matrix)

def calc_vorzeichen(i):
    if i == 0:
        return -1
    elif i == 1:
        return 1
    else:
        return None
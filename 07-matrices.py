
def zero_matrix(m,n):
    zero_row = [0] * m
    return [zero_row] * n

def identity_matrix(n):
    result = []
    for i in range(n):
        row = ([0] * i) + [1] + ([0] * (n-i-1))
        result.append(row)
    return result

def number_of_rows(A):
    return len(A)
def number_of_columns(A):
    return len(A[0])
# formula: (A+B)[i][j] = A[i][j] + B[i][j]
def add_matrices(A,B):
    assert number_of_rows(A) == number_of_rows(B)
    assert number_of_columns(A) == number_of_columns(B)
    result = []
    for i in range(number_of_rows(A)):
        row = []
        for j in range(number_of_columns(A)):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result
def transpose(A): return list(zip(*A))

A0 = [[3,4,5],[1,2,6]]
B0 = [[3,3,3],[1,1,1]]
# [[6, 7, 8], [2, 3, 7]]
print(transpose(A0))
# print(add_matrices(A0,B0))
# print (identity_matrix(3))


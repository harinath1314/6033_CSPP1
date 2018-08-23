rows=2
columns=4

mat_mul = []
for i in range(rows):
    mat_mul.append([])
for i in range(rows):
    for j in range(columns):
        mat_mul[i].append(j)
        mat_mul[i][j] = 0
print(mat_mul)

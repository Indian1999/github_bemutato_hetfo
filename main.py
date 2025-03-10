def generate_matrix(n, m):
    return [[0 for j in range(m)] for i in range(n)]

matrix = generate_matrix(4, 6)
for row in matrix:
    print(row)
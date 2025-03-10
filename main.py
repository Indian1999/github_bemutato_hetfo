import random
import matplotlib.pyplot as plt

def generate_matrix(n, m):
    return [[0 for j in range(m)] for i in range(n)]

matrix = generate_matrix(10, 10)
for row in matrix:
    print(row)
    
for i in range(1, 101):
    row = random.randrange(0, len(matrix))
    col = random.randrange(0, len(matrix[row]))
    matrix[row][col] = i
    
    
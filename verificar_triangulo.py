def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print("Digite valores para os lados de um triângulo !")
a = input("Lado a = ")
b = input("Lado b = ")
c = input("Lado c = ")
print("O triângulo de lados a:", a, " b:", b, " c:", c, " é ", is_a_triangle(a, b, c))

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
cp_list = []

for elemento in my_list:
    if elemento not in cp_list:
        cp_list.append(elemento)

my_list = cp_list[:]

print("A lista com os elementos exclusivos aqui")
print(my_list)
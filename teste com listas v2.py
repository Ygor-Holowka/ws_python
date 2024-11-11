my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 9]
invertida = my_list[::-1]
count = 0
tamanho = len(my_list)
removedor = False
while (count < tamanho):    
    for i in range(tamanho):        
        for j in range(tamanho):
            if my_list[i] == my_list[j] and i != j and j > i:
                print(my_list[i], ".", i, my_list[j], ".", j)
                removedor = True
                break
        if removedor: break
    if removedor:
        del my_list[j]
        tamanho = len(my_list)
        removedor = False
    count += 1    

print("A lista com os elementos exclusivos aqui")
print(my_list)
    


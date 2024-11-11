my_tup = (1, 2, 3)
print(my_tup[2])
##
tup = 1, 2, 3
a, b, c = tup
 
print(a * b * c)
##
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2) # duplicatas de 2
 
print(duplicates) # saídas: 4
##
d1 = {'Adão Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):   # faz a leitura dos itens no dicionários d1 e d2
    d3.update(item)     # insere o item no dicionário d3

print(d3)
##
my_list = ["car", "Ford", "flor", "Tulip"]

t = tuple(my_list) # convertentendo lista em tupla
print(t)
##
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors) # convertendo tuplas em dicionários
print(colors_dictionary)
##
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy() # se fizer isso em uma lista, ambas apontam para o mesmo lugar
my_dictionary.clear()
 
print(copy_my_dictionary) # uma lista estaria vazia, mas dicionários não
##  
colors = {
    "branco": (255, 255, 255),
    "cinza": (128, 128, 128),
    "vermelho": (255, 0, 0),
    "verde": (0, 128, 0)
    } # declaração com muitos itens, RECUO SUSPENSO
 
for col, rgb in colors.items(): # imprime tuplas que são formados por valor e sua referência
    print(col, ":", rgb)
##

estoque = []

n_registros = int(input("Quantos registros deseja criar"))

for x in range(n_registros):
    codigo_item = int(input("Código do produto: "))
    nome_item = input("Nome do item: ")
    valor_item = float(input("Valor do item: "))
    aux_estoque = [codigo_item, nome_item, valor_item]
    estoque.append(aux_estoque)

print("Quantidade de itens na lista: ", len(estoque))

for n in estoque:
    codigo_item = n[0]
    nome_item = n[1]
    valor_item = n[2]
    print("Produto:", nome_item, "   Código:", codigo_item, "   Valor item:", valor_item)
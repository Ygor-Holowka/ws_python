while True:
    try:
        value = int (input('Insira um número natural:')) 
        print('O recíproco de', value, 'é', 1 / value) 
    except ValueError:
        print('Não sei o que fazer.' ) 
    except ZeroDivisionError:
        print('Divisão por zero não é permitida em nosso universo.') 
    except: 
        print('algo de estranho aconteceu aqui ... Desculpe! ')

    sair = input("Digite 'q' para sair: ")
    if sair == 'q': break
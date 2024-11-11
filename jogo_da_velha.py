from colorama import Fore, Back, Style
import random
T = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
contador = 1

def quadrante():
    global T 
    y = 1
    count = 0
    while count < 3:
        count += 1
        print(Back.RED + "+-------+-------+-------+" + Back.RESET)
        print(Back.RED + "|       |       |       |" + Back.RESET)
        print(Back.RED + "|  ",  T[y], "  |  ", T[y+1], "  |  ", T[y+2], "  |" + Back.RESET)
        print(Back.RED + "|       |       |       |" + Back.RESET)
        y += 3        
    print(Back.RED + "+-------+-------+-------+" + Back.RESET)
    

def marcarXouO():
    global T
    global contador 
    global marcador
    acabou = False
    
    while True and contador < 10:
        try:
            if contador % 2 != 0:
                marcador = int(input("Escolha uma posição para marcar X: "))
                if marcador > 0 and marcador < 10:
                    if T[marcador] == 'X' or T[marcador] == 'O':
                        print(Fore.RED + Style.BRIGHT + "!! Posição já ocupada, escolha outra !!" + Style.RESET_ALL + Fore.RESET)
                        continue
                    else:
                        T[marcador] = 'X'
                        quadrante()
                        contador += 1
            else:
                marcador = random.randint(1,9)
                if marcador > 0 and marcador < 10:
                    if T[marcador] == 'X' or T[marcador] == 'O':
                        ## print(Fore.RED + Style.BRIGHT + "!! Posição já ocupada, escolha outra !!" + Style.RESET_ALL + Fore.RESET)
                        continue
                    else:
                        T[marcador] = 'O'
                        quadrante()
                        print("Computador fez jogada !!")
                        contador += 1
        except:
            print(Fore.RED + Style.BRIGHT + "Digite algo entre 1 e 9" + Style.RESET_ALL + Fore.RESET)
                
        acabou = verificador()
        if acabou: break
        
def verificador():
    if (T[1] == 'X' and T[2] == 'X' and T[3] == 'X') or (T[1] == 'O' and T[2] == 'O' and T[3] == 'O'): 
        if T[1] == 'X':
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'X' GANHOU" + Style.RESET_ALL + Fore.RESET)
            return True
        else:
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'O' GANHOU" + Style.RESET_ALL + Fore.RESET)   
            return True
    elif (T[4] == 'X' and T[5] == 'X' and T[6] == 'X') or (T[4] == 'O' and T[5] == 'O' and T[6] == 'O'): 
        if T[4] == 'X':
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'X' GANHOU" + Style.RESET_ALL + Fore.RESET)
            return True
        else:
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'O' GANHOU" + Style.RESET_ALL + Fore.RESET)   
            return True
    elif (T[7] == 'X' and T[8] == 'X' and T[9] == 'X') or (T[7] == 'O' and T[8] == 'O' and T[9] == 'O'): 
        if T[7] == 'X':
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'X' GANHOU" + Style.RESET_ALL + Fore.RESET)
            return True
        else:
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'O' GANHOU" + Style.RESET_ALL + Fore.RESET)   
            return True    
    elif (T[1] == 'X' and T[4] == 'X' and T[7] == 'X') or (T[1] == 'O' and T[4] == 'O' and T[7] == 'O'): 
        if T[1] == 'X':
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'X' GANHOU" + Style.RESET_ALL + Fore.RESET)
            return True
        else:
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'O' GANHOU" + Style.RESET_ALL + Fore.RESET)   
            return True
    elif (T[2] == 'X' and T[5] == 'X' and T[8] == 'X') or (T[2] == 'O' and T[5] == 'O' and T[8] == 'O'): 
        if T[2] == 'X':
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'X' GANHOU" + Style.RESET_ALL + Fore.RESET)
            return True
        else:
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'O' GANHOU" + Style.RESET_ALL + Fore.RESET)   
            return True
    elif (T[3] == 'X' and T[6] == 'X' and T[9] == 'X') or (T[3] == 'O' and T[6] == 'O' and T[9] == 'O'): 
        if T[3] == 'X':
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'X' GANHOU" + Style.RESET_ALL + Fore.RESET)
            return True
        else:
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'O' GANHOU" + Style.RESET_ALL + Fore.RESET)   
            return True            
    elif (T[1] == 'X' and T[5] == 'X' and T[9] == 'X') or (T[1] == 'O' and T[5] == 'O' and T[9] == 'O'): 
        if T[2] == 'X':
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'X' GANHOU" + Style.RESET_ALL + Fore.RESET)
            return True
        else:
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'O' GANHOU" + Style.RESET_ALL + Fore.RESET)   
            return True
    elif (T[3] == 'X' and T[5] == 'X' and T[7] == 'X') or (T[3] == 'O' and T[5] == 'O' and T[7] == 'O'): 
        if T[3] == 'X':
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'X' GANHOU" + Style.RESET_ALL + Fore.RESET)
            return True
        else:
            print(Fore.BLUE + Style.BRIGHT + "JOGADOR 'O' GANHOU" + Style.RESET_ALL + Fore.RESET)   
            return True
        


print(Fore.GREEN + Style.BRIGHT + "Jogo da velha by Ygor !!!" + Style.RESET_ALL + Fore.RESET)   
quadrante()
marcarXouO()
print(" Jogo finalizado ")

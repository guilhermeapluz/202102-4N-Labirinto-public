from Labirinto import Labirinto
from Posicao import Posicao
import time

def constroiMatriz(xMatriz):
    matriz = []
    for x in range(xMatriz):
        list.append(matriz,[None,None])

    matriz[0][0] = "Zero-Zero"
    matriz[0][1] = "Zero-Um"
    matriz[1][0] = "Um-Zero"
    matriz[1][1] = "Um-Um"
    return matriz

def main():
    
    vInput = 0
    while vInput < 2:
        print("Digite o valor da matriz: ")
        vInput = int(input())
        if(vInput < 2):
            print("O valor deve ser maior que 2.\n")

    lab = Labirinto(vInput)

    tab = lab.getTabuleiro()
    pos = Posicao(lab.getEntradaSaida())
    tabCpy = tab.copy()

    #print(pos.moveCursor(tabCpy,pos.getEntrada()))
    pos.moveCursor(tabCpy,pos.getEntrada())


    #print("\nposNodo.getCaminho()")
    #print(pos.getCaminho())
    

    # Imprime a matriz multidimensional
    print("\n----- Imprime a matriz em formato de tabela -----\n")
    impMatriz = "   "
    for k in range(int(vInput)):
        impMatriz = impMatriz+"| "+str(k)+" "
        if k == int(vInput)-1:
            impMatriz = impMatriz + "|\n"

    
    for l in tab:
        ind = tab.index(l)
        impMatriz = impMatriz+" "+str(ind)+" |"
        
        for c in l:
            if c == None: impMatriz = impMatriz+"   |"
            else: impMatriz = impMatriz+" "+str(c)+" |"
        
        impMatriz = impMatriz+"\n"
    
    print(impMatriz)
    

main()
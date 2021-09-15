from Nodo import Nodo
import random

class Posicao:

    def __init__(self,pPos):
        
        self.entrada = pPos[0]
        self.saida   = pPos[1]
        self.caminho = []

    def getEntrada(self):
        return self.entrada

    def getSaida(self):
        return self.saida
    
    def getCaminho(self):
        return self.caminho

    def _setCaminho(self,pPar):
        list.append(self.caminho,pPar)
    
    def moveCursor(self,tabuleiro,pPosicao):
        #print("\n*** Entrou no método moveCursor() ***")
        posDisponiveis = self._posicoesPossiveis(tabuleiro,pPosicao)
        print("---")
        posNodo = Nodo()
        pSaida = []

        posNodo.setPosicao(self.entrada)
        posNodo.setNodoAnterior(None)
        posNodo.setProximoNodo(pPosicao)

        for p in posDisponiveis:

            posNodo.setPosicao(p)
            posNodo.setNodoAnterior(self.entrada)
            posNodo.setProximoNodo(pPosicao)

            if p == self.saida:
                #print("Move o cursor de ("+str(pPosicao[0])+","+str(pPosicao[1])+") para ("+str(p[0])+","+str(p[1])+")")
                print("\nParabens! Encontrou a Saida.")
                print("Posicao Saida: "+str(p))
                

                #tabuleiro[pPosicao[0]][pPosicao[1]] = "+"
                posNodo.setPosicao(p)
                posNodo.setNodoAnterior(pPosicao)
                posNodo.setProximoNodo(None)

                #return pPosicao

            elif tabuleiro[p[0]][p[1]] is None:
                
                #print("Move o cursor de ("+str(pPosicao[0])+","+str(pPosicao[1])+") para ("+str(p[0])+","+str(p[1])+")")
                tabuleiro[p[0]][p[1]] = "*"
                
                
                #posNodo.setPosicao(p)
                #posNodo.setNodoAnterior(pPosicao)
                
                proximoNodo = self.moveCursor(tabuleiro,p)
        
                posNodo.setProximoNodo(proximoNodo)

                """if proximoNodo is not None:
                    if tabuleiro[proximoNodo[0]][proximoNodo[1]] == "+" or proximoNodo == self.saida:
                        #print("P saida = "+str(p))
                        
                        tabuleiro[p[0]][p[1]] = "+"
                        posNodo.setSaida(p)
                        list.append(pSaida,p)
                        posNodo.setSaida(pSaida)"""

        print(posNodo.getTodasPosicoes())
        return posNodo.getPosicaoAtual()


    def _posicoesPossiveis(self,tabuleiro,pPosicao):
        #print("\n*** Entrou em posicoesPossiveis() ***")
        posPossiveis = []
        posX = pPosicao[0]
        posY = pPosicao[1]
        qtTotPos = len(tabuleiro)

        if posX-1 >= 0:

            if tabuleiro[posX-1][posY] == None:
                list.append(posPossiveis,[posX-1,posY])
            elif tabuleiro[posX-1][posY] == "S":
                #print("1 - Parabens! Encontrou a Saida.")
                posPossiveis = [[posX-1,posY]]
                return posPossiveis

        if posX+1 <= qtTotPos-1:
            if tabuleiro[posX+1][posY] == None:
                list.append(posPossiveis,[posX+1,posY])
            elif tabuleiro[posX+1][posY] == "S":
                #print("2 - Parabens! Encontrou a Saida.")
                posPossiveis = [[posX+1,posY]]
                return posPossiveis

        if posY-1 >= 0:
            if tabuleiro[posX][posY-1] == None:
                list.append(posPossiveis,[posX,posY-1])
            elif tabuleiro[posX][posY-1] == "S":
                #print("3 - Parabens! Encontrou a Saida.")
                posPossiveis = [[posX,posY-1]]
                return posPossiveis

        if posY+1 <= qtTotPos-1:
            if tabuleiro[posX][posY+1] == None:
                list.append(posPossiveis,[posX,posY+1])
            elif tabuleiro[posX][posY+1] == "S":
                #print("4 - Parabens! Encontrou a Saida.")
                posPossiveis = [[posX,posY+1]]
                return posPossiveis
            

        return posPossiveis
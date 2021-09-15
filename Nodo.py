
class Nodo:

    def __init__(self,pNodo=None):

        #print("*** Entrou na classe Nodo ***")
        self.anterior = None
        self.posicao = pNodo
        self.proximo = None
        self.caminho = []

        #print("Anterior: "+str(self.anterior))
        #print("Posição: "+str(self.posicao))
        #print("Próximo: "+str(self.proximo))

    def getTodasPosicoes(self):
        return [self.anterior,self.posicao,self.proximo]

    def getProximoNodo(self):
        return self.proximo
    
    def getPosicaoAtual(self):
        return self.posicao

    def getCaminho(self):
        return self.caminho
    
    def setNodoAnterior(self,pNodo):
        self.anterior = pNodo

    def setPosicao(self,pNodo):
        self.posicao = pNodo
        #list.append(self.caminho,pNodo)
    
    def setProximoNodo(self,pNodo):
        self.proximo = pNodo

    def setSaida(self,pNodo):
        list.append(self.caminho,pNodo)
    
    

    


    
    
    
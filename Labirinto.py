import random

class Labirinto:

    def __init__(self,linMatriz,matObs = []):
        self.matriz = linMatriz
        self.obstaculos = matObs

        self.tab = self._Tabuleiro(linMatriz)       # Gera o tabuleiro
        self.obs = self._Obstaculos(linMatriz)      # Gera Obstaculos 
        self.pes = self._PosicaoInicial(linMatriz)  # Posição de Entrada e Saída

    def getTabuleiro(self):
        return self.tab

    def getObstaculo(self):
        return self.obs

    def getEntradaSaida(self):
        return self.pes

    def _PosicaoInicial(self,xMatriz):

        posES = []
        for k in range(xMatriz):
            
            if len(posES) < 2:
                xRand = random.randint(0,xMatriz-1)
                yRand = random.randint(0,xMatriz-1)

                while [xRand,yRand] in posES or [xRand,yRand] in self.obs:
                    xRand = random.randint(0,xMatriz-1)
                    yRand = random.randint(0,xMatriz-1)

                list.append(posES,[xRand,yRand])
                if posES.index([xRand,yRand]) == 0:
                    self.tab[xRand][yRand] = "E"
                else:
                    self.tab[xRand][yRand] = "S"
            else:
                break

        return posES

    def _Obstaculos(self,xMatriz):
        qtObs = int((xMatriz*xMatriz)*0.3)

        obstaculos = []
        
        for n in range(qtObs):

            xObs = random.randint(0,xMatriz-1)
            yObs = random.randint(0,xMatriz-1)

            while [xObs,yObs] in obstaculos:
                xObs = random.randint(0,xMatriz-1)
                yObs = random.randint(0,xMatriz-1)
                
            self.tab[xObs][yObs] = "/"
            list.append(obstaculos,[xObs,yObs])

        return obstaculos
    
    def _Tabuleiro(self,xMatriz):

        tab = []
        for x in range(xMatriz):
            list.append(tab,[None]*xMatriz)

        return tab
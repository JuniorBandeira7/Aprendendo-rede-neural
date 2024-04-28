import numpy as np
from alteraPesos import alteraPesos
from processarPesos import processarPesos
from processarPartidas import processarPartidas

class Perceptron:
    def __init__(self):
        pass

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def treinar(self):
        learningRate = 0.1

        #busca os pesos de um arquivo de texto
        pesos = processarPesos.processarPesos()

        #busca a lista com as informaçoes de um arquivo de texto
        lista_de_listas = processarPartidas.processarPartidas()
        numero = 0

        for linha in lista_de_listas:
            w1 = float(pesos[0])
            w2 = float(pesos[1])
            w3 = float(pesos[2])
            w4 = float(pesos[3])
            w5 = float(pesos[4])
            w6 = float(pesos[5])

            numero = numero + 1

            x1 = float(lista_de_listas[lista_de_listas.index(linha)][0])
            x2 = float(lista_de_listas[lista_de_listas.index(linha)][1])
            x3 = float(lista_de_listas[lista_de_listas.index(linha)][2])
            x4 = float(lista_de_listas[lista_de_listas.index(linha)][3])
            x5 = float(lista_de_listas[lista_de_listas.index(linha)][4])
            x6 = float(lista_de_listas[lista_de_listas.index(linha)][5])
            target = float(lista_de_listas[lista_de_listas.index(linha)][6])

            somaPonderada = w1*x1+w2*x2+w3*x3+w4*x4+w5*x5+w6*x6

            if somaPonderada != target:
                erro = target - somaPonderada               #normalizando(dando o mesmo peso) os valores do vetor
                pesos[0] = w1 + learningRate * erro * x1 / (np.linalg.norm(x1) + 1e-8)
                pesos[1] = w2 + learningRate * erro * x2 / (np.linalg.norm(x2) + 1e-8)
                pesos[2] = w3 + learningRate * erro * x3 / (np.linalg.norm(x3) + 1e-8)
                pesos[3] = w4 + learningRate * erro * x4 / (np.linalg.norm(x4) + 1e-8)
                pesos[4] = w5 + learningRate * erro * x5 / (np.linalg.norm(x5) + 1e-8)
                pesos[5] = w6 + learningRate * erro * x6 / (np.linalg.norm(x6) + 1e-8)
                alteraPesos.alteraPesos(pesos)
            
            print("previsao da partida ",numero," :",somaPonderada)
            print("target da partida ",numero," :",target)
            print("aproximação: ", self.sigmoid(somaPonderada))

        
    def testar(self, ama, dano, danoRecebido, ward, cs, ouro):
        pesos = processarPesos.processarPesos()

        w1 = float(pesos[0])
        w2 = float(pesos[1])
        w3 = float(pesos[2])
        w4 = float(pesos[3])
        w5 = float(pesos[4])
        w6 = float(pesos[5])
        
        x1 = ama
        x2 = dano
        x3 = danoRecebido
        x4 = ward
        x5 = cs
        x6 = ouro

        somaPonderada = w1*x1+w2*x2+w3*x3+w4*x4+w5*x5+w6*x6

        print("nota: ", somaPonderada)


if __name__ == "__main__":
    # Criar uma instância da classe principal
    minha_classe = Perceptron()

    minha_classe.treinar()

    #minha_classe.testar(0.33, 338.65, 902.21, 4, 5.5, 282.73)

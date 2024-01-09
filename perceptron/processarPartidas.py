class processarPartidas:    
    def processarPartidas():

        nome_arquivo = 'perceptron\dadosDeTreino.txt'

        lista_de_listas = []

        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                elementos = linha.split()

                sublist = [
                    float(elementos[0]) / 10,
                    float(elementos[1]) / 1000,
                    float(elementos[2]) / 1000,
                    float(elementos[3]) / 100,
                    float(elementos[4]) / 10,
                    float(elementos[5]) / 1000,
                    float(elementos[6])
                ]

                lista_de_listas.append(sublist)
        
        return lista_de_listas
    #print(processarPartidas())



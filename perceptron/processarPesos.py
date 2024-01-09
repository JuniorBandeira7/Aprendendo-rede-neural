class processarPesos:
    def processarPesos():
        nome_arquivo = 'perceptron\pesos'

        pesos = []

        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                pesos.append(linha)
        return pesos
        



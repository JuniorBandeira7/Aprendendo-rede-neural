class alteraPesos:
    def alteraPesos(pesos):

        nome_arquivo = 'perceptron\pesos'

        with open(nome_arquivo, 'w') as arquivo:
            for elemento in pesos:
                arquivo.write(str(elemento) + '\n')

def processaPalavra(transicoes, estadoInicial, estadosFinais, palavra):
    estadosAtuais = {estadoInicial}
    i=1 #TODO: Remover
    for simbolo in palavra:
        print("--------------------------------------------------------------- Verificando o", i,"simbolo:", simbolo) #TODO: Remover
        i=i+1 #TODO: Remover
        novosEstados = set()
        for estadoAtual in estadosAtuais:
            for transicao in transicoes:
                if transicao[0] == estadoAtual and transicao[1] == simbolo:
                    print("Alimentando", simbolo, "no estado atual", estadoAtual,"é possivel alcancar:", transicao[2:]) #TODO: Remover
                    novosEstados.update(transicao[2:])
        estadosAtuais = novosEstados
        print("Os estados alcancaveis são apos alimentar", simbolo, "sao:", estadosAtuais) #TODO: Remover
        if not estadosAtuais:
            return "Rejeito"
    print("--------------------------------------------------------") #TODO: Remover
    print("Depois de verificar toda palavra estados alcancaveis são:", estadosAtuais) #TODO: Remover
    print("--------------------------------------------------------") #TODO: Remover
    # Verifica se pelo menos um dos estados atuais é final
    if any(estado in estadosFinais for estado in estadosAtuais):
        return "Aceito"
    else:
        return "Rejeito"
    



# 0 c 0
# 0 d 0
# 0 g   1 2
# 1 c 0
# 1 d   1 2
# 1 g   1
# 2 c   1 2 
# 2 d 0 1
# 2 g 0 1 2

def main():
    # Lendo a entrada
    numEstados = int(input())
    numSimbolos, *simbolos = input().split()
    numSimbolos = int(numSimbolos)
    
    transicoes = []
    for _ in range(numEstados * numSimbolos):
        transicao = input().split()
        estadoOrigem = int(transicao[0])
        simbolo = transicao[1]
        estadosDestino = list(set(map(int, transicao[2:])))
        transicoes.append((estadoOrigem, simbolo, *estadosDestino))

    estadoInicial = int(input())
    num_estadosFinais, *estadosFinais = map(int, input().split())
    estadosFinais = set(estadosFinais)

    palavra = input().strip()

    # Processando a palavra
    result = processaPalavra(transicoes, estadoInicial, estadosFinais, palavra)
    print(result)

if __name__ == "__main__":
    # print(processaPalavra([(0, 'a', 0), (0, 'b', 0), (0, 'c', 0), (0, 'd', 0), (0, 'e', 0), (0, 'f', 0), (0, 'g', 1, 2), (0, 'h', 0), (0, 'i', 0), (0, 'j', 0), (0, 'k', 0), (0, 'l', 0), (0, 'm', 0), (0, 'n', 0), (0, 'o', 0), (1, 'a', 0), (1, 'b', 0), (1, 'c', 0), (1, 'd', 1, 2), (1, 'e', 0), (1, 'f', 0), (1, 'g', 1), (1, 'h', 0, 1, 2), (1, 'i', 0), (1, 'j', 0), (1, 'k', 0), (1, 'l', 1, 2), (1, 'm', 0), (1, 'n', 1), (1, 'o', 0), (2, 'a', 0), (2, 'b', 1, 2), (2, 'c', 1, 2), (2, 'd', 0, 1), (2, 'e', 0, 1), (2, 'f', 0), (2, 'g', 0, 1, 2), (2, 'h', 0), (2, 'i', 0), (2, 'j', 0), (2, 'k', 1, 2), (2, 'l', 0), (2, 'm', 1, 2), (2, 'n', 0), (2, 'o', 0)], 0, {0, 2}, "gccgddggggggggggggggggggggggggggggggggggggggggggggggggggggggc"))
    main()




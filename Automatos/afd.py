def processaPalavra(transicoes, estadoInicial, estadosFinais, palavra):
    estadoAtual = estadoInicial
    for simbolo in palavra:
        achouTransicao = False
        for transicao in transicoes:
            if transicao[0] == estadoAtual and transicao[1] == simbolo:
                estadoAtual = transicao[2]
                achouTransicao = True
                break
        if not achouTransicao:
            return "Rejeito"
    if estadoAtual in estadosFinais:
        return "Aceito"
    else:
        return "Rejeito"

def main():
    # Lendo a entrada
    numEstados = int(input())
    numSimbolos, *simbolos = input().split()
    numSimbolos = int(numSimbolos)
    
    transicoes = []
    for _ in range(numEstados * numSimbolos):
        transicao = input().split()
        transicoes.append((int(transicao[0]), transicao[1], int(transicao[2])))

    estadoInicial = int(input())
    num_estadosFinais, *estadosFinais = map(int, input().split())
    estadosFinais = set(estadosFinais)

    palavra = input().strip()

    # Processando a palavra
    result = processaPalavra(transicoes, estadoInicial, estadosFinais, palavra)
    print(result)

if __name__ == "__main__":
    main()

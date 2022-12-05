import string
import random

# Conjunto de caracteres possiveis a serem utilizados.
caracteres = string.ascii_letters + " "
# Tamanho da sequencia sugerida no algoritimo
tamSequencia = 28
#probabilidade de mutação
probMutacao = 5

# Quantidade de copias sugeridas no algoritmo
qtdElementos = 100

def gerarSequenciaInicial():
    frase = ""
    for _ in range(tamSequencia):
        frase += (random.choice(caracteres))
    return frase

def criarGeracao(seqAtual, qtdElementos, probMutacao):
    geracao = []
    for _ in range(qtdElementos):
        elementoGeracao = ""
        for x in range(tamSequencia):
            # Gerar outro caracter com base na probabilidade especificada.
            p = random.randint(1, 100)
            if(p <= probMutacao):
                novoChar = seqAtual[x]
                # Garantir que o novo caracter não é igual ao que já existia.
                while novoChar == seqAtual[x]:
                    novoChar = random.choice(caracteres) # talvez usar random com index
                # Nesse momento é garantido de que o novoChar é novo de fato.
                elementoGeracao += novoChar
            else:
               elementoGeracao += seqAtual[x]
        geracao.append(elementoGeracao)
    return geracao
# Baseado no calculo de distancia de Hamming
def calcularPontuacao(elemento, seqAlvo):
    distancia = 0
    for i in range(tamSequencia):
        if elemento[i] != seqAlvo[i]:
            distancia += 1
    return distancia

def selecionarMelhorElementoGeracao(geracao, seqAlvo):
    melhorElemento = ""
    menorPontuacao = tamSequencia
    for e in range(qtdElementos): # e de elemento da sequencia
        pontuacao = calcularPontuacao(geracao[e], seqAlvo)
        if pontuacao < menorPontuacao:
            menorPontuacao = pontuacao
            melhorElemento = geracao[e]
    return {
        "melhor" : melhorElemento,
        "pontuacao" : menorPontuacao
    }


def evoluir(probMutacao, qtdElementos ):
    seqAtual = gerarSequenciaInicial()
    seqAlvo = "METHINKS IT IS LIKE A WEASEL"
    gen = 1

    while seqAtual != seqAlvo:
        geracao = criarGeracao(seqAtual, qtdElementos, probMutacao)
        melhorElemento = selecionarMelhorElementoGeracao(geracao, seqAlvo)
        seqAtual = melhorElemento["melhor"]
        print(" Geracao:", gen, "Melhor elemento: ", seqAtual, " Distancia:", melhorElemento["pontuacao"])
        gen += 1


def main():
    evoluir(probMutacao,qtdElementos)
main()

""" _ algumas notas de observações
Quanto maior a probabilidade de mudança, mais gerações (mais demorado)
são necessarias para atingir o nivel de evolução alvo.

Quanto maior a quantidade de elementos de uma geração,
observa-se uma velocidade maior (menos geração) para atingir
o nivel da evolução alvo. Contudo, a maior quantidade de elementos
na geração, aumenta exponencialmente o custo computacional para
a evolução e, consequentemente, atingir o objetivo.( No caso deste aqui
presente)
"""

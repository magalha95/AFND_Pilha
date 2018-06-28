#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Codifing by: Magalhães da Silva, Ana Flávia Lemos e Lucas Estevão
#Email: italo.ufsj@gmail.com

import sys

#Função que valida a Quadrupla
def valida_maquina(maquina):
    return len(maquina) == 4

#Função recebe a quadrupla representada pela maquina e uma palavra para ser processada
def processa_palavra(maquina, palavra):
    pilha = []
    #Caso a quantidade de elementos da tupla for menor que 4 ou a palavra não consiga ser validada
    if not valida_maquina(maquina):
        return False

    # Processamento do automato.
    estado_atual = maquina['estado_inicial']
    for char in palavra:
        if char not in alfabeto:
            return False
        #verifica se há algo para empilhar
        if (maquina['funcao_transicao'][estado_atual][char][2] != '&'):
            pilha.append(maquina['funcao_transicao'][estado_atual][char][2])
            estado_atual = maquina['funcao_transicao'][estado_atual][char][0]
        #verifica se há algo para desempilhar
        if (maquina['funcao_transicao'][estado_atual][char][1] != '&'):
            if (pilha[-1] == maquina['funcao_transicao'][estado_atual][char][1]):
                pilha.pop()
                estado_atual = maquina['funcao_transicao'][estado_atual][char][0]
    if (len(pilha) == 0):
        estado_atual = maquina['funcao_transicao'][estado_atual]['?'][0]
    return (estado_atual in maquina['estados_finais'])

if __name__ == '__main__':

    #Define o alfabeto
    alfabeto = ['a', 'b']
    #Define a função de transição
    '''
        Ex: (q1,0)=q1
            (q1,1)=q1
            (q1,1)=q2
            (q2,0)=q1
            (q2,1)=q2
    '''
    funcao_transicao = {'q0' : {'a' : ['q0', '&', 'B'],
                                'b' : ['q1', 'B', '&'],
                                '?' : ['qf', '?', '?'],
                                },
                        'q1' : {'b' : ['q1', 'B', '&'],
                                '?' : ['qf', '?', '?'],
                                },
                        'qf' : {}
                        }

    #Define o estado incial
    estado_inicial = 'q0'
    #Define o conjunto de estados finais
    estados_finais = ['qf']

    #Define uma quadrupla. É uma quadrupla pois a função transição já está mapeada
    maquina = {'alfabeto':alfabeto,
               'funcao_transicao':funcao_transicao,
               'estado_inicial':estado_inicial,
               'estados_finais':estados_finais}

    #Abertura do arquivo de Leitura contendo todas as palavras para serem processadas
    arquivoEntrada= sys.argv[1]
    arquivo = open(arquivoEntrada,'r')
    palavras = arquivo.read()
    #Quebra a lista contendo todas as palavras no "\n"
    palavras = palavras.split('\n')
    #Abre arquivo saida para salvar as respostas computadas pelo automato
    arquivoSaida = open('resultadoPalavrasAFNP.txt','w')
    respostaFinal=[]
    #Realiza o processamento de cada palavra.
    print "Processando as Palavras do Arquivo..."
    for palavra in palavras:
        resultado = processa_palavra(maquina, palavra)
        palavraResultado= palavra + " " + str(resultado) + "\n"
        respostaFinal.append(palavraResultado)

    print "Salvando resultados"
    #Salva as palavras no arquivo
    arquivoSaida.writelines(respostaFinal)

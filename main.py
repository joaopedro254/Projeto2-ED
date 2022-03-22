from Advogado import Advogado
from Processo import Processo
from Pilha import *
from Fila import *
from Lista import *

if __name__ == "__main__":
                              
    def cadastra_processo():
        cod = int(input("Digite o código do processo a ser cadastrado: "))
        status = input("Digite o satus do processo a ser cadastrado: ")
        descricao = input("Digite uma descrição para o processo a ser cadastrado: ")
        custo = int(input("Digite o custo do processo a ser cadastrado: "))
        processo = Processo(status, custo, descricao, cod)
        return processo

    #Criação de objetos de PilhaProcessos

    processoP1 = Processo('Deferido', 1550, 'blablabla', 6544)
    processoP2 = Processo('indeferido', 3000, 'blablabla', 5543)
    processoP3 = Processo('Deferido', 1000, 'blablabla', 6655)
    processoP4 = Processo('indeferido', 2500, 'blablabla', 3234)

    #Criação de objetos de FilaProcessos

    processof1 = Processo('Indeferido', 1550, 'blablabla', 2898)
    processof2 = Processo('Indeferido', 2000, 'blablabla', 7784)
    processof3 = Processo('Deferido', 1000, 'blablabla', 9123)
    processof4 = Processo('Deferido', 2500, 'blablabla', 7689)

    #Criação de objetos de ListaProcessos

    processoL1 = Processo('Deferido', 2324, 'rajdfjakj', 9382)
    processoL2 = Processo('Indeferido', 9328, 'rajdfjakj', 8392)
    processoL3 = Processo('Deferido', 1239, 'rajdfjakj', 9482)
    processoL4 = Processo('Indeferido', 5093, 'rajdfjakj', 5234)

    advogado = Advogado('123123')
    #Inserção de objetos na Lista
    advogado.adicionar_processo_l(processoL1)
    advogado.adicionar_processo_l(processoL2)
    advogado.adicionar_processo_l(processoL3)
    advogado.adicionar_processo_l(processoL4)

    #Inserção de objetos na Fila
    advogado.adicionar_processo_f(processof1)
    advogado.adicionar_processo_f(processof2)
    advogado.adicionar_processo_f(processof3)
    advogado.adicionar_processo_f(processof4)

    #Inserção de objetos na Pilha
    advogado.adicionar_processo_p(processoP1)
    advogado.adicionar_processo_p(processoP2)
    advogado.adicionar_processo_p(processoP3)
    advogado.adicionar_processo_p(processoP4)

    print(advogado)
    while True:
        print('''
----------------------------MENU----------------------------
1 - Exibir processos.
2 - Verificar o processo de maior custo ou menor custo dentro da lista de processos.
3 - Aumentar o custo de um processo dentro da lista de processos.
4 - Adicionar processo a pilha de processos.
5 - Remover processo da pilha de processos.
6 - Adicionar processo a fila de processos.
7 - Remover processo da fila de processos.
8 - Adicionar processo a lista de processos.
9 - Remover processo da lista de processos.
10 - Ordenar processos na lista de processos.
11 - Verificar tamanho das pilhas, filas e listas de processos.
12 - Imprimir processos na lista de processos por Código e Status.
13 - Buscar um processo na lista de processos através do Código.
------------------------------------------------------------''')
        opcao = int(input('Digite um número equivalente ao índice no menu para realizar consulta(Ou um valor não existente para finalizar): '))
        if opcao == 1:
            test = int(input("Exibir processos de lista, pilha ou fila[1-2-3]: "))
            if test == 1:
                try:
                    print(advogado.processosL)
                except ListaException as le:
                    print(le)
            elif test == 2:
                try:
                    print(advogado.processosP)
                except PilhaException as pe:
                    print(pe)
            elif test == 3:
                try:
                    print(advogado.processosF)
                except FilaException as fe:
                    print(fe)

        elif opcao == 2:
            test = int(input('Buscar processo de maior ou menor custo[1-2]: '))
            if test == 1:
                print(advogado.maior_custo())
            else:
                print(advogado.menor_custo())

        elif opcao == 3:
            cod = int(input('Escolha um processo através do Código para incrementar seu custo: '))
            custo = int(input('Informe um valor a ser incrementado ao custo: '))
            print(advogado.incrementa_custo_processo(cod, custo))

        elif opcao == 4:
            processo = cadastra_processo()
            advogado.adicionar_processo_p(processo)
            print("Processo cadastrado!")

        elif opcao == 5:
            print(advogado.remover_processo_p())

        elif opcao == 6:
            processo = cadastra_processo()
            advogado.adicionar_processo_f(processo)
            print("Processo cadastrado!")

        elif opcao == 7:
            print(advogado.remover_processo_f())
        
        elif opcao == 8:
            processo = cadastra_processo()
            test = input("Deseja informar a posição a ser adicionada?(S/N) ").upper()
            if test == 'S':
                pos = int(input("Informe a posição da lista que deseja cadastrar o processo: "))
                print(advogado.adicionar_processo_l(processo, pos))
                
            elif test == 'N':
                print(advogado.adicionar_processo_l(processo))
                
        elif opcao == 9:
            test = input("Deseja informar a posição a ser removida?(S/N) ").upper()
            if test == 'S':
                pos = int(input("Posição: "))
                print(advogado.remover_processo_l(pos))
            elif test == 'N':
                print(advogado.remover_processo_l())
                
        elif opcao == 10:
            print(advogado.ordena_processos())

        elif opcao == 11:
            print(f"Tamanho da Pilha: {advogado.mostrar_tam_processosP()}")
            print(f"Tamanho da Fila: {advogado.mostrar_tam_processosF()}")
            print(f"Tamanho da Lista: {advogado.mostrar_tam_processosL()}")

        elif opcao == 12:
            print(advogado.imprimir_processos())

        elif opcao == 13:
            cod = int(input("Informe o Código do Processo a ser buscado: "))
            print(advogado.busca_processo(cod))

        else:
            print("Programa finalizado!")
            break

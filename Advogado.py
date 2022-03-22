from Pilha import *
from Fila import *
from Lista import *

class Advogado:
    def __init__(self, cod_oab):
        self.__cod_oab = cod_oab
        self.__processosP = PilhaProcessos()
        self.__processosF = FilaProcessos()
        self.__processosL = ListaProcessos()

    @property
    def cod_oab(self):
        return self.__cod_oab
    @cod_oab.setter
    def cod_oab(self, newOAB):
        self.__cod_oab = newOAB
    @property
    def processosL(self):
        if self.__processosL.vazia():
            raise ListaException('A Lista se encontra vazia')
        return self.__processosL
    @processosL.setter
    def processosL(self, newProcessosL):
        self.__processosL = newProcessosL
    @property
    def processosP(self):
        if self.__processosP.vazia():
            raise PilhaException('A Pilha se encontra vazia')
        return self.__processosP
    @processosP.setter
    def processosP(self, newProcessosP):
        self.__processosP = newProcessosP
    @property
    def processosF(self):
        if self.__processosF.vazia():
            raise FilaException('A Fila se encontra vazia')
        return self.__processosF
    @processosF.setter
    def processosF(self, newProcessosF):
        self.__processosF = newProcessosF
    
    #MÉTODOS DE PILHA

    def adicionar_processo_p(self, novo_processo_p):
        #falta criar um objeto
        self.__processosP.adicionar(novo_processo_p)

    def remover_processo_p(self):
        try:
            self.__processosP.remover()
            return "Primeiro processo da pilha removido!"
        except PilhaException as pe:
            return pe
    
    def mostrar_tam_processosP(self):
        try:
            p = self.__processosP
            return p.tamanho
        except PilhaException as pe:
            return pe

    #MÉTODOS DE FILA

    def adicionar_processo_f(self, novo_processo_f):
        #falta criar um objeto
        self.__processosF.adicionar(novo_processo_f)

    def remover_processo_f(self):
        try:
            self.__processosF.remover()
            return "Processo a frente da fila removido!"
        except FilaException as fe:
            return fe
    
    def mostrar_tam_processosF(self):
        try:
            p = self.__processosF
            return p.tamanho
        except FilaException as fe:
            return fe

    #MÉTODOS DE LISTA

    def adicionar_processo_l(self, novo_processo_l, pos = 0):
        #falta criar objeto
        try:
            self.__processosL.adicionar(novo_processo_l, pos)
            return "Processo adicionado!"
        except ListaException as le:
            return le
    def remover_processo_l(self, pos = 0):
        try:
            self.__processosL.remover(pos)
            return "Processo removido!"
        except ListaException as le:
            return le

    def imprimir_processos(self):
        output = ''
        p = self.__processosL
        try:
            for i in range(p.tamanho):
                obj = p.buscar(i)
                output += f"{obj.cod} - {obj.status}\n"
            return output
        except ListaException as le:
            return le

    def busca_processo(self, cod):
        p = self.__processosL

        try:
            for i in range(p.tamanho):
                obj = p.buscar(i, cod)
                if obj.cod == cod:
                    return obj
        except ListaException as le:
            return le

    def ordena_processos(self):
        try:
            self.__processosL.ordenar()
            return 'Lista ordenada!'
        except ListaException as le:
            return le

    def mostrar_tam_processosL(self):
        try:
            p = self.__processosL
            return p.tamanho
        except ListaException as le:
            return le

    def maior_custo(self):
        p = self.__processosL
        custoInicial = 0

        try:
            for i in range(p.tamanho):
                    obj = p.buscar(i)
                    if obj.custo >= custoInicial:
                        custoInicial = obj.custo
            
            
            for i in range(p.tamanho):
                    obj = p.buscar(i)
                    if obj.custo == custoInicial:
                        return f"Código: {obj.cod}, Status: {obj.status}, Custo: {obj.custo}"
        except ListaException as le:
            return le                
           
    def menor_custo(self):
        p = self.__processosL
        valorInicial = 0

        try:
            for i in range(p.tamanho):
                obj = p.buscar(i)
                if obj.custo >= valorInicial:
                    valorInicial = obj.custo
            
            for i in range(p.tamanho):
                obj = p.buscar(i)
                if obj.custo <= valorInicial:
                    valorInicial = obj.custo
            
            for i in range(p.tamanho):
                obj = p.buscar(i)
                if obj.custo == valorInicial:
                    return f"Código: {obj.cod}, Status: {obj.status}, Custo: {obj.custo}"
        except ListaException as le:
            return le

    def incrementa_custo_processo(self, cod, valor):
        p = self.__processosL

        try:
            for i in range(p.tamanho):
                obj = p.buscar(i, cod)
                if obj.cod == cod:
                    obj.incrementa_custo(valor)
                    return p.mostrar_elemento(i)
        except ListaException as le:
            return le

    def __str__(self):
        return f'Código OAB: {self.__cod_oab}\nPilha de Processos: \n{self.__processosP}\nFila de Processos: \n{self.__processosF}\nLista de Processos: \n{self.__processosL}'




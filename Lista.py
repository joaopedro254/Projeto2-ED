from Processo import Processo

class ListaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class ListaProcessos:
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def vazia(self):
        return self.__tamanho == 0

    @property
    def inicio(self):
        if self.vazia():
            raise ListaException('A Lista se encontra vazia')
        return self.__inicio
    @inicio.setter
    def inicio(self, novoInicio):
        self.__inicio = novoInicio
    @property
    def tamanho(self):
        if self.vazia():
            raise ListaException('A Lista se encontra vazia')
        return self.__tamanho
    @tamanho.setter
    def tamanho(self, novoTamanho):
        self.__tamanho = novoTamanho

    def adicionar(self, novoProcesso, pos = 0):
        processoL = novoProcesso

        if pos > (self.__tamanho) or pos < (self.__tamanho - self.__tamanho):
            raise ListaException('A lista não contém o índice indicado.')

        if pos == 0:    #Inserção no início
            processoL.prox = self.__inicio
            self.__inicio = processoL
            self.__tamanho += 1
        
        else:   #Inserção no Meio e Fim
            p = self.__inicio
            q = None
            cont = 0

            while (cont < pos) and (p != None):
                q = p
                p = p.prox
                cont += 1

            q.prox = processoL
            processoL.prox = p
            self.__tamanho += 1

    def remover(self, pos = 0):
        if self.vazia():
            raise ListaException('A Lista se encontra vazia')
        elif pos >= (self.__tamanho) or pos < (self.__tamanho - self.__tamanho):
            raise ListaException('A lista não contém o índice indicado.')
        elif pos == 0:
            self.__inicio = self.__inicio.prox
            self.__tamanho -= 1
        else:
            p = self.__inicio
            q = None
            cont = 0

            while (cont < pos) and (p != None):
                q = p
                p = p.prox
                cont += 1
        
            q.prox = p.prox
            self.__tamanho -= 1

    def mostrar_elemento(self, pos):
        if pos >= (self.__tamanho) or pos < (self.__tamanho - self.__tamanho):
            raise ListaException('A lista não contém o índice indicado.')

        p = self.__inicio
        cont = 0

        while (cont < pos) and (p != None):
            p = p.prox
            cont += 1

        return p.__str__()

    def ordenar(self):
        if self.vazia():
            raise ListaException('A Lista se encontra vazia')
        else:  
            ordenado = False
            cont = 0

            while ordenado == False:
                q = self.__inicio
                p = self.__inicio.prox
                ordenado = True
                while p != None:
                    if q.cod > p.cod:
                        q.status, p.status = p.status, q.status
                        q.custo, p.custo = p.custo, q.custo
                        q.descricao, p.descricao = p.descricao, q.descricao
                        q.cod, p.cod = p.cod, q.cod
                        ordenado = False
                        cont += 1
                    q = p
                    p = p.prox


    def buscar(self, pos, cod = 0):
        if self.vazia():
            raise ListaException('A Lista se encontra vazia')
        elif pos >= (self.__tamanho) or pos < (self.__tamanho - self.__tamanho):
            raise ListaException('A lista não contém o índice indicado.')
        else:
            p = self.__inicio
            cont = 0
            while (cont < pos) and (p != None):
                p = p.prox
                cont += 1
            return p

    def __str__(self):
        output = ''
        p = self.__inicio

        while p != None:
            output += f"Código: {p.cod}, Status: {p.status}, Descrição: {p.descricao}, Custo: {p.custo}\n"
            p = p.prox
        return output

    



   

    


            
                



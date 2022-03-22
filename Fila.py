from Processo import Processo

class FilaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class FilaProcessos:
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def vazia(self):
        return self.__tamanho == 0

    @property
    def inicio(self):
        if self.vazia():
            raise FilaException('A Fila se encontra vazia')

        return self.__inicio
    @inicio.setter
    def inicio(self, newInicio):
        self.__inicio = newInicio

    @property
    def tamanho(self):
        if self.vazia():
            raise FilaException('A Fila se encontra vazia')
        return self.__tamanho
    @tamanho.setter
    def tamanho(self, newTamanho):
        self.__tamanho = newTamanho

    def adicionar(self, novo_processo):
        processoF = novo_processo

        aux = self.__inicio

        if aux == None:
            self.__inicio = processoF

        else:
            while aux.prox != None:
                aux = aux.prox

            aux.prox = processoF

        self.__tamanho += 1

    def remover(self):
        if self.vazia():
            raise FilaException('A Fila se encontra vazia')

        self.__inicio = self.inicio.prox
        self.__tamanho -= 1
    
    def mostrar_elemento(self):
        if self.vazia():
            raise FilaException('A Fila se encontra vazia')

        return self.__inicio.__str__()

    def __str__(self):
        output = ''
        p = self.__inicio

        while p != None:
            output += f"Código: {p.cod}, Status: {p.status}, Descrição: {p.descricao}, Custo: {p.custo}\n"
            p = p.prox
        return output




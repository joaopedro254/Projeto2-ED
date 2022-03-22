from Processo import Processo


class PilhaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class PilhaProcessos:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def vazia(self):
        return self.__tamanho == 0

    @property
    def topo(self):
        if self.vazia():
            raise PilhaException('A Pilha se encontra vazia')

        return self.__topo
    @topo.setter
    def topo(self, newTopo):
        self.__topo = newTopo
    @property
    def tamanho(self):
        if self.vazia():
            raise PilhaException('A pilha se encontra vazia')
        return self.__tamanho
    @tamanho.setter
    def tamanho(self, newTamanho):
        self.__tamanho = newTamanho

    def adicionar(self, novo_Processo):
        processoP = novo_Processo
        processoP.prox = self.__topo
        self.__topo = processoP

        self.__tamanho += 1

    def remover(self):
        if self.vazia():
            raise PilhaException('A Pilha se encontra vazia')

        self.__topo = self.__topo.prox
        self.__tamanho -= 1

    def mostrar_elemento(self):
        if self.vazia():
            raise PilhaException('A Pilha se encontra vazia')

        return self.__topo.__str__()

    def __str__(self):
        output = ''
        p = self.__topo

        while p != None:
            output += f"Código: {p.cod}, Status: {p.status}, Descrição: {p.descricao}, Custo: {p.custo}\n"
            p = p.prox
        return output



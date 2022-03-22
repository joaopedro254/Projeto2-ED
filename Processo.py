class Processo:
    def __init__(self, status, custo, descricao, cod):
        self.__status = status
        self.__custo = custo
        self.__descricao = descricao
        self.__cod = cod
        self.__prox = None

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, novo_status):
        self.__status = novo_status
    @property
    def custo(self):
        return self.__custo
    @custo.setter
    def custo(self, novo_custo):
        self.__custo = novo_custo
    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, nova_descricao):
        self.__descricao = nova_descricao
    @property
    def cod(self):
        return self.__cod
    @cod.setter
    def cod(self, newCod):
        self.__cod = newCod
    @property
    def prox(self):
        return self.__prox
    @prox.setter
    def prox(self, novo_prox):
        self.__prox = novo_prox

    def incrementa_custo(self, valor):
        self.__custo += valor

    def __str__(self):
        return f'Código: {self.__cod}, Status: {self.__status}, Descrição: {self.__descricao}, Custo: {self.__custo}'
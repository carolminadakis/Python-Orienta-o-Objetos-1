class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo do {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Valor indisponível!")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property #O @property faz com que vc não precise usar os (), ele entende que é uma propriedade que deve ser retornada
    def limite(self):
        return  self.__limite

    @limite.setter  #O @nomedoatributo.setter vai alterar o valor pré definido, sem precisar dos (), apenas atribuindo normalmente um valor
    def limite(self, limite):  #Atribuindo novo valor, o set não vai retornar nada, apenas modificar o valor inicial
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
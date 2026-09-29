from ctypes import c_int16


class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta de id={self.id} criada com sucesso.Saldo atual de {self.saldo:,.2f}")
    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."
    def depositar(self,valor):
        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta de id={self.id}")

    def sacar(self,valor):
        if valor > self.saldo:
            print(f"SAQUE NEGADO de R${valor:,.2f}na conta de id={self.id} por :SALDO INSUFICIENTE ")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta de {self.id}")
c1=ContaBancaria(112,"Gustavo",3000)
c1.depositar(500)
c1.sacar(2000000)
print(c1)

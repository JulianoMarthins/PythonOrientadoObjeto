from datetime import datetime
import pytz
import locale


class ContaCorrete:

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTC-8')

    def __init__(self, nome: str, cpf: str, agencia: str, numeroConta: str):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = 0
        self.agencia = agencia
        self.numeroConta = numeroConta
        self.transacoes = []
        self.cartao = []

    @staticmethod
    def _dataHora():  # Função retorna a data de brasilia formatada
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)

        return horario_br.strftime('%d/%m/%y %H:%M:%S')

    def consultarSaldo(self) -> str:
        valorFormatado = locale.currency(self.saldo, grouping=True)
        msg = f'Saldo: {valorFormatado}'

        return msg

    def dadosCliente(self):
        msg = f'''
        =-=-=-=- Dados do Cliente =-=-=-=-
            Nome: {self.nome}
            CPF: {self.cpf}
            Agencia: {self.agencia} Número: {self.numeroConta}
            {self.consultarSaldo()}
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''

        return msg

    def depositar(self, valor: float) -> None:
        self.saldo += valor
        valorFormatado = locale.currency(valor, grouping=True)
        saldoFormatado = locale.currency(self.saldo, grouping=True)
        self.transacoes.append(
            (self._dataHora(), valorFormatado, saldoFormatado, 'Deposito'))

    def sacar(self, valor: float) -> None:
        if self.saldo - valor < self._limiteConta():
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            valorFormatado = locale.currency(valor, grouping=True)
            saldoFormatado = locale.currency(self.saldo, grouping=True)
            self.transacoes.append(
                (self._dataHora(), valorFormatado, saldoFormatado, 'Saque'))

    def transferencia(self, valor, contaDestino) -> None:
        self.sacar(valor)
        contaDestino.depositar(valor)

    def _limiteConta(self):
        self.limite = -1000
        return self.limite

    def consultarLimite(self):
        limiteFormatado = locale.currency(self.limite, grouping=True)
        print(f'Limite: {limiteFormatado}')

    def extrato(self):
        msg = f'''
        =-=-=- Histório de Transações =-=-=-

            Cliente: {self.nome}

      Data e Hora         Valor           Saldo       Serviço'''
        print(msg)
        for transacao in self.transacoes:
            print(transacao)

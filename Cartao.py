from datetime import datetime
from random import randint
import locale
import pytz


class Cartao:

    locale.setlocale(locale.LC_ALL, "pt_BR.UTC-8")

    def __init__(self, contaCorrente) -> None:
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = contaCorrente.nome
        self.validade = f'{Cartao._data().month}/{Cartao._data().year + 5}'
        self.codSeguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self.limite = 4000
        self.ContaCorrente = contaCorrente
        contaCorrente.cartao.append(self)

    @staticmethod
    def _data():  # Função retorna a data de brasilia formatada
        fuso_br = pytz.timezone('Brazil/East')
        return datetime.now(fuso_br)

    def dadosCartao(self):
        limiteFormatado = locale.currency(self.limite, grouping=True)
        msg = f"""
        =-=-=-=-=- Dados do Cartão =-=-=-=-=-
            Titular: {self.titular}
            Número Cartão: {self.numero}
            Validade: {self.validade}
            Código de Segurança: {self.codSeguranca}
            Limite: {limiteFormatado}
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="""
        return msg

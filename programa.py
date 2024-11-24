from ContaCorrente import *
from Cartao import *
import os

# Função para limpar o terminal cada vez que eu executar o programa


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


print()  # Apenas para dar um espaço das escritas obrigatórias do terminal
clearTerminal()

# Criação de objeto, conta corrente para Juliano
juliano = ContaCorrete('Juliano Martins', '35.456.756-34', '0460', '1543-5')

juliano.depositar(9_000)  # Depoisto
juliano.sacar(1_000)  # Saque

print(juliano.dadosCliente())  # Dados da conta do juliano

# Criação de nova conta para Thiele
thiele = ContaCorrete('Thiele Gringer', '35.675.345-43', '0460', '1524-7')

thiele.depositar(4_000)  # Deposito
thiele.sacar(1_300)  # Saque

print(thiele.dadosCliente())  # Dados da conta da Thiele

# Separação para melhor visualização no terminal
print('\n\n                   Transferência\n')
# Transferência de R$ 1.800,00 reais da conta do Juliano para  a conta da Thiele
juliano.transferencia(1_800, thiele)

# Analisando os dados do Juliano para testar a função de transferência ao enviar o valor
print(juliano.dadosCliente())
print(juliano.extrato())

# Analisando os dados da Thiele para testar a função de transferência ao receber o valor
print(thiele.dadosCliente())
print(thiele.extrato())

# Criação de cartão de crédito, testando nova classe
cartaoJuliano = Cartao(juliano)

# Verificaç]ao
print(f'Titular do cartão de crédito: {cartaoJuliano.titular}')
print(cartaoJuliano.ContaCorrente.numeroConta)


print(f'Validade Cartão de crédito: {juliano.cartao[0].validade}')
print(f'Número do cartão de crédito: {juliano.cartao[0].numero}')
print(f'Número de segurança: {juliano.cartao[0].codSeguranca}')

print('\n')
print(cartaoJuliano.dadosCartao())

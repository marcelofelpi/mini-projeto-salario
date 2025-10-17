print('Olá, querido funcionário! Seja bem- vindo!')
n1 = input('Por favor, informe o seu nome completo:')
print(
    f'Tudo preparado(a) {n1}?\n Vamos calcular o aumento do seu salário em 15%')

# RECEBE O VALOR COMO TEXTO (COM VÍRGULAS E PONTOS, NO PADRÃO BR)
valor_digitado = (input('Digite o valor do seu salário atualmente:'))

# USA O REPLACE PARA REMOVER O SEPARADOR DE MILHAR (PONTO)
valorlimpo = valor_digitado.replace('.', '')
valorfinal = valorlimpo.replace('.', '')
salario = float(valorfinal)
if salario < 2000:
    print('Nossa... talvez seja uma boa mudar de emprego!')

elif salario == 2000:
    print('Seu salário é de R$2000.00. Um valor OK, mas com aumento de 15 % vai melhorar!')

else:
    print('Uau! Belo salário hein!')

conta = salario*1.15
print(f'{n1} o seu salário com aumento de 15%, ficou no valor de R${conta:.2f}')

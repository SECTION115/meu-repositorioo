print('Digite seu nome: ')
nome = input()

print('Digite sua idade: ')
idade = input()

print('Digite sua altura: ')
altura = input()

idade_futura = int(idade) + 10

print('Obrigado por responder. As seguintes informações estão cadastradas em ' + nome)
print('NOME: ' + nome)
print('IDADE: ' + idade)
print('ALTURA: ' + altura)
print('Veja quantos anos você terá em uma década: ' + str(idade_futura))

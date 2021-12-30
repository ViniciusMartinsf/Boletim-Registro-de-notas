#MATÉRIA DE LISTAS COMPOSTAS
#Lista padrao
primaria = list()
#lista que servirá somente para copiar os dados e joga
secundaria = list()
cont = 0
print(f'\033[32m    BOLETIM COM LISTAS COMPOSTAS\033[m')
print('-=-'*12)
minimo = float(input('Primeiro, digite a nota minima para aprovação: '))
while True:
    nome = str(input('Digite o nome: '))
    secundaria.append(nome)
    nota1 = float(input('Nota 1: '))
    secundaria.append(nota1)
    nota2 = float(input('Nota 2: '))
    secundaria.append(nota2)
    cont += 1
    primaria.append(secundaria[:])
    secundaria.clear()
    continuar = str(input("Quer continuar ? [S/N]")).upper().strip()[0]
    if continuar == 'N':
        break
    while continuar not in "S":
        continuar = str(input("Não entendi, digite apenas S ou N: ")).upper().strip()[0]
        if continuar == 'SN':
            break
    if continuar == 'N':
        break
#print(primaria)
#soma = primaria[0][1] + primaria[0][2]
#media = soma / 2
#print(media)
print(f'{"No.":<4}   {"NOME":<15} {"MÉDIA":>10}  {"RESULTADO FINAL"}')
print('-'*44)
for c in range(0, cont):
    print(f'{c:<4}   {primaria[c][0]:<15}',end='')
    soma = primaria[c][1] + primaria[c][2]
    media = soma / 2
    print(f' {media:>8}', end='')
    if media >= minimo:
        print('    \033[34mAprovado\033[m')
    else:
        print('    \033[31mReprovado\033[m')

print('-'*44)
while True:
    escolhanota = int(input('Insira o numero do aluno caso queira visualizar as notas dele. (999 para interromper) '))
    if escolhanota == 999:
        break
    print(f'As notas de {primaria[escolhanota][0]} são {primaria[escolhanota][1]} e {primaria[escolhanota][2]}')
from time import sleep
print('\033[34mOBRIGADO POR REPRODUZIR MEU PROGRAMA!')
sleep(1)
print('\033[31mEncerrando...')
sleep(2)
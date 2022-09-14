"""Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

galera = []
dado = []
resp = 'S'
pesada = []
pessoaspesadas = []
pessoasleves = []
leve = []
maispesada = maisleve = cont = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while resp != 'N' and resp != 'S':
        resp = str(input('Opção invalida, escolha sim ou não [S/N]')).strip().upper()[0]
    galera.append(dado[:])
    dado.clear()
    cont += 1
    if resp == 'N':
        break
print(f'Ao todo tivemos {cont} pessoas cadastradas')
for p in galera:
    if p[1] >= 80:
        pessoaspesadas.append(p[0])
        pesada.append(p[1])
        maispesada += 1
    else:
        pessoasleves.append(p[0])
        leve.append(p[1])
        maisleve += 1
print('-='*30)
print(f'Ao todo tivemos {maispesada} pessoas mais pesadas')
print(f'Sendo elas {pessoaspesadas} com {pesada}Kg cada')
print(f'Ao todo tivemos {maisleve} pessoas mais leve')
print(f'Sendo elas {pessoasleves} com {leve}Kg cada')

tot18= tothom = totmu20 = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F]')).strip().upper()[0]
    if idade >=18:
        tot18 +=1
    if sexo == 'M':
        tothom +=1
    if sexo == 'F' and idade < 20:
        totmu20 +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-'*20)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo tempos {tothom} homens cadastrados')
print(f'Ao todo temos {totmu20} mulheres com menos de 20 anos')
print('-=-'*20)
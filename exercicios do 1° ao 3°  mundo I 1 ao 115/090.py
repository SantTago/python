#=========== como eu fiz =====================

tabela = dict()
tabela['nome'] = str(input("nome:"))
tabela['nota1'] = float(input("1° nota:"))
tabela['nota2'] = float(input("2° nota:"))
media = (tabela['nota1']+tabela['nota2']) / 2
print(f'Media e igual : {media}')
if media <= 6.0:
    print('Situação e Reprovado!')
else:
    print('Situaçao e Aprodado!')
print(f'A media e igual a {media}')


#=========== como o professor fezz =====================

aluno = dict()
aluno['nome'] = str(input('Nome:'))
aluno['media'] = float(input(f'Media de {aluno["nome"]} '))
if aluno['media'] > 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
print('='*20)
for k,v in aluno.items():
    print(f'-{k} é igual a {v}')
    

#========== Como eu fiz =======================================

with open("pessoas.txt",) as arquivo:
	texto = arquivo.read() # read(): usado para ler dados do arquivo aberto usando o método open()
	print("="*40)
	print(f'{"Pessoas Cadastradas":^40}')
	print("="*40)
	lista = list(open("pessoas.txt","rt"))
  
	for valor in lista:
		print(f'{valor}',end='',)
	if lista[1]:
		print(f'{lista[1]:>30}',end='')
		
	


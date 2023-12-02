import urllib
import urllib.request


site = str(input('Insira o site: '))

try:
    site1 = urllib.request.urlopen('https://www.'+site+'/') # urlopen para abrir URL # .request protocologos de html
    
except urllib.request.URLError: # urllib.request.URLError se o Try nao fuincionar ele chama o erro
    print('O Site não está acessível no momento')
else: # se o site for aberto ele retorna
    print('Consegui abrir o site com sucesso!')
    
    
#OpenerDirector() #gerencia uma coleção de objetos Handler que fazem todo o trabalho real. 
#========== Como eu fiz =======================================
try:
    import requests

    url = requests.get("http://www.pudim.com.br/").status_code == 200 # requerimento para o get com a url e pedi o status do code se era 200
    print("\033[32mConsegui acessar o site do Putdim com SUCESSO!.\033[m")
        
except:
    print("\033[31mO site do pudim nao esta disponivel no momento!.\033")
    
#========== Como o professor fez =======================================
    
import urllib 
import urllib.request # request para fazer as resiziçoes 

try:
    site = urllib.request.urlopen('http://pudim.com.br') # .urlopen para abrir a url
except urllib.error.URLError: # erro da except .error.URLError
    print("O site Pudim nao esta acessivel no momento")
else:
    print("O site Pudim acessivel")
    #print(site.read()) # .read() para trazer o codigo da pagina em html
    
	 
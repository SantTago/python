#============= COMO EU FIZ =================

# Exercício Python 48: Faça um programa que calcule a 
# soma entre todos os números que são múltiplos de três e 
# que se encontram no intervalo de 1 até 500.

from time import sleep
print('''\033[0;30;41m
──────▌░▄█████▄░░░░░▄████▄░▐            
─────▐░▌░▄▄▄▄▄░░░░░░▄▄▄▄▄░░▌        
─────▌░▌░░░██░░░▐░▌░░██░░░█      
─────▀▄▐░░░░░░░░▐░▌░░░░░░░▌   
───────█░░░░░░░░▌░▐░░░░░░▐         
───────█░░░░░░░▀▄▄▄▀░░░░░▌         
────────█░░░░▄░░░░░░▄░░░█         
────▄▄▄▄█░░░░░▀▀▀▀▀▀░░░█            
▄▄▀▀▒▒▒▌░▀▄░░░░░░░░░░░█              
▒▒▒▒▒▒▐░░░░▀▀▄░░░░░▄▄▀▀▄                
▒▒▒▒▒▒▌░░░░░░░▀▀▀▀▀░░▐▒▒▀▄       
▒▒▒▒▒▒▐░░░░░░░░░░░░░░▐▒▒▒▒▀▄          
▒▒▒▒▒▒▒▐░░░░░░░░░░░░▐▒▒▒▒▒▒▒▀▄      
\033[m''')
print('''---ESSE PROGRAMA SOMA TODOS OS NUMEROS IMPAR ENTRE 0 A 500---
      \033[36m----FIQUE ATE O FINAL PRA VER O RESULTADO----
      
      
      ''' )
sleep(3)
h2 = 0
for h in range(1,501, 2):
    sleep(1)
    h1 = ( h%2 ) == 1
    h2 += h
    print('\033[36mIMPAR | '
          '\033[31m{} | '
          '\033[36m{} | '
          '\033[31m{} |'.format(h1, h, h2))
print('\033[31mA SOMA ENTRE TODOS OS NUMEROS IMPAR DA ')
print('\033[36m================= \033[31m{} '
      '\033[36m=================='.format(h2))

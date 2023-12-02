
# =================== COMO EU FIZ ==============



problema = str(input('Digite uma soexpresao que usa parentes: '))
cont = 0
conte = 0

for simbo in problema: # SIMBO RECEBE OS VALORES DENTRO DO PROBLEMA
        
    if simbo == '(':
        cont += 1
        
    elif simbo == ')':
        conte += 1
        
if cont == conte:
    print("A soluçao esta correta!")
else:
    print("A soluçao esta incorreta!!")
    
#=================== COMO EU FIZ COM A SOLUÇAO DO PROFESSOR  ==============
 
expr = str(input('Digite uma expressap matematica: '))
cont = conte = 0
for simb in expr:
    if simb == '(':
        conte += 1
    elif simb == ')':
        cont += 1
       
if cont == conte: # len para ver quantos elementos tem na pilha 
    print('Sua expressao e valida!')
else:
    print('Sua expressao esta Incorreta!')

    

 #=================== COMO O PROFESSOR FEZ ==============

expr = str(input('Digite uma expressap matematica: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        pilha.append(')')
        if len(pilha) > 0:
            pilha.pop() # para eliminar o ultima casa 
        else:
            pilha.append(')')
            break
if len(pilha) == 0: # len para ver quantos elementos tem na pilha 
    print('Sua expressao e valida!')
else:
    print('Sua expressao esta Incorreta!')
    
print(pilha)
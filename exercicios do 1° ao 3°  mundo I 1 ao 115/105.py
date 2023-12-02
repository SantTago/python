
#================ COMO EU FIZ =====================

def notas(*num, sit=False): # sit e variavel 
    """
    _> Função para analizar notas e situaçao de varios alunos 
    
    Param *nun: Uma ou varias notas de alunos 
    Param sit: valor opcional indicando se deve ou nao adiconar a Situaçao 
    
    xxxxxxxxxx
    return: Dicionario com varias informaçoes sobre a situaçao da turma
    xxxxxxxxx
    """

    for valor in num:
        total =  len(num) # len recebe o total de notas 
    print(f'Total: {total}, ', end='')

    for valor in num:
        maior = max(num) # max puxa o maior valor de notas 
    print(f'maior: {maior}, ', end='')

    for valor in num:
        menor = min(num) # min puxa o menor valor de notas 
    print(f'Menor: {menor}, ', end='')

    for valor in num:
        media  = total / len(num)  # a media = ele pega o total de notas e divide elas pelo tatal
    print(f'Media: {media}, ', end='')

    if sit:
        if media < 6: # se media for menor que 6
            print('Situação : Ruim')

 
#programa principal
notas(5.5, 9.5, 10, 6.5, 10,sit=True) # CASO QUEIRA MOSTRAR A SITUAÇAO COLOCAR O sit=True
#notas(resp)


#============= COMO O PROFESOR FEZ =====================

def notas(*n, sit=False):
    """
    _> Função para analizar notas e situaçao de varios alunos 
    
    Param *n: Uma ou varias notas de alunos 
    Param sit: valor opcional indicando se deve ou nao adiconar a Situaçao 
    return: Dicionario com varias informaçoes sobre a situaçao da turma
    """
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n) / len(r) # sum para somar todos os numeros
    
    if r["media"] >= 7:
        r["Situção"] = "Boa"
    elif r["media"] >= 5:
        r["Situação"] = "Razoavel"
    else:
        r["Situaçao"] = "Ruim"
    return r

#programa principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)
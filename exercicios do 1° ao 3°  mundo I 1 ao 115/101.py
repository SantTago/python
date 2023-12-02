#================ COMO EU FIZ =====================

from datetime import date # date - Data Time - Hora
atual = date.today().year # date - data | today - Hoje | year - Ano

def voto(ano=0): # ano recebe o valor de atual que e o ano atual 
    print('-=' * 30)
    ano = int(input("Que ano voce nasceu? "))
    idade = atual - ano
    print(f'Com {idade} Anos: ', end='')
    if idade > 18:
        if idade < 69:
            return "Voto Obrigadorio!!!"
    elif idade <= 16:
        return "Não Vota!!!"
    if idade >= 70:
        return "Voto Opcional!!!"
    print('-=' * 30)
#programa principal

print(voto(atual))

#================ COMO O PROFESOR FEZ =====================

def voto(ano): # ano recebe o valor de anor recebe o valor de nasc
    from datetime import date # usar a importaçao dentro da funçao economiza memoria 
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA!!'
    elif 16 <= idade < 18: 
        return f'com {idade} anos: VOTO E OPCIONAL!!'
    else:
        return f'Com {idade } anos: VOTO OBRIGATORIO!!'

nasc = int(input("Em que ano voce nasceu? ")) 
print(voto(nasc))
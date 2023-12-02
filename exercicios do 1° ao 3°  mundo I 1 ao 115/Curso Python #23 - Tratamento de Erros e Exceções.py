
try: # tente fazer 
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
       
       
except (ValueError, TypeError): # se der proble com ValueError, TypeErro 
    print("Tivemos um problema com tipo de dado que vc digitou. !")

except ZeroDivisionError: # nao divisivel por zero
    print("nao e possivel dividir um numero por zero!")

except KeyboardInterrupt: # caso o campo esteja vazio 
    print("O usuario preferil nao informar nenhum dado!")
        

except Exception as erro: # except | se der problema / Exception
   print(f"Problema encontrado doi {erro.__class__}") # e so chamar o  com ponto no final do erro e a __class__ # ele mostra a tipo de erro  
   
except Exception as erro: # except | se der problema / Exception
   print(f"Problema encontrado foi {erro.__cause__}") # e so chamar o  com ponto no final do erro e a __cause__ # ele mostra a causa de erro  
    
except: # se der problema
    print("Infelismente tivemos um problema ;(") 

else: #else para caso funcione o Try
    print(f'O resultado é {r}')
    
finally: # finally e opcional ele ira acontecer idependente do resultado 
    print("Volte Sempre! Muito Obrigado!")
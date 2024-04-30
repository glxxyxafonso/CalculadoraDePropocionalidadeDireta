# Version 2.0
# Code available in English at https://github.com/glxxyxafonso/

# Dear programmer,
# When I made this code, only god and I knew how it worked.
# Now, only god knows how it works!!
# If you are trying to optimise this code (that you probably won't be able to)
# Please add how much time you spent on this in this counter:

# Hours_Spent_On_This_Code = 2

from time import sleep as wait

def smart_float(msg, tipo=float, exist_condition=""):
    value = None
    while value is None:
        value_str = input(msg)
        try:
            value = tipo(value_str)
        except:
            value = None
        if value_str == exist_condition:
            return None
    return value
            
def checamento_de_proporcionalidade():   
    x, y = 0, 0 # inicial values
    k, constant = 0, None
    done = False
    while not done:
        x = smart_float("Insira o X: ")
        y = smart_float("Insira o f(X): ")
     
        if None in [x, y]:
            done = True
        else:
            k = y / x
            print(f"x={x}, f({x})={y}, Constante de proporcionalidade: {k}")
        
            if constant is None:
                constant = k
                
            if constant != k:
                print("Constante de proporcionalidade diferente da anterior!")
                done = True

print("Boas-vindas à Calculadora de Proporcionalidade Direta!")
print("Código disponível no Github - https://github.com/glxxyxafonso")
print("V2 feita por https://github.com/jpedrodias - Obrigado :)")
wait(2)

done = False
while not done:
    option = ""
    while option not in  ["S", "N"]:
        option = input("Queres começar? (S/N) ").upper()
        
    if option == 'N':
        done = True
    else:
        checamento_de_proporcionalidade()

# Version 3.0
# Code available in English at https://github.com/glxxyxafonso/

# Dear programmer,
# When I made this code, only god and I knew how it worked.
# Now, only god knows how it works!!
# If you are trying to optimise this code (that you probably won't be able to)
# Please add how much time you spent on this in this counter:

# Hours_Spent_On_This_Code = 4  

from time import sleep as wait

print("Boas-vindas à Calculadora de Proporcionalidade Direta!")
print("Código disponível no Github - https://github.com/glxxyxafonso")
wait(2)

print("Antes de começarmos, preciso de uma valor de base para a constante de proporcionalidade direta.")

x = float(input("Insira o valor de X: "))
y = float(input("Insira o valor de f(X): "))

k = y / x
print("Temos um valor de base, que é", k)

while True:
    x2 = float(input("Insira o valor de X:"))
    y2 = float(input("Insira o valor de f(X)"))
    k2 = y2 / x2
    
    if k2 == k:
        print("No momento, tem constante de proporcionalidade direta.")
    else:
        print("Não tem constante de proporcionalidade direta.")
        print("Adeus!")
        wait(2)
        quit()
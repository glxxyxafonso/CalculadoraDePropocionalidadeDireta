# Version 1.0
# Code available in English at https://github.com/glxxyxafonso/

# Dear programmer,
# When I made this code, only god and I knew how it worked.
# Now, only god knows how it works!!
# If you are trying to optimise this code (that you probably won't be able to)
# Please add how much time you spent on this in this counter:

# Hours_Spent_On_This_Code = 1

from time import sleep as wait

print("Boas-vindas á Calculadora de Proporcionalidade Direta!")
print("Código disponível no Github - https://github.com/glxxyxafonso")
wait(2)

numone = input("Insira o X: ")
print()
numonetwo = input("Insira o f(X): ")
numoneresult = float(numonetwo) / float(numone) # Quando pedi um input, deu-me erro por ser string. O float converte. 

print("Efetuei o cálculo e deu", numoneresult)

numtwo = input("Insira o X (o outro X): ")
print()
numtwotwo = input("Insira o f(X) (o outro f(X): ")
print()
numtworesult = float(numtwotwo) / float(numtwo) # Repeti a mesma coidsa que na linha 9. 

if numtworesult == numoneresult:
  print("No momento, é uma proporcionalidade direta.")
  print()
  print("Vamos continuar.")
else: 
  print("Não é uma proporcionalidade direta.")
  print("Obrigado por teres usado esta calculadora!")
  quit()

numthree = input("Insira o terceiro X: ")
print()
numthreetwo = input("Insira o terceiro f(X): ")
numthreeresult = float(numthreetwo) / float(numthree)

if numthreeresult == numoneresult:
  print("No momento, é uma proporcionalidade direta.")
  print()
  print("Vamos continuar.")
else:
  print("Não é uma proporcionalidade direta.")
  print("Obrigado por teres usado esta calculadora!")
  quit()

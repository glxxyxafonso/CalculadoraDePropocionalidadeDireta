# Version 1.2
# Code available in English at https://github.com/glxxyxafonso/

# Dear programmer,
# When I made this code, only god and I knew how it worked.
# Now, only god knows how it works!!
# If you are trying to optimise this code (that you probably won't be able to)
# Please add how much time you spent on this in this counter:

# Hours_Spent_On_This_Code = 2

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
  print("No momento, é uma propocionalidade direta.")
  print()
  print("Vamos continuar.")
  print("Se deseja acabar, faça CTRL+C")
  wait(3)
else: 
  print("Não é uma propocionalidade direta.")
  print("Obrigado por teres usado esta calculadora!")
  quit()

numthree = input("Insira o terceiro X: ")
print()
numthreetwo = input("Insira o terceiro f(X): ")
numthreeresult = float(numthreetwo) / float(numthree)

if numthreeresult == numoneresult:
  print("No momento, é uma propocionalidade direta.")
  print()
  print("Vamos continuar.")
  print("Se deseja acabar, faça CTRL+C")
  wait(3)
else:
  print("Não é uma propocionalidade direta.")
  print("Obrigado por teres usado esta calculadora!")
  quit()

numfour = input("Insira o quarto X: ")
print()
numfourtwo = input("Insira o quarto f(X): ")
numfourresult = float(numfourtwo) / float(numfour)

if numfourresult == numoneresult:
  print("No momento, é uma propocionalidade direta.")
  print()
  print("Se deseja acabar, faça CTRL+C")
  wait(3)
else:
  print("Não é uma propocionalidade direta.")
  print("Obrigado por teres usado esta calculadora!")
  quit()

numfive = input("Insira o quinto X: ")
print()
numfivetwo = input("Insira o quinto f(X): ")
numfiveresult = float(numfivetwo) / float(numfive)

if numfiveresult == numoneresult:
  print("No momento, é uma propocionalidade direta.")
  print()
  print("Se deseja acabar, faça CTRL+C")
  wait(3)
else:
  print("Não é uma propocionalidade direta.")
  print("Obrigado por teres usado esta calculadora!")
  quit()

numsix = input("Insira o sexto X: ")
print()
numsixtwo = input("Insira o sexto f(X): ")
numsixresult = float(numsixtwo) / float(numsix)

if numsixresult == numoneresult:
  print("No momento, é uma propocionalidade direta.")
  print()
  print("Se deseja acabar, faça CTRL+C")
  wait(3)
else:
  print("Não é uma propocionalidade direta.")
  print("Obrigado por teres usado esta calculadora!")
  quit()

numseven = input("Insira o sétimo X: ")
print()
numseventwo = input("Insira o sétimo f(X): ")
numsevenresult = float(numseventwo) / float(numseven)

if numoneresult == numsevenresult:
  print("No momento, é uma propocionalidade direta.")
  print()
  print("Se deseja acabar, faça CTRL+C")
  wait(3)
else:
  print("Não é uma propocionalidade direta.")
  print("Obrigado por teres usado esta calculadora!")
  quit()

numeight = input("Insira o oitavo X: ")
print()
numeighttwo = input("Insira o oitavo f(X): ")
numeightresult = float(numeighttwo) / float(numeight)

if numeightresult == numoneresult:
  print("No momento, é uma propocionalidade direta.")
  print()
  print("Se deseja acabar, faça CTRL+C")
  wait(3)
else:
  print("Não é uma propocionalidade direta.")
  print("Obrigado por teres usado esta calculadora!")
  quit()

numnine = input("Insira o nono X: ")
print()
numninetwo = input("Insira o nono f(X): ")
numnineresult = float(numninetwo) / float(numnine)

if numnineresult == numoneresult:
  print("No momento, é uma propocionalidade direta.")
  print()
  print("Se deseja acabar, faça CTRL+C")
  wait(3)
else:
  print("Não é uma propocionalidade direta.")
  print("Obrigado por teres usado esta calculadora!")
  quit()

numten = input("Insira o décimo X: ")
print()
numtentwo = input("Insira o décimo f(X): ")
numtenresult = float(numtentwo) / float(numten)

if numtenresult == numoneresult:
  print("É uma propocionalidade direta.")
  print()
  print("O utilizador chegou ao limite de X e f(X) que pode inserir. Obrigado por ter usado a calculadora!")
  wait(4)
else:
  print("Não é uma propocionalidade direta.")
  print("Obrigado por teres usado esta calculadora!")
  quit()x

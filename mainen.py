# Version 2.0
# Code available in English at https://github.com/glxxyxafonso/ (but you are in the english version of the code...)

# Dear programmer,
# When I made this code, only god and I knew how it worked.
# Now, only god knows how it works!!
# If you are trying to optimise this code (that you probably won't be able to)
# Please add how much time you spent on this in this counter:

# Hours_Spent_On_This_Code = 4

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
        x = smart_float("Insert the X element: ")
        y = smart_float("Insert the f(X) element: ")
     
        if None in [x, y]:
            done = True
        else:
            k = y / x
            print(f"x={x}, f({x})={y}, Constant of direct proportionality: {k}")
        
            if constant is None:
                constant = k
                
            if constant != k:
                print("The Constant of direct proportionality is different! That is ilegal!!!")
                done = True

print("Welcome to the constant of direct proportionality calculator!")
print("Code available on Github - https://github.com/glxxyxafonso")
print("V2 made by https://github.com/jpedrodias - Thank you :)")
wait(2)

done = False
while not done:
    option = ""
    while option not in  ["S", "N"]:
        option = input("Let's start? (S/N) ").upper()
        
    if option == 'N':
        done = True
    else:
        checamento_de_proporcionalidade()

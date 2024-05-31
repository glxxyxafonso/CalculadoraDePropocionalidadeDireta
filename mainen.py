# Version 3.0
# Code available in English at https://github.com/glxxyxafonso/

# Dear programmer,
# When I made this code, only god and I knew how it worked.
# Now, only god knows how it works!!
# If you are trying to optimise this code (that you probably won't be able to)
# Please add how much time you spent on this in this counter:

# Hours_Spent_On_This_Code = 4  

from time import sleep as wait

print("Welcome to the Direct Proportional Constant Calculator!")
print("Code available on Github - https://github.com/glxxyxafonso")
wait(2)

print("Before starting, I need a base value to calculate the constant of proportionality.")

x = float(input("Insert the X value: "))
y = float(input("Insert the f(X) value: "))

k = y / x
print("We have a base value, which is", k)

while True:
    x2 = float(input("Insert the X value: "))
    y2 = float(input("Insert the f(X) value: "))
    k2 = y2 / x2
    
    if k2 == k:
        print("At the moment, we have a constant of proportionality.")
    else:
        print("There's no constant of proportionality in this case.")
        print("Goodbye!")
        wait(2)
        quit()
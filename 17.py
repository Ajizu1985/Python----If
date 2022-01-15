#Exs17
dig1 = int(input("Pls enter digit1 = "))
dig2 = int(input("Pls enter digit2 = "))
dig3 = int(input("Pls enter digit3 = "))

if (dig3>dig2 and dig2>dig1) or (dig1>dig2 and dig2>dig3) :
    digX = dig1*2
    digY = dig2*2
    digZ = dig3*2
    print("Dig1=", digX)
    print("Dig2=", digY)
    print("Dig3=", digZ)
else:
    digX = -dig1
    digY = -dig2
    digZ = -dig3
    print("Dig1=", digX)
    print("Dig2=", digY)
    print("Dig3=", digZ)

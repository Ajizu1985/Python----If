#Exs19
dig1 = int(input("Pls enter digit1 = "))
dig2 = int(input("Pls enter digit2 = "))
dig3 = int(input("Pls enter digit3 = "))
dig4 = int(input("Pls enter digit4 = "))
if (dig1==dig2 and dig2==dig3 and dig1!=dig4):
    print("Not equal digit is fourth digit=", dig4)
elif (dig1==dig2 and dig2==dig4 and dig1!=dig3):
    print("Not equal digit is third digit=", dig3)
elif (dig1==dig3 and dig3==dig4 and dig1!=dig2):
    print("Not equal digit is second digit=", dig2)
elif (dig2==dig3 and dig3==dig4 and dig1!=dig4):
    print("Not equal digit is first digit=", dig1)
else:
    print("Pls enter digits as required")

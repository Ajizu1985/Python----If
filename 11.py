#Exs11
digit1=int(input("Enter digit1:"))
digit2=int(input("Enter digit2:"))
if(digit1>digit2 or digit1<digit2):
    if(digit1>digit2):
        A=digit1
        B=digit1
        print("A=", A)
        print("B=", B)
    else:
        A=digit2
        B=digit2
        print("A=", A)
        print("B=", B)
else:
    A=0
    B=0
    print("A=", A)
    print("B=", B)

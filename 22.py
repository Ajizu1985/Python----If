#Exs22
X = int(input("Pls enter digit for X to check in which quarter dot lies= "))
Y = int(input("Pls enter digit for Y to check in which quarter dot lies= "))

if (X>0 and Y>0):
    print("It does lie on 1st quarter")
elif (X<0 and Y>0):
    print("It does lie on 2nd quarter")
elif (X<0 and Y<0):
    print("It does lie on 3rd quarter")
elif (X>0 and Y<0):
    print("It does lie on 4th quarter")
else:
    print("It does not lie on any quarter")
#Exs21
X = int(input("Pls enter digit for X to check whether dot lies on the coordinate plane= "))
Y = int(input("Pls enter digit for Y to check whether dot lies on the coordinate plane= "))

if (X==0 and Y==0):
    print("0")
elif ((X>0 or X<0) and Y==0):
    print("1")
elif (X==0 and (Y>0 or Y<0)):
    print("2")
else:
    print("3")

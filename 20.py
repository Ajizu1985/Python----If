#Exs20
A = int(input("Pls enter digit for A = "))
B = int(input("Pls enter digit for B = "))
C = int(input("Pls enter digit for C = "))
X= B - A
Y= C - A
if (X>Y):
    print("Closest to A is C. Distance is=", Y)
else:
    print("Closest to A is B. Distance is=", X)
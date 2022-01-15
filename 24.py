#Exs25
import math
x = int(input("Pls enter digit for x= "))

if x>0:
    res = 2*math.sin(x)
    print(f"f({x})=", res)
elif x<=0:
    res1 = x - 6
    print(f"f({x})=", res1)
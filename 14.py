#Exs14
dig1 = int(input("Pls enter digit1 = "))
dig2 = int(input("Pls enter digit2 = "))
dig3 = int(input("Pls enter digit3 = "))

if dig1>dig2 and dig2>dig3:
    print(f"{dig3} is the smallest digit and {dig1} is the highest digit")
if dig1>dig3 and dig3>dig2:
    print(f"{dig2} is the smallest digit and {dig1} is the highest digit")
if dig2>dig1 and dig1>dig3:
    print(f"{dig3} is the smallest digit and {dig2} is the highest digit")
if dig2>dig3 and dig3>dig1:
    print(f"{dig1} is the smallest digit and {dig2} is the highest digit")
if dig3>dig1 and dig1>dig2:
    print(f"{dig2} is the smallest digit and {dig3} is the highest digit")
if dig3>dig2 and dig2>dig1:
    print(f"{dig1} is the smallest digit and {dig3} is the highest digit")

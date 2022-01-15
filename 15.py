#Exs15
dig1 = int(input("Pls enter digit1 = "))
dig2 = int(input("Pls enter digit2 = "))
dig3 = int(input("Pls enter digit3 = "))

if dig1>dig2 and dig2>dig3:
    dig = dig1+dig2
    print(f"Sum of {dig1}+{dig2} = {dig}")
if dig1>dig3 and dig3>dig2:
    dig = dig1+dig3
    print(f"Sum of {dig1}+{dig3} = {dig}")
if dig2>dig1 and dig1>dig3:
    dig = dig1+dig2
    print(f"Sum of {dig1}+{dig2} = {dig}")
if dig2>dig3 and dig3>dig1:
    dig = dig2+dig3
    print(f"Sum of {dig2}+{dig3} = {dig}")
if dig3>dig1 and dig1>dig2:
    dig = dig1+dig3
    print(f"Sum of {dig1}+{dig3} = {dig}")
if dig3>dig2 and dig2>dig1:
    dig = dig2+dig3
    print(f"Sum of {dig2}+{dig3} = {dig}")

#Exs9
digit1=float(input("Enter digit1:"))
digit2=float(input("Enter digit2:"))
if(digit1>digit2):
    temp=digit1
    digit1=digit2
    digit2=temp
    print(f"digit1={digit1}, digit2={digit2}")
else:
    temp=digit2
    digit2=digit1
    digit1=temp
    print(f"digit1={digit1}, digit2={digit2}")
    

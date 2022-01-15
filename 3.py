#Exs3
digit = int(input("Enter a digit: "))

if digit > 0:
    digit +=1
    print("Digit is", digit)
elif digit == 0:
    digit = 10
    print("Digit is", digit)
else:
    digit -= 2
    print("Digit is", digit)

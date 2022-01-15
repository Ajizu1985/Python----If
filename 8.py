#Exs8
numbers = [101, -15]
for i in numbers:
    if(numbers[0]>numbers[1]):
        print(f"{numbers[0]} = first, {numbers[1]} = second")
        break
    else:
        print(f"{numbers[1]} = first, {numbers[0]} = second")
        break

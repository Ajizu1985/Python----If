#Exs5
digits = [-1, 15, 6]
counter1 = 0
counter2 = 0
for item in digits:
    if (item>0):
        counter1 += 1
    if (item<0):
        counter2 += 1
print("Positive digits are", counter1)
print("Negative digits are", counter2)

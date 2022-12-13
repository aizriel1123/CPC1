data1 = 0
data2 = 0
num = input("Enter a number or press Enter to quit: ")

while num:
    data1 += 1
    data2 += float(num)
    num = input("Enter a number or press Enter to quit: ")
    total = data1/data2

print("The sum is", data2, "\nThe average is", total)





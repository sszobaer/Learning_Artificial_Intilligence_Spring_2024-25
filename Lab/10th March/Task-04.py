#Max number finder
a = int(input("Enter the number you want to input in your list: "))
listOfNumbers = []
for i in range(a):
    y = int(input("Input the number: "))
    listOfNumbers.append(y)
print(listOfNumbers)
largest_number = listOfNumbers[0]
for i in listOfNumbers:
    if i>largest_number:
        largest_number = i
print(f"The largest number is {largest_number}")

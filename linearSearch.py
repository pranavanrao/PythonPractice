def linearSearch(a, size, x) :
    for i in range(size) :
        if (a[i] == x) :
            return i
    return -1

size = int(input("Enter the size of an array : "))

a = []

for i in range(size) :
    element = input(f"Enter the array item {i+1}: ")
    a.append(element)

print("The array is : ")
for i in range(size) :
    print(a[i], end=" ")

x = input("\nEnter the element to be searched in an array : ")
result = linearSearch(a, size, x)

if result == -1 :
    print("The item entered is not in the array")
else :
    print("The item is present in the index ", result+1)
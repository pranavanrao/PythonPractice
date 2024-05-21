def binarySearch(a, low, high, x) :
    while low <= high :
        mid  = low + (high - low) // 2

        if a[mid] == x :
            return mid

        if a[mid] < x :
            low = mid + 1
        else :
            high = mid -1

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
result = binarySearch(a, 0, size-1, x)

if result == -1 :
    print("The item entered is not in the array")
else :
    print("The item is present in the index ", result)
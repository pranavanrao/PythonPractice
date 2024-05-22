def selectionSort(a, size) :
    for i in range(size-1) :
        min = i
        for j in range(i+1, size) :
            if (a[j] < a[min]) :
                min = j
        a[i], a[min] = a[min], a[i]

size = int(input("Enter the size of an array : "))

a = []

for i in range(size) :
    element = input(f"Enter the array item for index {i}: ")
    a.append(element)

print("The unsorted array : ")
for i in range(size) :
    print(a[i], end=" ")

print("\nThe sorted array :")

selectionSort(a,size)

for i in range(size) :
    print(a[i], end=" ")
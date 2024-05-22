def swapItems(a, i, j) :
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def selectionSort(a, size) :
    for i in range(size) :
        for j in range(i+1, size) :
            if (a[j] < a[i]) :
                swapItems(a, i, j)
        print(a[i], end=" ")

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
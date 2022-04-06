def bubbleSort(arr):
    n = len(arr)
    for i in range(0, n ):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [12,34,4,56,23]
bubbleSort(arr)
for i in range(len(arr)):
    print(arr[i])
def selectSort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
arr = [12,34,4,56,23]
selectSort(arr)
for i in range(len(arr)):
    print(arr[i])
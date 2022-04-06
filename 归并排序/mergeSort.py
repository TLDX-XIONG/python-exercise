def merge(arr, left, mid, right):
    i, j, k = left, mid+1, 0
    while(i <= mid and j <= right):
        if(arr[i] < arr[j]):
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        tmp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        tmp[k] = arr[j]
        j += 1
        k += 1
    for i in range(right-left+1):
        arr[i+left] = tmp[i]

def sort(arr, left, right):
    if(left < right):
        mid = (right - left) // 2 + left
        sort(arr, left, mid)
        sort(arr, mid+1, right)
        merge(arr, left, mid, right)

def mergeSort(arr):
    n = len(arr)
    sort(arr, 0, n-1)

arr = [12,34,4,56,23,12,7,3,10,54,67]
tmp = [0]*len(arr)
mergeSort(arr)
for i in range(len(arr)):
    print(arr[i])
def binarySearch(arr, x):
    left, right = 0, len(arr)-1
    while(left <= right):
        mid = (right - left) // 2 + left
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [2,3,4,5,7,10,12]
x = int(input('please input number to be search: '))
result = binarySearch(arr, x)
if(result != -1):
    print('index:', result)
else:
    print('no existing.')
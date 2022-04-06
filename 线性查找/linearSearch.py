def linearSearch(arr, x):
    n = len(arr)
    for i in range(n):
        if(arr[i] == x):
            return i
    return -1
arr = [1,2,3,4,5,6,7,8,9,10]
x = int(input('please input number to be searched: '))
ans = linearSearch(arr, x)
if(ans != -1):
    print('index:',ans)
else:
    print('nubmber no existing.') 
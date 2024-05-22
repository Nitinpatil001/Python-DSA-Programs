def bubblesort(arr):
    for iteration in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
            #print(arr)
    return arr
arr=[6,3,7,8,2,9]
bubblesort(arr)
print(arr)
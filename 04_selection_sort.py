def selectionsort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
arr=[4,2,6,5,9,8]
selectionsort(arr)
print(arr)
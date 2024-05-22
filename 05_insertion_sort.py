def insertionsort(arr):
    for i in range(1, len(arr)):
        key= arr[i]
        last= i-1
        
        while last>=0 and key<arr[last]:
            arr[last+1]=arr[last]
            last = last-1
            
        arr[last+1]=key
        
arr=[3,5,2,7,5,7]
insertionsort(arr)
print(arr)
        
def partition(arr,low,high):
    p=arr[low]
    i=low+1
    j=high
            
    while True:
        while i<=j and arr[i]<=p:
            i+=1
        while i<=j and arr[j]>=p:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]   
    return j

def quicksort(arr,low,high):
    if low < high:
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)
    
arr=[5, 8, 1, 2, 6, 3, 9]
quicksort(arr,0,len(arr)-1) 
print(arr)








    

        
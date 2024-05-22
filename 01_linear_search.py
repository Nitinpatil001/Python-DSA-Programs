def linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return -1
arr=[2,3,5,7,8,9]
target=8
result=linearsearch(arr,target)

if result != -1:
    print(f"Target found at {result}")
else:
    print("Target not found")    
    
    
    
    
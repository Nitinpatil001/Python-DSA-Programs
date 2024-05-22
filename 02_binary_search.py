def binarysearch(arr,target):
    left=0
    rigth=len(arr)-1
    
    while rigth>=left:
        middle=(rigth+left)//2
        middle_element=arr[middle]
        
        if target==middle_element:
            return middle
        elif target>middle_element:
            left=middle+1
        else:
            rigth=middle-1
arr=[2,3,4,5,6,8]
target=8
result=binarysearch(arr,target)

print(f"Target found at {result} ")
def binarysearch(arr,target):
    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        if arr[mid]<target:
            left=mid+1
        if arr[mid]>target:
            right=mid-1
    return -1

arr=list(map(int,input().split(",")))
target=int(input())

result=binarysearch(arr,target)
 
if result !=-1:
    print(f" the value {target} found at {result}")
else:
    print(f"{target} not found")
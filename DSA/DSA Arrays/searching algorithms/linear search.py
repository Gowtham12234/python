def linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr=list(map(int,input().split(",")))
target=int(input())
result=linearsearch(arr,target)

if result!=-1:
    print(f"the {target} found at{result}")
else:
    print(f"value {target} not found")
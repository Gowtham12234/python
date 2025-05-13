arr=list(map(int,input().split(",")))
n=len(arr)
for i in range(n):
    index_value=i
    present_value=arr[i]

    for j in range(i-1,-1,-1):
        if arr[j]>present_value:
            arr[j+1]=arr[j]
            index_value=j
        else:
            break
    arr[index_value]=present_value
print("soreted array using insertion sort is ",arr)

#approach1

arr=list(map(int,input().split(",")))

n=len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print("sorted array",arr)

#approach2

ar=list(map(int,input().split(",")))
n=len(ar)
swapped=False
for i in range(n-1):
    for j in range(n-i-1):
        if ar[j]>ar[j+1]:
            ar[j],ar[j+1]=ar[j+1],ar[j]
            swapped=True
    if not swapped:
        break
print("sorted array:",ar)
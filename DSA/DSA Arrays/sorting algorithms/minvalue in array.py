arr=list(map(int,input().split(","))) #declaring the array taking input from user 
min_arr=arr[0]  # intialize the mininmum value with first index..
for i in arr:
    if i < min_arr:
        min_arr=i
print("min element in the array is ",min_arr)



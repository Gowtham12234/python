arr=list(map(int,input().split(",")))  # declaring array from user input
n=len(arr)
for i in range(n):                     # running outer loop for length of array..

    min_index=i                         # storing mininum value as the first value 

    for j in range(i+1,n):               # runnuing inner loop for finding least value than i 

        if arr[j]<arr[i]:                   # the value that is less than i should be swapped 
            min_index=j                     # updating the leadt value

    arr[i],arr[min_index]=arr[min_index],arr[i] # swapping the values 

print ("sorted array:",arr)                       # printing the sorted array..



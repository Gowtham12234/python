def partiton(array,high,low):
    pivot =array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i+=1
            array[i],array[j]=array[j],array[i]
        array[i+1],array[high]=array[high],array[i+1]
        return i+1
    def quicksort(arrat,low=0,high=None):
        if high is None:
            high=len(array)-1
        while low<high:
            pivot_index=partiton(array,low,high)
            
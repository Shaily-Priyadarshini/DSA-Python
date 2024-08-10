def partition(arr,low,high):

    pivot=arr[low]
    i=low+1
    j=high
    while True:
        while i<=j and arr[i]<=pivot:
            i+=1
        while i<=j and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quickSort(arr,low,high):
    if low<high:

        pi=partition(arr,low,high)
        quickSort(arr,0,pi-1)
        quickSort(arr,pi+1,high)


    return
# arr=[7,4,5,2,1]
arr=[1]
n=len(arr)
quickSort(arr,0,n-1)
print(arr)
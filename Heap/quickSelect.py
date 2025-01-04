
def partition(l,r,arr):
    storeR = r
    pivot = arr[r]
    r = r-1
    while l < r:
        if arr[l]> pivot:
            arr[l], arr[r]  = arr[r], arr[l]
            r -= 1
        else:
            l += 1
    arr[l+1], arr[storeR] = arr[storeR], arr[l+1] 
    return l

def quickSelect(arr,l,r,k):
    pivotIndex = partition(l,r,arr)
    if pivotIndex == k - 1:
        return arr[pivotIndex]
    elif k - 1 > pivotIndex:
        return quickSelect(arr,pivotIndex + 1, r,k)
    else:
        return quickSelect(arr,l,pivotIndex - 1,k)

arr = [15,10,4,3,20,7]
k = 1
print(quickSelect(arr,0,len(arr)-1,k))

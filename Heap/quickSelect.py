
def partition(l,r,arr):
    pivot = arr[r]
    i = l
    for j in range(l,r):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


def quickSelect(arr,l,r,k):
    pivotIndex = partition(l,r,arr)
    if pivotIndex == k - 1:
        return arr[pivotIndex]
    elif k - 1 > pivotIndex:
        return quickSelect(arr,pivotIndex + 1, r,k)
    else:
        return quickSelect(arr,l,pivotIndex - 1,k)

arr = [15,10,4,3,20,7]
k = 6
print(quickSelect(arr,0,len(arr)-1,k))

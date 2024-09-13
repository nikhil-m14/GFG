#Question: Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. 
# Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

#CODE:

def search(arr, x): #optimized
        
    if x in arr:
        return arr.index(x)
    return -1

def search(arr, x): # Brute Force

    for i in range(len(arr)):
            if arr[i] == x:
                return i

    return -1

def search(arr, x): # Only works for sorted array # two pointer method # Worse Case
        
        arr.sort() # sorted before 
        i = 0
        j = len(arr) - 1
        
        while i <= j:
            mid = (i + j) // 2
            
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                i = mid + 1
            else:
                j = mid - 1
                
        return -1
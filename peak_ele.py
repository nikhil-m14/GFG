# Question: Given an 0-indexed array of integers arr[] of size n, find its peak element and return it's index.
#  An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).
# Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

# CODE:

def peakElement(arr, n):
    maxi = 0
    index = 0
    
    for i in range(n):
        
        if arr[i] > maxi:
            maxi = arr[i]
            index = i
    return index


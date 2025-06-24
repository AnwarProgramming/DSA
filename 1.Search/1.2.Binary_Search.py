"""
Implementation of Binary Search Algorithm
Args: L-list of numbers, v-searching element
Pre-condition: Input list must be sorted.
Returns: Index i, if element is found otherwise False
"""

# Case 1: When the element k is found in the list L
# Case 2: When the element k is not found in the list L

def binarysearch(L, v):
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (low + high) // 2
        if L[mid] < v:
            low = mid + 1
        elif L[mid] > v:
            high = mid - 1
        else:  
            return mid # Case 1
    return False # Case 2


# Example usage
L = [1, 3, 4, 78, 90]
print(binarysearch(L, 78))  # Output: 3
print(binarysearch(L, 6))   # Output: False
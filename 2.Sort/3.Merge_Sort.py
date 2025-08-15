"""
Implementation of Merge Sort algorithm in Python.

"""
"""
Let's implement Merge function that merges two sorted list A and B into a single sorted list C.
"""
# Case 1: When both lists A and B have elements for comparing
# Case 2: If list B is over, shift all elements of list A to list C
# Case 3: If list A is over, shift all elements of list B to list C
# Return the merged list C

def merge(A, B): # Merge two sorted lists A and B
    m, n = len(A), len(B)
    C,i,j=[],0,0
    while i < m and j < n:  # Case 1
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    while i < m:  # Case 2
        C.append(A[i])
        i += 1
    while j < n:  # Case 3 
        C.append(B[j])
        j += 1
    return C

"""
Let's implement Merge Sort function that divides the problem into sub-problems i.e. sub-lists
"""
# Base case: If list contains only one element or no element
# Recursively call Merge Sort on left halves of the list
# Recursively call Merge Sort on right halves of the list
# Merge the two sorted list Left_Half and Right_Half

def merge_sort(L):
    n = len(L)
    if n <= 1:  # Base case
        return L
    mid = n // 2
    Left_Half = merge_sort(L[:mid])  # Recursively call Merge Sort on left half
    Right_Half = merge_sort(L[mid:])  # Recursively call Merge Sort on right half
    return merge(Left_Half, Right_Half)  # Merge the two sorted halves


# Example usage
L = [89, 4, 17, 34, 3, 1] 
print("Original list:", L)
sorted_list = merge_sort(L)
print("Sorted list:", sorted_list) # Output: [1, 3, 4, 17, 34, 89]
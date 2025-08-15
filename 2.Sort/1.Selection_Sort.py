"""
Implementation of Selection Sort Algorithm
Args: L-list of integers
Returns: sorted list L
"""

# Case 1: When list contains 1 or none elements
# Case 2: In each iteration find smallest elemeent and place it in right position

def selection_sort(L):
    n = len(L)
    if n <= 1: # Case 1
        return L
    for i in range(n): # Case 2
        min_index = i
        for j in range(i + 1, n): 
            if L[j] < L[min_index]: # Find the minimum element in remaining unsorted array
                min_index = j
        L[i], L[min_index] = L[min_index], L[i] # Swap the found minimum element with the first element
    return L


# Example usage
L = [64, 25, 12, 22, 11]
print("Original list:", L)
sorted_list = selection_sort(L)
print("Sorted list:", sorted_list)  # Output: [11, 12, 22, 25, 64]
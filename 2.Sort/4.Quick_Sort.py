"""
Function1:
   Implement partition() function
   Args: L-list of integers, lower-starting index, upper-ending index
    Returns: Index of pivot element finally it is placed
"""
# Case 1: If element at L[i] > pivot
# Case 2: If element at L[j] <= pivot

def partition(L, lower, upper):
    pivot = L[lower]
    i = lower
    for j in range(lower + 1, upper + 1):
        if L[j] <= pivot:  # Case 2
            i += 1
            L[i], L[j] = L[j], L[i]  # Swap elements
    L[lower], L[i] = L[i], L[lower]  # Place pivot in the right position
    return i  # Return index of pivot element



"""
Function2:
    Implement recursive quick_sort() function
    Args: L-list of integers, lower-starting index, upper-ending index
    Returns: Finally sorted list of L
"""
# General Case 1: Call quick sort on left partition of pivot
# General Case 2: Call quick sort on right partition of pivot
# Base Case: return list L

def quick_sort(L, lower, upper):
    if lower < upper:  # Base case
        pivot_index = partition(L, lower, upper)  # Get pivot index
        quick_sort(L, lower, pivot_index - 1)  # General Case 1
        quick_sort(L, pivot_index + 1, upper)  # General Case 2
    return L  # Base Case: Return sorted list L


# Example usage
L = [78, 2, 5, 2, 1, 7, 34, 49, 14, 3]
print("Original list:", L)
sorted_list = quick_sort(L, 0, len(L) - 1)
print("Sorted list:", sorted_list)  # Output: [1, 2, 2, 3, 5, 7, 14, 34, 49, 78]
"""
Implementation of Insertion Sort algorithm in Python.

"""
# Case 1: When list contains 1 or none elements
# Case 2: In each iteration compare the current element and the previous elements
# And swap them, when necessary

def insertion_sort(L):
    n = len(L)
    if n <= 1:  # Case 1
        return L
    for i in range(1, n):  # Case 2
        j = i
        while j > 0 and L[j - 1] > L[j]:  # And swap them, when necessary
            L[j - 1], L[j]=  L[j], L[j - 1]
            j -= 1
    return L

# Example usage
L = [67, 4, 2, 88, 1, 6]
print(insertion_sort(L))  # Output: [1, 2, 4, 6, 67, 88]
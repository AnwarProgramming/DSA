"""
Let's implement a linear search algorithm
Args: L-list of numbers, v-searching element
Returns: Index i, if element is fund otherwise False
"""

# Case 1: When the element v is found in the list L
# Case 2: When the element v is not found in the list L

def naivesearch(L,v):
    for i in range(len(L)):
        if v==L[i]: # Case 1
            return i
    return False # Case 2

# Example usage
L = [90, 4, 78, 3, 1]
print(naivesearch(L, 78))  # Output: 2
print(naivesearch(L, 6))  # Output: False

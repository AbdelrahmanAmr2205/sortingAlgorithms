# Function to perform Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: return if array has 1 or 0 elements
    
    mid = len(arr) // 2  # Find the middle index
    left = merge_sort(arr[:mid])  # Recursively sort left half
    right = merge_sort(arr[mid:])  # Recursively sort right half
    
    return merge(left, right)  # Merge sorted halves

# Function to merge two sorted arrays
def merge(left, right):
    result = []  # Array to store merged elements
    i = j = 0  # Pointers for left and right arrays
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # Choose the smaller element
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])  # Append remaining elements from left array
    result.extend(right[j:])  # Append remaining elements from right array
    return result

# Example usage
arr1 = [3, 6, 8, 10, 1, 2, 1]

print("Before Merge Sort:", (arr1))  
print("After Merge Sort:", merge_sort(arr1))  
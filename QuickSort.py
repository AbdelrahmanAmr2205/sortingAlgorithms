import random

# Function to partition the array using a randomized pivot
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Select a random pivot
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot with last element
    pivot = arr[high]  # Pivot value
    i = low - 1  # Index for smaller element
    
    for j in range(low, high):
        if arr[j] < pivot:  # If current element is smaller than pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Move pivot to correct position
    return i + 1  # Return partition index

# Function to perform Quick Sort using the randomized partitioning method
def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot = randomized_partition(arr, low, high)  # Get pivot index
        randomized_quick_sort(arr, low, pivot - 1)  # Sort left subarray
        randomized_quick_sort(arr, pivot + 1, high)  # Sort right subarray

# Main function for Quick Sort
def quick_sort(arr):
    randomized_quick_sort(arr, 0, len(arr) - 1)  # Sort entire array
    return arr

# Example usage
arr1 = [3, 6, 8, 10, 1, 2, 1]

print("Before Quick Sort:", (arr1))
print("After Quick Sort:", quick_sort(arr1)) 
def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

def main():
    arr = [5, 4, 7, 2, 9, 3]
    BubbleSort(arr)
    print(arr)

main()

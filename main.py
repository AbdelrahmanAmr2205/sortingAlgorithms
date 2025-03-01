import random
import time
import selectionSort
import BubbleSort
import InsertionSort

def generate_random_array(size):
    return [random.randint(-9999999,9999999) for i in range(size)]

#takes the a string of the name of the sorting algorithm and its size, and returns the time it took
def get_time_for_algorithm(algorithm, size): 
    arr= generate_random_array(size)
    if algorithm == "Selection Sort":
        starting_time= time.time() * 1000
        selectionSort.selectionSort(arr.copy())
        ending_time= time.time() * 1000
    elif algorithm == "Bubble Sort":
        starting_time= time.time() * 1000
        BubbleSort.BubbleSort(arr.copy())
        ending_time= time.time() * 1000
    else:
        starting_time= time.time() * 1000
        InsertionSort.InsertionSort(arr.copy())
        ending_time= time.time() * 1000
    print(algorithm + " - size: " + str(size) + " - time: " + str(ending_time - starting_time) + " milliseconds")

def main():
    get_time_for_algorithm("Selection Sort", 100)
    get_time_for_algorithm("Bubble Sort", 100)
    get_time_for_algorithm("Insertion Sort", 100)
    get_time_for_algorithm("Selection Sort", 1000)
    get_time_for_algorithm("Bubble Sort", 1000)
    get_time_for_algorithm("Insertion Sort", 1000)
    get_time_for_algorithm("Selection Sort", 5000)
    get_time_for_algorithm("Bubble Sort", 5000)
    get_time_for_algorithm("Insertion Sort", 5000)
    get_time_for_algorithm("Selection Sort", 10000)
    get_time_for_algorithm("Bubble Sort", 10000)
    get_time_for_algorithm("Insertion Sort", 10000)
    get_time_for_algorithm("Selection Sort", 25000)
    get_time_for_algorithm("Bubble Sort", 25000)
    get_time_for_algorithm("Insertion Sort", 25000)
    get_time_for_algorithm("Selection Sort", 50000)
    get_time_for_algorithm("Bubble Sort", 50000)
    get_time_for_algorithm("Insertion Sort", 50000)
    get_time_for_algorithm("Selection Sort", 100000)
    get_time_for_algorithm("Bubble Sort", 100000)
    get_time_for_algorithm("Insertion Sort", 100000)
    get_time_for_algorithm("Selection Sort", 250000)
    get_time_for_algorithm("Bubble Sort", 250000)
    get_time_for_algorithm("Insertion Sort", 250000)

main()

# 1. Using a while loop, implement bubble sort algorithm


def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        j = 0
        while j < len(arr) - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            j += 1
        if not swapped:
            break
    return arr
        
# test data 
data = [-2, 45, 0, 11, -9]
print(bubble_sort(data))



# 2. Using a while loop, implement selection sort algorithm

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        j = i + 1
        while j < len(arr):
            if arr[min_index] > arr[j]:
                min_index = j
            j += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# test data
data = [-2, 45, 0, 11, -9]
print(selection_sort(data))



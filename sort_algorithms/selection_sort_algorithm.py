
# Selection sort in Python


# def selectionSort(array, size):
   
#     for step in range(size):
#         min_idx = step

#         for i in range(step + 1, size):
         
#             # to sort in descending order, change > to < in this line
#             # select the minimum element in each loop
#             if array[i] < array[min_idx]:
#                 min_idx = i
         
#         # put min at the correct position
#         (array[step], array[min_idx]) = (array[min_idx], array[step])


# data = [-2, 45, 0, 11, -9 ,-2]
# size = len(data)
# selectionSort(data, size)
# print('Sorted Array in Ascending Order:')
# print(data)

# selection sort using a while loop

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
data = [-2, 45, 0, 11, -9 ,-2]
print(selection_sort(data))
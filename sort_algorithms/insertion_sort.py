
def insertion_sort(arr):
    for i in range(1, len(arr)):
        first_element_index = i - 1
        nxt_element = arr[i]
        # Compare the current element with next one

        while (arr[first_element_index] > nxt_element) and (first_element_index >= 0):
            arr[first_element_index + 1] = arr[first_element_index]
            first_element_index -= 1
        arr[first_element_index + 1] = nxt_element
    return arr

print(insertion_sort([1, 4,2,-44,-12,56,23]))
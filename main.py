def selection_sort(arr):
    n = len(arr)
    # Determine the length of the array.

    for pos in range(n - 1):
        # Iterate through the array up to the second-to-last element
        # because the last one will automatically be in the correct position.

        for k in range(pos + 1, n):
            # Iterate over the rest of the array to find
            # the actual smallest element.

            if arr[k] < arr[pos]:
                # If an element is found that is smaller than the one
                # currently considered the smallest.

                arr[k], arr[pos] = arr[pos], arr[k]
                # Swap the smallest element found with the element at index 'k'.
                # This places the smallest element in the current correct position.

    return arr
    # Return the now sorted array.


print(selection_sort([6, 2, 6, 3, 8, 9, 1, 5]))
# Print the result of the selection sort on the given list.

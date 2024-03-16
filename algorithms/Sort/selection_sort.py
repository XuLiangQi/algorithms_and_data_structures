def selection_sort(arr: list) -> list:
    """Sort the given numerical array (list) in ascending order

    Parameters:
    -----------

        arr: List of numerical values

    Return:
    -------

        sorted_arr: List sorted in ascending order
    """
    sorted_arr = []
    for _ in range(len(arr)):
        # Find the smallest number to register
        min_num = arr[0]
        for num in arr:
            if num < min_num:
                min_num = num
        sorted_arr.append(min_num)
        arr.remove(min_num)

    return sorted_arr

if __name__ == "__main__":
    arr = [3, 6, 2, 4, 1, 4, 9, 2]
    print(f"List before sort: {arr}")
    sorted_arr = selection_sort(arr)
    print(f"List after sort: {sorted_arr}")

    str_arr = ["banana", "apple", "grape", "orange", "kiwi"]
    print(f"String list before sort: {str_arr}")
    sorted_str_arr = selection_sort(str_arr)
    print(f"String list after sort: {sorted_str_arr}")
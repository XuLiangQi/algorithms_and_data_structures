def quick_sort(arr: list) -> list:
    """Sort the givin list in ascending order using
    quick sort algorithm.
    
    Parameters:
    ----------
    arr: List of numerical values.
    
    Return:
    -------
    sorted_arr: Sorted numerical list
    """
    if len(arr) < 2:
        return arr
    else:
        pivit = arr[0]
        less = []
        more = []
        for num in arr[1:]:
            if num <= pivit:
                less.append(num)
            elif num > pivit:
                more.append(num)
        less = quick_sort(less)
        more = quick_sort(more)
        sorted_arr = less + [pivit] + more
        return sorted_arr


if __name__ == "__main__":
    arr = [3, 6, 2, 4, 1, 4, 9, 2]
    print(f"List before sort: {arr}")
    sorted_arr = quick_sort(arr)
    print(f"List after sort: {sorted_arr}")

    str_arr = ["banana", "apple", "grape", "orange", "kiwi"]
    print(f"String list before sort: {str_arr}")
    sorted_str_arr = quick_sort(str_arr)
    print(f"String list after sort: {sorted_str_arr}")
"""4 approaches for solving 2-sum problem."""


def binary_search(arr, num):
    start_idx, end_idx = 0, len(arr)
    while start_idx < end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if arr[mid_idx] == num:
            return mid_idx
        elif arr[mid_idx] > num:
            end_idx = mid_idx
        else:
            start_idx = mid_idx + 1
    return float('-inf')


def brute_force(arr, target):
    for idx in range(len(arr)):
        for idx2 in range(idx+1, len(arr)):
            if arr[idx] + arr[idx2] == target:
                return True
    return False


def hashing(arr, target):
    visited = set()
    for num in arr:
        if target - num in visited:
            return True
        visited.add(num)
    return False


def bin_search(arr, target):
    arr.sort()
    for idx, num in enumerate(arr):
        idx2 = binary_search(arr, target - num)
        if idx2 >= 0 and (idx != idx2):
            return True
    return False


def inward_walk(arr, target):
    arr.sort()
    left_idx, right_idx = 0, len(arr) - 1
    while left_idx < right_idx:
        total = arr[left_idx] + arr[right_idx]
        if total == target:
            return True
        elif total < target:
            left_idx += 1
        else:
            right_idx -= 1
    return False


if __name__ == "__main__":
    # Let's test if among lists given below, there are numbers that sum to 2.
    target_sum = 2
    lists = ([], [3, 1, 8, 4, 1, 1], [2], [1, 1])
    for l in lists:
        print(l.__repr__(), "Target: {}".format(target_sum))
        for fnt in (brute_force, hashing, bin_search, inward_walk):
            print("{}:".format(fnt.__name__.replace('_', ' ').capitalize()), fnt(l, target_sum))
        print('')

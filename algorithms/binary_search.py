def binary_search(items, target):
    lo = 0
    hi = len(items)
    while lo < hi:
        mid = int((lo + hi) / 2)
        current = items[mid]

        if target == current:
            return True

        if target > current:
            lo = mid
        if target < current:
            hi = mid

    return False

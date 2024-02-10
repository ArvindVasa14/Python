def binsearch(nums, x):
    nums = list(enumerate(nums))
    nums.sort(key = lambda x : x[1])
    low = 0
    high = len(nums)-1
    
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if nums[mid][1] == x:
            return nums, mid

        elif nums[mid][1] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


nums1 = [76, 1, 31, 41, 29, 26, 78, 13, 64, 50, 66, 63, 81, 78, 6, 69, 77, 24, 36, 88, 60, 44, 24, 74, 58]

search = 63

sortednums, result = binsearch(nums1, search)


if result != -1:
    print(f"Search element {search} is present at index {sortednums[result][0]}.")
else:
    print(f"Search element {search} not found")
    

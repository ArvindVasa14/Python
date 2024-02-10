
nums = [69, 93, 13, 27, 33, 40, 38, 57, 28, 31, 80, 32, 95, 19, 70, 91, 15, 26, 46, 18, 94, 71, 94, 75, 30]

nums.sort()
print(nums)

search = 13

nums2 = nums.copy()
nums2 = list(enumerate(nums2))
idx = len(nums2)


while len(nums2)>1:
    if nums2[0][1] == search:
        print(f'Search element {search} can be found at index position {nums2[0][0]}')
        break
    idx = len(nums2)//2
    if nums2[idx][1] == search:
        print(f'Search element {search} can be found at index position {nums2[idx][0]}')
        break
    else:
        if  search < nums2[idx][1]:
            nums2 = nums2[:idx]
        else:
            nums2 = nums2[idx:]
else:
    print(f'Search element {search} cannot be found')
    
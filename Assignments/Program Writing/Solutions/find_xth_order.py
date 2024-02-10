#solution 1

def getX(x,nums):
    if len(nums)!=0 and x <= len(nums):
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] <= nums[i]:
                    count += 1
            if count == x:
                return nums[i]
    else:
        return 0
        
print(getX(2, [6, 3, -1, 5]))

print(getX(4, [5, 10, -3, -3, 7, 9]))


#solution 2

def getX(x, nums):
  # write your code here
  if len(nums)!=0 and x <= len(nums):
    nums.sort()
    return nums[x-1]
  else:
    return 0

print(getX(2, [6, 3, -1, 5]))

print(getX(4, [5, 10, -3, -3, 7, 9]))
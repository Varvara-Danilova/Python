nums=list(map(int, input().split()))
m = 0
n = 0
for i in range(len(nums)):
    count = nums.count(nums[i])
    if m < count:
        m = count
        nums[i] = n







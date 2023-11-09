nums = list(map(int, input().split()))
min_pos = 0
max_pos = 0
for i in range(len(nums)):
    if nums[max_pos] < nums[i]:
        max_pos = i
    if nums[min_pos] > nums[i]:
        min_pos = i
nums[min_pos],nums[max_pos] = nums[max_pos],nums[min_pos]
for i in range(len(nums)):
    print(nums[i], end=' ')

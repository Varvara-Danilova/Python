nums = list(map(int, input().split()))
el = list(map(int, input().split()))
nums.insert(el[0], el[1])
for i in range(len(nums)):
    print(nums[i], end=' ')
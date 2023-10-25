# Bubble Sort
def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
nums = [34, 78, 28, 93, 24, 1]
print("Before Sorting")
print(nums)
sort(nums)
print("After Sorting")
print(nums)

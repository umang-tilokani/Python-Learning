# Selection Sort
def sort(nums):
    for i in range(6):
        minpos = i
        for j in range(i, 7):
            if nums[j] < nums[minpos]:
                minpos = j
            temp = nums[i]
            nums[i] = nums[minpos]
            nums[minpos] = temp
nums = [43, 8, 50, 70, 13, 86, 9]
print("Before Sorting")
print(nums)
sort(nums)
print("After Sorting")
print(nums)

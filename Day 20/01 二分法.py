# 算法：是高效解决问题的方法
# 算法之二分法

# 需求：有一个按照从小到大排列的数字列表
#       需要从该数字列表中找到我们想要的那一个数字
#       如何做更高效


nums = [-3, 4, 7, 10, 13, 21, 43, 77, 89]
find_num = 10


# 方案一：整体遍历效率太低
# for num in nums:
#     if num == find_num:
#         print('find it')
#         break

# 方案二：二分法
def find(find_num, nums):
    mid = len(nums) // 2
    print(nums)
    if len(nums) == 0:
        print('can\'t find')
        return
    if nums[mid] == find_num:
        print('find it')
        return
    elif find_num < nums[mid]:
        find(find_num, nums[0:mid])
    elif find_num > nums[mid]:
        find(find_num, nums[mid+1:])

find(99, nums)

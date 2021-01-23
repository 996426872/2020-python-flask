nums = [1,1,2,2,2,2,2,4,5,5,9,9,9,9,10]
# print(li)
# del li[0]
# print(li)
# del li[2]
# print(li)
# del li[6]
# print(li)
# li.pop(1)
# print(li)

n = len(nums)
a = nums[0]
# for num in nums:
#     if num == a:
#         nums.remove(num)
#     else:
#         a = num
#     print(a)
#     print(nums)
n = len(nums)
a = nums[0]
nums = [1,1,2,2,2,2,2,4,5,5,9,9,9,9,10]
print("处理前nums:",nums)
print("------------------------------------")
index = 1
while index < len(nums):
    if nums[index] == a:
        del nums[index]
        print("删除字符:", a)
        print("删除字符后数组是：", nums)
    else:
        print("已经处理字符是：", a)
        print("已经处理数组下标是：",index)
        a = nums[index]
        index = index + 1
        print("待处理字符是：", a)
        print("待处理数组下标是：",index)
    print("------------------------------")

print("------------------------------------")
print("处理后nums:",nums)
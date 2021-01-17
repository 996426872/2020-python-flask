def get_sorted_numbers(nums):
    nums = set(nums)
    return sorted(nums)


while True:
    try:
        n = eval(input())
        stu_nums = []
        for i in range(0, n):
            stu_nums.append(eval(input()))
        sorted_nums = get_sorted_numbers(stu_nums)
        for num in sorted_nums:
            print(num)
    except:
        break
'''
while True:
    try:
        a , res = int (input ()) , set ()
        for i in range (a): res.add (int (input ()))
        for i in sorted (res): print (i)
    except:
        break
'''
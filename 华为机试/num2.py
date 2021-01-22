def getFar(nums):
    park_len = len(nums)
    start = 0
    end = 0
    max_len = 0

    while end < park_len - 1:
        start = end
        while nums[start] == 1 and start < park_len:
            start = start + 1
            print("start", start)
        end = start+1
        print("end", end)
        while nums[end] == 0 and end < park_len:
            end = end + 1
            print("end", end)
        if end == park_len and nums[end-1]==0:
            k = end - start
            max_len = max(max_len , k)
            return max_len
        if start == 0:
            k = end - start
        else:
            if end - start > 2:
                k = (end-start+1)//2
        max_len = max(max_len,k)
        print("k",)
        print("max_len" , max_len)

    return max_len


while True:
    nums = input().split(",")
    nums = [eval(i) for i in nums]
    print(nums)
    print(getFar(nums))

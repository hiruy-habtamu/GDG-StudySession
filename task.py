def MaxNum(nums:list):
    num = float('-inf')
    for i in nums:
        if num < i:
            num = i
    return num
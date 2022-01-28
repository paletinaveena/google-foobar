def solution(xs):
    if len(xs) == 1:
        return str(xs[0])
    if xs.count(0) == len(xs):
        return str(0)
    xs = [x for x in xs if x != 0]
    positive_nums = [x for x in xs if x > 0]
    negative_nums = [x for x in xs if x < 0]
    if len(negative_nums) % 2 != 0:
        negative_nums.sort()
        negative_nums = negative_nums[:-1]
    if len(negative_nums) == 0 and len(positive_nums) == 0:
        return str(0)
    FinalList = positive_nums + negative_nums
    result = reduce(lambda x, y : x * y, FinalList)
    return str(result)

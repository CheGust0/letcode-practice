#给定一个整数数组 nums 和一个整数目标值 target
#请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
from ctypes import HRESULT


class Solution:
    def twonum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range (i+1, n):
                if (nums[i]+nums[j]) == target:
                    return [i, j]
        return "can't find"

def main():
    a = Solution()
    nums = [3,5,7,9]
    target = 8
    result = a.twonum(nums, target)
    print(result)

main()
"给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和"

"利用Kadane算法求最大子数组和"
class Solution:
    def maxSubArray(self,nums):
        if not nums:
            return 0

        current_sum = max_sum = nums[0]
        """动态规划的思路，当当前数前面的最大子数组和小于零，则由当前数重新开始计算最大和，放置于current_sum"""
        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

def main():
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

if __name__ == '__main__':
    main()

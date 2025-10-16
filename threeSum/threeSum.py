"""给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]
满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
请你返回所有和为 0 且不重复的三元组。"""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        k = 0
        for k in range(len(nums)-2):
            """由于nums[j]>=nums[i]>nums[k]"""
            """如果nums[k]>0,则说明找不到三数相加等于零"""
            if nums[k]>0:
                break
            """跳过重复的nums[k]，避免出现重复的组合"""
            if k>0 and nums[k] == nums[k-1]:
                continue
            i,j = k+1,len(nums)-1
            while i<j:
                s = nums[k]+nums[i]+nums[j]

                if s<0:
                    """当s<0应使i向右移动，并避免重复组合"""
                    i+=1
                    while i<j and nums[i]==nums[i-1]:i+=1
                elif s>0:
                    """当s>0应使j向左移动，并避免重复的组合"""
                    j-=1
                    while i<j and nums[j]==nums[j+1]:j-=1
                else:
                    """当s=0则保存此时的组合，并使i,j同时移动"""
                    res.append([nums[k],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i < j and nums[i] == nums[i - 1]: i+=1
                    while i < j and nums[j] == nums[j + 1]: j-=1
        return res

def main():
    s = Solution()
    print(s.threeSum([-1,0,1,2,2,-1,-4]))

main()

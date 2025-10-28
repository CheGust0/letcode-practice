"给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积"
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1]*n
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1,-1,-1):      #range函数左闭右开，故停止在-1才能取到0
            answer[i] *= right
            right *= nums[i]

        return answer

def main():
    s = Solution()
    print(s.productExceptSelf([1,2,3,4,5]))

if __name__ == '__main__':
    main()

"给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。"

class Solution:
    def rotate(self, nums, k):
        """通过逆转数组达到轮转的效果"""
        def reverse(i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        n = len(nums)
        k %= n
        """将数组所有数先逆转一次
        然后将前k个逆转，达到轮转过来的效果
        最后将其他所有进行逆转达到顺序的效果"""
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        return nums

def main():
    sol = Solution()
    print(sol.rotate([1, 2, 3, 4, 5], 3))

if __name__ == '__main__':
    main()
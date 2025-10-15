"给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。"
class Solution:
    def maxArea(self, height):
        n = len(height)
        max_area = 0
        i,j = 0,n-1

        "两个指针一个指向开头，一个指向结尾"
        "从两边开始遍历寻找最大的接水量"
        while i<j:
            if height[i]<height[j]:
                max_area = max(max_area,(j-i)*height[i])
                i+=1
            else:
                max_area = max(max_area,(j-i)*height[j])
                j-=1
        return max_area

def main():
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))

main()
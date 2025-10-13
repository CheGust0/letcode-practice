class Solution:
    def longestConsecutive(self, nums):
        "将数列改编为哈希数列"

        "当num = [1,145,54,23]时"
        "哈希数列st = [1,23,54,145]"
        st = set(nums)
        num = 0
        for x in st:
            if x-1 in st:
                "判断x是否为一个连续序列的首位，如果不是则跳过"
                continue
            y = x+1
            while y in st:
                y+=1
            num = max(num, y-x)
        return num

def main():
    s = Solution()
    nums = [1,2,3,0,34,5]
    print(s.longestConsecutive(nums))

main()
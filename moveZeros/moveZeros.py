"给定一个数组nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序"

class Solution:
    def moveZeros(self, nums):

        j = 0
        for i in range(len(nums)):
            if nums[i]:
                "当nums[i]!=0时，将其与nums[j]交换，即将非零元素移向左侧"
                nums[i],nums[j] = nums[j],nums[i]
                j+=1

"使用双指针，将非零元与零元分开，非零元都移向左侧，零移向右侧"

def main():
    s = Solution()
    nums = [0,1,15,78,56,0,12]
    print(nums)
    s.moveZeros(nums)
    print(nums)

main()
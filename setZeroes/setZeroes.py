"给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0"

class Solution():
    def setZeroes(self, matrix):
        """下列两个数组用于存储某一行或某一列是否存在0"""
        zero_in_row = [0 in row for row in matrix]
        zero_in_col = [0 in col for col in zip(*matrix)]   #zip函数用于将列转置为行

        for i,row0 in enumerate(zero_in_row):   #enumerate函数用于返回索引以及索引对应的值
            for j,col0 in enumerate(zero_in_col):
                if row0 or col0:
                    matrix[i][j] = 0

def main():
    s = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print("更改前")
    print(matrix)
    print("更改后")
    s.setZeroes(matrix)
    print(matrix)

if __name__ == '__main__':
    main()
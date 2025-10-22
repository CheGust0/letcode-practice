"""以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。"""

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda p:p[0])#根据数组左端点进行排序

        ans = []
        for p in intervals:
            if ans and p[0]<=ans[-1][1]:#判断区间是否有相交
                ans[-1][1] = max(ans[-1][1], p[1])#若相交更新右端点的值
            else:
                ans.append(p)

        return ans

def main():
    s = Solution()
    intervals = [[1,3],[2,6],[8,10],[9,14],[15,18]]
    ans = s.merge(intervals)
    print(ans)

if __name__ == '__main__':
    main()
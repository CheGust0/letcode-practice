"给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。"

class Solution:
    def findAnagrams(self,s,p):
        s_len,p_len = len(s), len(p)
        """如果被搜索字符串小于需要搜索字符串长度，则直接返回空数组"""
        if s_len<p_len:
            return []

        ans = []
        """初始化计数数组，将每一个都初始化为0"""
        s_count = [0]*26
        p_count = [0]*26
        for i in range(p_len):
            """该循环体内将第一组窗口进行索引"""
            """例如s中前三个为cba，将每一个字母放入数组中对应的位置
            故s_count中为[1,1,1,0,0,0 ...]"""
            s_count[ord(s[i])-97] += 1
            p_count[ord(p[i])-97] += 1

        if s_count == p_count:
            ans.append(0)

        """该循环中去除左端字母，将窗口进行滑动"""
        for i in range(s_len-p_len):
            s_count[ord(s[i])-97] -= 1
            s_count[ord(s[i+p_len])-97] +=1

            if s_count == p_count:
                ans.append(i+1)

        return ans

def main():
    s = Solution()
    print(s.findAnagrams("cbaebabacd","abc"))

if __name__ == "__main__":
    main()
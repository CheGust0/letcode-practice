"给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。"
class Solution:
    def lengthOfLongestSubstring(self, s):
        ret,dic,i = 0,{},-1

        for j in range((len(s))):
            if s[j] in dic:
                """检查到重复字母，更新左指针，使两指针中间无重复字母"""
                i = max(dic[s[j]],i)
            dic[s[j]] = j #记录下哈希表
            ret = max(ret, j-i)

        return ret

def main():
    s = Solution()
    string = "abcabcbb"
    print(s.lengthOfLongestSubstring(string))

main()

"给你一个字符串数组，请你将字母异位词组合在一起。可以按任意顺序返回结果列表"

class Solution:
    def groupAnagrams(self, str:list[str]) -> list[list[str]]:
        "使用字典解决"
        str_dict = {}

        "将数组中的每一个单词重新排序后作为字典的子键"
        for s in str:
            sorted_s = ''.join(sorted(s))
            "判断是否字典中有该子键"
            if sorted_s not in str_dict:
                str_dict[sorted_s] = []

            str_dict[sorted_s].append(s)

        return list(str_dict.values())


def main():
    s = Solution()
    arr = ["aet","eat","tan","nat","bat"]
    print(s.groupAnagrams(arr))

main()

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        first_string = strs[0]

        for i in range(len(first_string)):
            char = first_string[i]
            
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return first_string[:i]
        
        return first_string

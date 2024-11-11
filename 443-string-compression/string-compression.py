class Solution:
    def compress(self, chars: List[str]) -> int:
        s= ""
        # s = s + str(chars[0])
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count+=1
            else:
                s = s + str(chars[i-1])
                if count > 1:
                    s = s + str(count)
                count = 1
        s = s + str(chars[-1])
        if count > 1:
            s = s + str(count)
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)



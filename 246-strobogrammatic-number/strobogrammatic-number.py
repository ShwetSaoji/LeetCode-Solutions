class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        sb_num = ""

        for i in range(len(num)):
            if num[i] == "6":
                sb_num += "9"
            elif num[i] == "9":
                sb_num += "6"
            elif num[i] in "180":
                sb_num += num[i]
            else:
                return False
        
        return num[::-1] == sb_num


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        rem = 0 
        ans = ""

        i , j = 0 , 0 

        while i < len(num1) and j < len(num2):
            tot = int(num1[i]) + int(num2[j]) + rem
            if tot > 9:
                rem = tot//10
                ans += str(tot%10)
            else:
                ans += str(tot)
                rem = 0
            i, j = i + 1, j + 1
        
        while i < len(num1):
            tot = int(num1[i]) + rem
            if tot > 9:
                rem = tot//10
                ans += str(tot%10)
            else:
                ans += str(tot)
                rem = 0
            i += 1
        
        while j < len(num2):
            tot = int(num2[j]) + rem
            if tot > 9:
                rem = tot//10
                ans += str(tot%10)
            else:
                ans += str(tot)
                rem = 0
            j += 1
        if rem > 0:
            ans += str(rem)

        return ans[::-1]

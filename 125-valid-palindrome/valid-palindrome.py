class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l , r = 0 , len(s)-1

        # while l < r:
        #     while not s[l].isalpha() and l < r:
        #         l += 1
        #     while not s[r].isalpha() and r > l:
        #         r -= 1
            
        #     if s[l].lower() == s[r].lower():
        #         l += 1
        #         r -= 1
        #     else:
        #         return False
        
        # return True

        string = ""
        for i in s:
            if i.isalnum():
                print(i)
                string += i.lower()
        return string == string[::-1]
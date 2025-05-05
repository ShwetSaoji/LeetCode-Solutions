class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        parsed = ''
        i = 0 
        while i < len(abbr):
            if abbr[i].isalpha():
                parsed += abbr[i]
                i += 1
            else:
                if abbr[i] == "0":
                    return False
                num = 0 
                while i < len(abbr) and not abbr[i].isalpha():
                    num = num * 10 + int(abbr[i])
                    i += 1
                while num > 0 and len(parsed) <= len(word):
                    parsed += "6"
                    num -= 1
        print(parsed)
        if len(word) != len(parsed):
            return False
        else:
            for i in range(len(word)):
                if word[i] != parsed[i] and parsed[i] != "6":
                    return False
        
        return True
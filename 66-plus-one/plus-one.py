class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # num = ''.join(digits)
        # print(num)

        for i in range(len(digits)):
            digits[i] = str(digits[i])
        
        num = str(int(''.join(digits))+1)
        num_str = list(num)

        for i in range(len(num_str)):
            num_str[i] = int(num_str[i])
        
        return num_str
        
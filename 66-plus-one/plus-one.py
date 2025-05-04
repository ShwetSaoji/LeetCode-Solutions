class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = ''.join(str(i) for i in digits)
        digits = str(int(digits) + 1)
        return [int(i) for i in digits]
        
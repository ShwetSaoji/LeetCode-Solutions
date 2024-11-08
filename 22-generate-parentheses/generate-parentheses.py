class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openC, closeC):
            if openC == closeC == n:
                res.append("".join(stack))
            
            if openC < n:
                stack.append("(")
                backtrack(openC + 1, closeC)
                stack.pop()
            
            if closeC < openC:
                stack.append(")")
                backtrack(openC, closeC + 1)
                stack.pop()

        backtrack(0 , 0)
        return res

            
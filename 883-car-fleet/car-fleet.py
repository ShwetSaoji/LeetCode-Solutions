class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        stack = []

        for p, s in cars:
            if stack and (target-p)/s <= stack[-1]:
                continue
            else:
                stack.append((target-p)/s)

        return len(stack)
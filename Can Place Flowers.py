class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        count = 0
        prev = 0
        for i in range(len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and prev == 0:
                count += 1
                flowerbed[i] = 1
                prev = flowerbed[i]
            else:
                prev = flowerbed[i]
        
        if flowerbed[-1] == 0 and prev == 0:
            count += 1
            
        return n <= count

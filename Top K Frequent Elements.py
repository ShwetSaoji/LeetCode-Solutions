class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        res=[]
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        
        arr = sorted(dic.items(), key = lambda it: it[1], reverse=True)
        print(arr)
        arr = list(map(lambda it: it[0], arr))
        return arr[:k]
        
        # dic_keys = list(dic.keys())
        # dic_values = list(dic.values())
        # dic_sort = sorted(list(dic.values()), reverse=True)[:k]
        
        # print(dic_sort)
        # for i in dic_sort:
        #     pos = dic_values.index(i)
        #     res.append(dic_keys[pos])
        #     dic_values.pop(pos)
        
        # return res

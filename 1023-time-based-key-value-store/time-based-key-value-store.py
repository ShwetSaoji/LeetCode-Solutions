class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([value, timestamp])
        else:
            self.timeMap[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if len(self.timeMap) == 0:
            return ""
        value_list = self.timeMap.get(key, [])
        l , r = 0 , len(value_list) - 1
        res = ""
        while l <= r:
            m = (l+r)//2
            if value_list[m][1] <= timestamp:
                res = value_list[m][0]
                l = m + 1
            else:
                r = m - 1 
        
        return res 
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
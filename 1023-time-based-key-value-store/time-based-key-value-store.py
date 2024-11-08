class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append([value, timestamp])
        else:
            self.hmap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        val_list = self.hmap.get(key, [])
        l , r = 0, len(val_list) - 1
        res = ""
        while l <= r:
            m = (l+r)//2
            if val_list[m][1] <= timestamp:
                res = val_list[m][0]
                l = m + 1
            else:
                r = m -1
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
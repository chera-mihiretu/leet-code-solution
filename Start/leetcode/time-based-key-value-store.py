class TimeMap:
    def __init__(self):
        self.ds = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        get_list = self.ds[key]
        index =  bisect.bisect_left(get_list, [timestamp])
        if index < len(get_list) and get_list[index][0] == timestamp:
            return  get_list[index][1]
        if index == 0:
            return ""
        return get_list[index-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
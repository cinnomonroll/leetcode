# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

# Example 1:
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]


class TimeMap:
    def __init__(self):
        self.store = {} # key: list of pairs[val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])

        # binary search
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                result = values[mid][0] # store valid value
                left = mid + 1 # search right portion
            else:
                right = mid - 1 # search left portion
        
        return result
    

# reason for -> result = values[mid][0]
# tm.set("foo", "bar", 1)
# tm.set("foo", "bar2", 4)
# print(tm.get("foo", 5))  # Expected: "bar2"
# Binary search will hit:
# mid = 0 → timestamp = 1 ≤ 5 → result = "bar"
# mid = 1 → timestamp = 4 ≤ 5 → result = "bar2" (better match) -> 2 loops 


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))  # → "bar"
    print(tm.get("foo", 3))  # → "bar"
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))  # → "bar2"
    print(tm.get("foo", 5))  # → "bar2"





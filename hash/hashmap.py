class MyHashMap:

    def __init__(self):
        self.hashmap = {}

    def put(self, key, value):
        self.hashmap[key] = value

    def get(self, key): 
        return self.hashmap.get(key, -1)

    def remove(self, key):
        if key in self.hashmap:
            del self.hashmap[key]


# Example usage:
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(3))  
obj.put(2, 1)
print(obj.get(2))  
obj.remove(2)
print(obj.get(2))  

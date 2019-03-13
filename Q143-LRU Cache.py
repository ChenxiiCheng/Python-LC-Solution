'''
Question: 
  146. LRU Cache

Descrition: 
  Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
  get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
  put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
  Could you do both operations in O(1) time complexity?

Examples:
  LRUCache cache = new LRUCache( 2 /* capacity */ );

  cache.put(1, 1);
  cache.put(2, 2);
  cache.get(1);       // returns 1
  cache.put(3, 3);    // evicts key 2
  cache.get(2);       // returns -1 (not found)
  cache.put(4, 4);    // evicts key 1
  cache.get(1);       // returns -1 (not found)
  cache.get(3);       // returns 3
  cache.get(4);       // returns 4
'''

#Python3 Code:

'''
思路：
	1.get函数：(1)若key不在dict中，return -1
	  	  (2)若key在dict中，获取且return v
	2.put函数：(1)若key在dict中，则更新这个位置的value
		  (2)若key不在dict中，且cache已满时，用LRU规则踢出去一个，再加入新value
'''

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        v = self.cache.pop(key)
        self.cache[key] = v
        return v
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


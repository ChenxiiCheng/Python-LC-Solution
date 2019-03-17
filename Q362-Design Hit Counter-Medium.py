'''
Question: 
  362. Design Hit Counter

Descrition: 
  Design a hit counter which counts the number of hits received in the past 5 minutes.

  Each function accepts a timestamp parameter (in seconds granularity) and you may assume 
  that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
  It is possible that several hits arrive roughly at the same time.

Examples:

	HitCounter counter = new HitCounter();

	// hit at timestamp 1.
	counter.hit(1);

	// hit at timestamp 2.
	counter.hit(2);

	// hit at timestamp 3.
	counter.hit(3);

	// get hits at timestamp 4, should return 3.
	counter.getHits(4);

	// hit at timestamp 300.
	counter.hit(300);

	// get hits at timestamp 300, should return 4.
	counter.getHits(300);

	// get hits at timestamp 301, should return 3.
	counter.getHits(301); 
'''

#Python3 Code:

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #Solutio n2
        self.queue = collections.deque()
        
        
        #Solution
        #计算过去五分钟内的点击数，同时也可以指定某一秒钟进行点击。
        #那么应该维护一个队列，存储每一次点击的时间，那么新加入一次点击，
        #就把队首所有超出时间范围的点击都删除。
        self.data = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        #Solution 2
        self.queue.append(timestamp)
        
        
        #Solution
        self.data.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        #Solution 2
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()
        return len(self.queue)
        
        
        #Solution
        while self.data and timestamp - self.data[0] >= 300:
            self.data.pop(0)
        return len(self.data)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
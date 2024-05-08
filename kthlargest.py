import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums 
        heapq.heapify(self.heap)
        # print(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        # print(self.heap)

        while(len(self.heap) > self.k):
            heapq.heappop(self.heap)
        
        return self.heap[0]
        # output = []
        # if len(self.heap) > self.k:
        #     # print(self.heap)
        #     heapq.heappop(self.heap)            
        #     # print(self.heap)
        
        # return self.heap[0]
 
        
        # output = []

        # while(self.k > 0):
        #     kth_largest = heapq.heappop(self.nums)
        #     print(kth_largest)
        #     self.k -= 1
        
        # output.append(kth_largest)
        

nums = [4,5,8,2]
obj = KthLargest(3, nums)
param = obj.add(3);   
param = obj.add(5);   
param = obj.add(10);  
param = obj.add(9);   
param = obj.add(4);   
print(param)
# Top K Frequent Elements
#Sorting
class Solution:
    def topkFrequent(self,nums:List[int],k:int)->List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)

        arr = []            
        for num,cnt in count.items():
            arr.apend([cnt,num])
        arr.sort()

        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res 
    
'''TC = o(nlogn) and SC = o(n)'''


'''Min Heap'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
''' TC = o(nlogk) and sc = o(n+k)'''

'''Bucket Sort'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
'''TC = o(n) and SC = o(n)'''

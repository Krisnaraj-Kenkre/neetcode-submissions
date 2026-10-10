class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        keys_list = list(sorted_hashmap.keys())
        return keys_list[:k]
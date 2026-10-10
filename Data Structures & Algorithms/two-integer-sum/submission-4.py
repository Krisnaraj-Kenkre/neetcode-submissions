class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        output = []
        for idx, i in enumerate(nums):
            complement = target - i
            if complement in hashmap:
                complement_idx = hashmap[complement]
                output.append(complement_idx)
                output.append(idx)
                return output
            else:
                hashmap[i] = idx
            

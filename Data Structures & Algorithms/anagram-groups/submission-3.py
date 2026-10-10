class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for idx, i in enumerate(strs):
            orig_i = i
            i = list(i)
            i = sorted(i)
            i = "".join(i)
            if i in hashmap:
                hashmap[i].append(orig_i)
            else:
                hashmap[i] = [orig_i]
        return list(hashmap.values())
        
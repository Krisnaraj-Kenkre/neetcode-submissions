class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []
        output_idx = 0
        for idx, i in enumerate(strs):
            orig_i = i
            i = list(i)
            i = sorted(i)
            i = "".join(i)
            if i in hashmap:
                output[hashmap[i][0]].append(orig_i)
            else:
                hashmap[i] = [output_idx]
                output_idx += 1
                output.append([strs[idx]])
        return output
        
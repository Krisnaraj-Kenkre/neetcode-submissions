class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for i in strs:
            output += str(len(i)) + "_" + i
        return output
        

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "_":
                j += 1 
            
            length = int(s[i:j])
            start = j+1
            end = start + length

            decoded_list.append(s[start:end])
            i = end

        return decoded_list
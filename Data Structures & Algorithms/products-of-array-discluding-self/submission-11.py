class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        has_zero = False
        zero_idx = 0
        has_many_zeros = False
        product = 1

        for idx, i in enumerate(nums):
            if i == 0:
                if has_zero is False:
                    has_zero = True
                    zero_idx = idx
                    continue
                else:
                    has_many_zeros = True
                    return [0] * len(nums)
            else:
                product = product * i

        if has_zero is True:
            output = [0] * len(nums)
            output[zero_idx] = product
            return output
        else:
            for i in nums:
                output.append(int(product/i))

            return output

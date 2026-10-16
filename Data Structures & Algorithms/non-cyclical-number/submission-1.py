class Solution:
    def isHappy(self, n: int) -> bool:
        
        def add_digit_squared(num):
            output = 0
            str_num = str(num)
            for i in str_num:
                output += int(i)**2
            
            return output


        nums_encountered = {}
        last_num = n
        while last_num != 1:

            if last_num in nums_encountered:
                return False

            nums_encountered[last_num] = 1
            last_num = add_digit_squared(last_num)


        return True
class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        
        max_int = 2**31 - 1
        
        while x != 0:
            digit = x % 10
            
            if reversed_num > max_int // 10 or (reversed_num == max_int // 10 and digit > 7):
                return 0
            
            reversed_num = reversed_num * 10 + digit
            x //= 10

        final_reversed_num = sign * reversed_num
        
        if not (-2**31 <= final_reversed_num <= max_int):
            return 0
            
        return final_reversed_num

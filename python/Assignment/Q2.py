# Problem Statement: Reverse Integer
# You are given a signed 32-bit integer x.
# Your task is to reverse the digits of the integer and return the reversed value.
# However, if reversing x causes the value to go outside the signed 32-bit integer range:
# −231≤x≤231−1-2^{31} \le x \le 2^{31} - 1−231≤x≤231−1 then return 0.
# ⚠️ Important Constraint:
# You must solve this problem without using 64-bit integers (signed or unsigned).
# 
# Input
# A single signed integer x
# Output
# An integer representing the reversed digits of x
# Return 0 if the reversed value overflows the 32-bit signed integer range
# 
# Examples
# Example 1
# Input:  x = 123
# Output: 321
# 
# Example 2
# Input:  x = -123
# Output: -321
# 
# Example 3
# Input:  x = 120
# Output: 21
# 
# Task
# Write a program or function to reverse the digits of the given integer while handling overflow conditions appropriately.

def Reverse_Integer(n):
    neg = False
    rev_n = 0
    if n < -(2**31) or n > 2**31 - 1:
        return rev_n
    if n < 0:
        neg = True
        n = abs(n)
    while n > 0:
        rev_n = rev_n * 10 + n % 10
        n //= 10
    return rev_n * -1 if neg else rev_n

print(Reverse_Integer(123))
print(Reverse_Integer(-123))
print(Reverse_Integer(120))
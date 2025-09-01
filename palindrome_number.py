# Given an integer x, return true if x is a palindrome, and false otherwise.


# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def isPalindrome(x: int):
    if x < 0:
        return False
    
    temp = []
    while True:
        if x < 10:
            temp.append(x)
            break
        mod = x % 10
        temp.append(mod)
        x = x // 10
    
    left = 0
    right = len(temp) - 1

    while left <= right:
        if temp[left] == temp[right]:
            left = left + 1
            right = right - 1
        else:
            return False
    
    return True
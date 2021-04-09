class Solution:
    def getSum(self, a: int, b: int) -> int:
        xor=a^b
        carry=a&b
        return add(xor,carry<<1)

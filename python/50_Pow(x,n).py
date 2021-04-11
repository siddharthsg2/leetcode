class Solution:
    def myPow(self, x: float, n: int) -> float:
        isnneg , isxneg= n<0, x<0
        x, n= abs(x), abs(n)
        if n == 0: 
            return 1  
        if n == 1: 
            return 1/x if isnneg else x  
        pwr=self.myPow(x, n//2)
        if n%2 == 0: 
            ans= pwr*pwr
        else: 
            ans= pwr*pwr*x
        if isxneg and n%2==1:
            ans=-ans 
        if isnneg:
            ans= 1/ans
        return ans

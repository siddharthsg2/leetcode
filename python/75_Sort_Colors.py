class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0, count1, count2=0,0,0
        for num in nums:
            if num==0:
                count0+=1
            if num==1:
                count1+=1
            if num==2:
                count2+=1
        sum=count0+count1+count2
        for i in range(sum):
            if(count0>0):
                nums[i]=0
                count0-=1
            elif(count1>0):
                nums[i]=1
                count1-=1
            else:
                nums[i]=2
                count2-=1
        print (nums)

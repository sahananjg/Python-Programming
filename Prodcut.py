import math
def Pro(nums:list):
    a=[]
    for i in range(0,len(nums)):
        temp=nums[i]
        nums[i]=1
        a.append(math.prod(nums))
        nums[i]=temp
    return a
print(Pro([1,2,3,4]))
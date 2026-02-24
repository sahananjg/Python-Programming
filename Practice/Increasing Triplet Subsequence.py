def ITS(nums:list):
    c=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)-1):
            print(nums[i],nums[j],nums[j+1])
            if(nums[i]<nums[j]):
                if(nums[j]<nums[j+1]):
                    return True

    '''if(c>=3):
        return True
    else:
        return False'''



print(ITS([20,100,10,12,5,132]))
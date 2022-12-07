class Solution:
    def search(self, nums, target) -> bool:
        
        
        left = 0
        right = len(nums)-1
        
        
        # this will find the pivot
        i = 0
        if len(nums)<= 3:
            return target in nums
        else:
            while i < len(nums)-2 and nums[i]<= nums[i+1]:
                i +=1
            i+=1
        if target > left:
            right = i-1
        else:
            left = i
        
        def search(target,num,left,right):
            if target == nums[left] or target == nums[right]:
                return True

            if(target > nums[right] or target < nums[left]):
                return False


            if right-left < 5:
                for i in range(left,right+1):
                    if i == target:
                        return True
                return False
            else:
                midPoint = (left + right)//2
                if target < nums[midPoint]:
                    search(target,num,left,midPoint)
                else:
                    search(target,num,midPoint,right)
        return search(target,nums,left,right)
    
    
obj = Solution()

nums = [2,5,6,0,0,1,2]
target = 2

print(obj.search(nums,target))
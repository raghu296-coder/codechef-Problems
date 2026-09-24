class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumx(val):
            cop=val
            suv=0
            while cop!=0:
                dig=cop%10
                suv+=dig
                cop=cop//10
            return suv   
        ans=-1     
        for i in range(len(nums)):
            if sumx(nums[i])==i:
                ans=i
                break
        return ans        
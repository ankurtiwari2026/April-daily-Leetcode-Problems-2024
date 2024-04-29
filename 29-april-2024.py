class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        final=0
        for n in nums:
            final=final^n
        count=0
        while k or final:
            if (k%2)!=(final%2):
                count+=1
            k//=2
            final//=2
        return count            
        

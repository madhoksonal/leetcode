class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #using hashmap for efficiency
        
        seen = {} #create empty dictionary 
        
        for i, value in enumerate(nums): #easier way to iterate through list -- use enumerate()
            #i represents the counter, and value represents the number in the nums array (nums[i])
            
            difference = target - nums[i] #process to find the second number that = target
            #6-3 = 2. it keeps checking if the number in the list is the difference between the num in the list and the target.. if it is, then it is the value we want and we found our solution!
           
            if difference in seen: #if we have found the difference of target-nums[i]
                return [seen[difference], i]
            
            seen[value] = i #adds current nums[i] value 
            #print(i)
            
            
            
### BRUTE FORCE METHOD---------------------
        #final_num = []
        
        #for i in range(0, len(nums)):
        #    for j in range(i+1, len(nums)):
        #        if nums[i] + nums[j] == target:
        #            return (i, j)
        #return []
        
        
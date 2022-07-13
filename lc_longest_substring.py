class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
      
    #we used the sliding window algorithm here -
    #we looked at a window until we reached a duplicate, then changed the window of the substring to include the rest of the string after the duplicate and kept moving like that 
    
        current_letter_start = 0
        longest_substr = 0
        current_length = 0
        substr = {}
        
        for i, letter in enumerate(s): #enumerate saves the index and the element
            
            if letter in substr and substr[letter] >= current_letter_start: #we found a duplicate and the index of the duplicate letter is greater than or equal to the current pointer
                
                current_letter_start = substr[letter] + 1 #start the next substring on the letter after the index of the duplicate
                #substr[letter] shows the index of that letter
                
                current_length = i - substr[letter] #the current length of the substring without a duplicate is the counter (i) minus the index of the duplicate letter
                
                substr[letter] = i #this makes it so the next detection of duplicates will start where the most recent duplicate ended 
                
                #so, abcdab -- the code on line 19 will make the loop check the next substring after d at index 4
                
            
            else: #we have not found a duplicate
                substr[letter] = i
                current_length += 1 #the current length increments by 1 for the longest substring
                if current_length > longest_substr:
                    longest_substr = current_length
            
        return longest_substr
            
            
        
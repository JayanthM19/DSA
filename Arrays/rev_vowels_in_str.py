#https://leetcode.com/problems/reverse-vowels-of-a-string/
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=[]
        vowelSet = set("aeiouAEIOU")

        for sub in s:
            if sub=='a' or sub=='e' or sub=='i' or sub=='o' or sub=='u' or sub=='A' or sub=='E' or sub=='I' or sub=='O' or sub=='U':
                vowels.append(sub)
            
        final=""
        for sub in s:
            if sub not in vowelSet:
                final+=sub
            else:
                final+=vowels[-1]

                vowels.pop()
        
        return final
#https://leetcode.com/problems/valid-palindrome/

class Solution:
    def IsPalindrome(self,s):
        l=0
        r=len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True


if __name__=="__main__":
    s=str(input())
    sol=Solution()
    print(sol.IsPalindrome(s))
    
class Solution:
    def reverseString(self, s: str) -> str:
        reversedStr = ""
        print("The String is : ", s)
        for i in range(len(s), 0, -1):
            reversedStr += s[i-1]
        return reversedStr


string = "Prasad"
ob = Solution()
print("The Reversed String coming from fxn is : ", ob.reverseString(string))
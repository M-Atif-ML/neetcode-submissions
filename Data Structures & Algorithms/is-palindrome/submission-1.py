class Solution:
    def isPalindrome(self, s: str) -> bool:
        cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums ={'0','1','2','3','4','5','6','7','8','9'}
        new_string = []
        filtered = []
        for char in s:
            
            if char != " ":
                if char in cap:
                    new_string.append(char.lower())

                else:
                    new_string.append(char)

        for char in new_string:
            if (ord(char)>=ord("a") and ord(char)<=ord('z')) or char in nums:
                
                filtered.append(char)
                
                
        print(filtered)
        n = len(filtered)
        for i in range(n):
            if filtered[i]!=filtered[n-i-1]:
                return False
        return True

        
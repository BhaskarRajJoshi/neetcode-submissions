class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # cleaned_s = s.replace(" ", "").replace("?", "")
        cleaned_s =""
        for char in s.lower():
            char_num = ord(char)

            if 97 <= char_num <= 122 or  48 <= char_num <= 57:
                cleaned_s += char
            else:
                pass
        if cleaned_s == cleaned_s[::-1]:
            return True
        else:
            return False
            


        
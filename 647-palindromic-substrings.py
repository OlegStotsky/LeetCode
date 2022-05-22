class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for mid in range(0, len(s)):
            ans += self.check(mid, mid, s)
            ans += self.check(mid, mid+1, s)
        return ans
            
    def check(self, l, r, s):
        cnt = 0
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            else:
                break
        
        return cnt

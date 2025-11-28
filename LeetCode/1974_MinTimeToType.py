class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = len(word) + \
            min(abs(ord(word[0])-ord('a')), abs(ord('z')-ord(word[0])+1))
        print(ans)
        for i in range(len(word)-1):

            ans += min(abs(ord(word[i+1])-ord(word[i])), abs(ord('z')-ord(word[i+1]) + 1 + ord(
                word[i]) - ord('a')), abs(ord('z')-ord(word[i]) + 1 + ord(word[i+1]) - ord('a')))
            print(ans)

        return ans

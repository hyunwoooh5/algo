class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        d1 = {'1': 'a', '2': 'b', '3': 'c', '4': 'd',
              '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i'}
        d2 = {'10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q',
              '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}

        s = [i for i in s]
        print(s)
        ind = len(s)-1
        ans = []

        while ind >= 0:
            if s[ind] == '#':
                ans.append(d2["".join(s[ind-2:ind+1])])
                ind -= 2
            else:
                ans.append(d1[s[ind]])
            ind -= 1
            print(ans, ind)

        return "".join(ans[::-1])

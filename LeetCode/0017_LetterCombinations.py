class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        n = len(digits)
        result = []
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(index, path):
            if len(path) == n:
                result.append(path)
                return

            current_digit = digits[index]
            letters = d[current_digit]

            for char in letters:
                backtrack(index+1, path + char)

        backtrack(0, "")

        return result

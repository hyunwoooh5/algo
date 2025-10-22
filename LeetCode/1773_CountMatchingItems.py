class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0

        for item in items:
            if ruleKey == "type":
                if item[0] == ruleValue:
                    ans += 1
            elif ruleKey == "color":
                if item[1] == ruleValue:
                    ans += 1
            elif ruleKey == "name":
                if item[2] == ruleValue:
                    ans += 1

        return ans

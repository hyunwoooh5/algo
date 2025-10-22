class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")

        d = {}
        d[" "] = " "
        index = 0
        for char in key:
            if char not in d:
                d[char] = "abcdefghijklmnopqrstuvwxyz"[index]
                index += 1
        print(d)

        return "".join([d[x] for x in message])

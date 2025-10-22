class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return f'{bin(int(date[:4]))[2:]}-{bin(int(date[5:7]))[2:]}-{bin(int(date[8:10]))[2:]}'

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        hand.sort()

        hash_table = {}

        for i in hand:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        while n > 0:
            min_key = min(hash_table)

            if min_key + groupSize - 1 in hash_table:
                for i in range(min_key, min_key + groupSize):
                    if i in hash_table:
                        hash_table[i] -= 1
                        n -= 1
                        if hash_table[i] == 0:
                            hash_table.pop(i)
                    else:
                        return False
            else:
                return False

        return True


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize:
            return False

        hand.sort()

        hash_table = {}

        for i in hand:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        for num in hand:
            if hash_table[num]:  # prevent 0 and lower
                for i in range(num, num+groupSize):
                    if i not in hash_table:
                        return False
                    hash_table[i] -= 1

        return True


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        hash_table = {}

        for num in hand:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        while n > 0:
            min_key = min(hash_table)

            if min_key + groupSize-1 in hash_table:
                for i in range(min_key, min_key + groupSize):
                    if i in hash_table and hash_table[i] > 0:
                        n -= 1
                        hash_table[i] -= 1
                        if hash_table[i] == 0:
                            hash_table.pop(i)
                    else:
                        return False

            else:
                return False

        return True


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hash_table = {}

        for num in hand:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        sorted_keys = sorted(hash_table.keys())

        for key in sorted_keys:
            if hash_table[key] > 0:
                needed = hash_table[key]

                for i in range(key, key+groupSize):
                    if i not in hash_table or hash_table[i] < needed:
                        return False

                    hash_table[i] -= needed

        return True

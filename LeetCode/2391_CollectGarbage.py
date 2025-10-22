class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m, p, g = 0, 0, 0
        n = len(garbage)

        mc = sum([c.count('M') for c in garbage])
        pc = sum([c.count('P') for c in garbage])
        gc = sum([c.count('G') for c in garbage])

        for i, gar in enumerate(garbage[::-1]):
            if 'M' in gar:
                m = n - 1 - i
                break

        for i, gar in enumerate(garbage[::-1]):
            if 'P' in gar:
                p = n - 1 - i
                break

        for i, gar in enumerate(garbage[::-1]):
            if 'G' in gar:
                g = n - 1 - i
                break

        print(travel[:m], travel[:p], travel[:g])

        return sum(travel[:m]) + sum(travel[:p]) + sum(travel[:g]) + mc + pc + gc

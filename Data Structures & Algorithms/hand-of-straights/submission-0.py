class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        from collections import Counter

        count = Counter(hand)
        hand.sort()

        for h in hand:
            if not count[h]:
                continue
            for i in range(h, h + groupSize):
                if not count[i]:
                    return False
                count[i] -= 1
        return True
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        sorted_hand = sorted(hand)
        cnt = Counter(hand)

        if len(hand) % groupSize != 0:
            return False
        
        for x in sorted_hand:
            if cnt[x] == 0:
                continue
            for card in range(x, x+groupSize):
                if cnt[card] == 0:
                    return False
                cnt[card] -= 1
        return True
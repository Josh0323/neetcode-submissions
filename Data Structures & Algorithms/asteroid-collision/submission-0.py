class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right = []
        for a in asteroids:
            if a < 0:
                while True:
                    if right and right[-1] > 0:
                        if right[-1] > abs(a):
                            break
                        
                        elif right[-1] == abs(a):
                            right.pop()
                            break
                        else:
                            right.pop()
                    else:
                        right.append(a)
                        break
            else:
                right.append(a)

        return right
        
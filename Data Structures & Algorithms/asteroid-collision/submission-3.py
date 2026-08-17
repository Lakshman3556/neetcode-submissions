class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        sk = []

        for i in asteroids:
            if not sk:
                sk.append(i)
            elif i<0:
                des=False
                while sk and sk[-1]>0:
                    if sk[-1]==abs(i):
                        sk.pop()
                        des=True
                        break
                    elif sk[-1]<abs(i):
                        sk.pop()
                    else:
                        des=True
                        break
                if not des:
                    sk.append(i)                  
            else:
                sk.append(i)
        return sk
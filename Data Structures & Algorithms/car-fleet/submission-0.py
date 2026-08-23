class Solution:
    def carFleet(self, target: int, pos: List[int], sp: List[int]) -> int:
        cars = sorted(zip(pos, sp), reverse=True)
        stk=[]
        for pos,sp in cars:
            time=(target-pos)/sp
            if not stk or time>stk[-1]:
                stk.append(time)
        return len(stk)        
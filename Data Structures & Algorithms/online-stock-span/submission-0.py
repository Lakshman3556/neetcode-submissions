class StockSpanner:

    def __init__(self):
        self.stk=[]
        self.s=[]
        

    def next(self, price: int) -> int:
        span=1
        while self.stk and self.stk[-1]<=price:
            self.stk.pop()
            span+=self.s.pop()
        self.stk.append(price)
        self.s.append(span)
        return span   
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)